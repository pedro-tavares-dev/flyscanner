"""
apis_output/terminal.py
-------------------------
Primeira api de saída: um "terminal" dentro da própria interface
(uma caixa de texto na aba Retorno / ou na janela principal) que vai
mostrando as passagens encontradas que bateram com as condições.

Como a interface (interface.py) já escuta o log.py pra atualizar a tela,
aqui a gente simplesmente registra o voo encontrado como uma mensagem
de log tipo SUCESSO com origem "terminal". A interface filtra/realça
essas mensagens na área de "Passagens encontradas".
"""

import log

NOME = "Terminal"

CAMPOS_CONFIG = []  # não precisa de nenhuma configuração/chave


def _formatar(voo: dict) -> str:
    origem = voo.get("origem", "?")
    destino = voo.get("destino", "?")
    tipo = voo.get("tipo_viagem", "?")
    ida = voo.get("data_ida", "?")
    volta = voo.get("data_volta", "")
    valor = voo.get("valor", "?")
    moeda = voo.get("moeda", "")
    cia = voo.get("companhia", "?")
    fonte = voo.get("fonte", "?")

    trecho = f"{origem} -> {destino}"
    datas = f"ida {ida}" + (f" / volta {volta}" if volta and tipo == "ida_volta" else "")
    return f"✈ {trecho} | {datas} | {cia} | {moeda} {valor} | via {fonte}"


def enviar(voo: dict, config: dict, log_callback=None) -> None:
    mensagem = _formatar(voo)
    callback = log_callback or log.registrar
    callback(mensagem, "SUCESSO", "terminal")
