"""
buscador.py
-----------
O "robô". Roda em uma thread separada (pra não travar a interface),
lendo periodicamente:
  1) as apis de entrada configuradas (e suas config/tokens);
  2) as condições cadastradas (condicoes.py);
  3) as apis de saída selecionadas (e suas config);

E fica em loop: consulta cada api_input -> filtra cada voo retornado
com condicoes.passagem_atende() -> se bater, manda pra cada api_output
configurada -> tudo isso reportando passo a passo pro log.py.

Também controla deduplicação simples (não fica reenviando o mesmíssimo
voo a cada ciclo).
"""

import threading
import time

import apis
import condicoes as condicoes_mod
import log
import historico


class Robo:
    def __init__(self, intervalo_segundos: int = 60):
        # Esse intervalo agora atua como um "Intervalo Global" entre as consultas
        self.intervalo_segundos = intervalo_segundos
        self._thread = None
        self._parar_evento = threading.Event()
        self._rodando = False
        self._voos_ja_enviados = set()  # chave simples pra evitar duplicar

        # Preenchidos via configurar() antes de start()
        self.apis_input_selecionadas = {}   # {chave_modulo: config_dict}
        self.apis_output_selecionadas = {}  # {chave_modulo: config_dict}

    def configurar(self, apis_input_selecionadas: dict, apis_output_selecionadas: dict):
        """
        apis_input_selecionadas: {"google_flight": {"api_key": "...", "intervalo_minutos": 60, "ultima_execucao": 0}, ...}
        apis_output_selecionadas: {"terminal": {}, "telegram": {"bot_token": "...", "chat_id": "..."}}
        """
        self.apis_input_selecionadas = apis_input_selecionadas or {}
        self.apis_output_selecionadas = apis_output_selecionadas or {}

    @property
    def rodando(self) -> bool:
        return self._rodando

    def start(self):
        if self._rodando:
            log.registrar_aviso("Robô já está rodando.", origem="buscador")
            return

        if not self.apis_input_selecionadas:
            log.registrar_erro("Nenhuma api de entrada configurada. Robô não iniciado.", origem="buscador")
            return
        if not self.apis_output_selecionadas:
            log.registrar_erro("Nenhuma api de saída configurada. Robô não iniciado.", origem="buscador")
            return

        self._parar_evento.clear()
        self._thread = threading.Thread(target=self._loop, daemon=True)
        self._rodando = True
        self._thread.start()
        log.registrar_sucesso("Robô iniciado.", origem="buscador")

    def stop(self):
        if not self._rodando:
            return
        self._parar_evento.set()
        self._rodando = False
        log.registrar("Robô parado pelo usuário.", nivel="INFO", origem="buscador")

    def _chave_voo(self, voo: dict) -> tuple:
        return (
            voo.get("origem"), voo.get("destino"), voo.get("data_ida"),
            voo.get("data_volta"), voo.get("valor"), voo.get("companhia"), voo.get("fonte"),
        )

    def _loop(self):
        modulos_input = apis.listar_apis_input()
        modulos_output = apis.listar_apis_output()

        fila_apis = list(self.apis_input_selecionadas.keys())
        indice_atual = 0

        while not self._parar_evento.is_set():
            condicoes_atuais = condicoes_mod.carregar()

            if not fila_apis:
                log.registrar_erro("Fila de APIs vazia. Loop interrompido.", origem="buscador")
                break 

            # 1. Pega a API da vez
            chave_input = fila_apis[indice_atual]
            config_input = self.apis_input_selecionadas[chave_input]

            agora = time.time()
            intervalo_api_segundos = config_input.get("intervalo_minutos", 60) * 60
            ultima_exec = config_input.get("ultima_execucao", 0)

            # 2. Avalia o Cooldown
            if (agora - ultima_exec) >= intervalo_api_segundos:
                modulo_input = modulos_input.get(chave_input)
                
                if modulo_input:
                    inicio = time.time()
                    voos = apis.buscar_em(modulo_input, config_input, condicoes_atuais)
                    duracao = round(time.time() - inicio, 2)
                    
                    log.registrar(f"{modulo_input.NOME}: {len(voos)} voos retornados em {duracao}s.", nivel="INFO", origem="buscador")

                    for voo in voos:
                        voo = historico.processar_score(voo)

                        if not condicoes_mod.passagem_atende(voo, condicoes_atuais):
                            continue

                        chave = self._chave_voo(voo)
                        if chave in self._voos_ja_enviados:
                            continue
                        self._voos_ja_enviados.add(chave)

                        log.registrar(f"Passagem bateu com as condições: {voo}", nivel="SUCESSO", origem="buscador")

                        for chave_output, config_output in self.apis_output_selecionadas.items():
                            modulo_output = modulos_output.get(chave_output)
                            if modulo_output:
                                apis.enviar_para(modulo_output, voo, config_output)
                            else:
                                log.registrar_erro(f"Api de saída '{chave_output}' não encontrada.", origem="buscador")

                    # Registra que a API foi consumida
                    self.apis_input_selecionadas[chave_input]["ultima_execucao"] = time.time()

                    # O robô descansa pelo intervalo global apenas quando UMA API FOI EXECUTADA
                    if not self._parar_evento.is_set():
                        log.registrar(f"Aguardando {self.intervalo_segundos}s para a próxima consulta na fila...", nivel="INFO", origem="buscador")
                        self._parar_evento.wait(self.intervalo_segundos)
                else:
                    log.registrar_erro(f"Api de entrada '{chave_input}' não encontrada em apis_input/.", origem="buscador")

            # 3. Avança a fila para a próxima API, independentemente de a anterior ter rodado ou não
            indice_atual = (indice_atual + 1) % len(fila_apis)
            
            # Se todas as APIs estiverem em cooldown, evita um loop infinito enlouquecido da CPU
            # Um mini-sleep de 1 segundo mantém o programa saudável até que alguma API esfrie.
            if not self._parar_evento.is_set():
                 time.sleep(1)

        self._rodando = False
        log.registrar("Loop do robô encerrado.", nivel="INFO", origem="buscador")