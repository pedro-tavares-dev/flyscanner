"""
interface.py
------------
Ponto de entrada da aplicação (é este arquivo que você roda: `python interface.py`).
"""

import json
import os
import queue
import re

import customtkinter as ctk

import apis
import buscador
import condicoes as condicoes_mod
import log
from tkcalendar import DateEntry

ARQUIVO_CONFIG_APIS = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config_apis.json")

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

# --- PALETA DE CORES GLOBAL (Estilo Nubank/Fintech) ---
COR_FUNDO = "#09090B"
COR_CARD = "#18181B"
COR_DESTAQUE = "#820AD1"
COR_HOVER_DESTAQUE = "#6B08A4"
COR_TEXTO = "#E4E4E7"
COR_TEXTO_SECUNDARIO = "#A1A1AA"
COR_INPUT_BG = "#27272A"
COR_INPUT_HOVER = "#3F3F46"

FONTE_TITULO = ("Segoe UI", 16, "bold")
FONTE_LABEL = ("Segoe UI", 13)


def carregar_config_apis() -> dict:
    if not os.path.exists(ARQUIVO_CONFIG_APIS):
        return {"input": {}, "output": {}, "input_ativas": [], "output_ativas": [], "ordem_inputs": [], "ordem_outputs": []}
    try:
        with open(ARQUIVO_CONFIG_APIS, "r", encoding="utf-8") as f:
            dados = json.load(f)
        dados.setdefault("input", {})
        dados.setdefault("output", {})
        dados.setdefault("input_ativas", [])
        dados.setdefault("output_ativas", [])
        dados.setdefault("ordem_inputs", [])
        dados.setdefault("ordem_outputs", [])
        return dados
    except (json.JSONDecodeError, OSError):
        return {"input": {}, "output": {}, "input_ativas": [], "output_ativas": [], "ordem_inputs": [], "ordem_outputs": []}


def salvar_config_apis(dados: dict) -> None:
    with open(ARQUIVO_CONFIG_APIS, "w", encoding="utf-8") as f:
        json.dump(dados, f, ensure_ascii=False, indent=2)


class JanelaLog(ctk.CTkToplevel):
    def __init__(self, master):
        super().__init__(master)
        self.title("FlyScanner - Log")
        self.geometry("800x500")
        self.protocol("WM_DELETE_WINDOW", self.withdraw)

        topo = ctk.CTkFrame(self)
        topo.pack(fill="x", padx=10, pady=(10, 0))
        ctk.CTkLabel(topo, text="Log do sistema", font=ctk.CTkFont(size=16, weight="bold")).pack(side="left")
        ctk.CTkButton(topo, text="Limpar log", width=100, command=self._limpar).pack(side="right")

        self.caixa_log = ctk.CTkTextbox(self, wrap="word", font=("Consolas", 12))
        self.caixa_log.pack(fill="both", expand=True, padx=10, pady=10)
        self.caixa_log.configure(state="disabled")

        self._fila = log.nova_fila_de_escuta()
        self._popular_log_existente()
        self._checar_fila()

    def _popular_log_existente(self):
        conteudo = log.ler_log_completo()
        if conteudo:
            self.caixa_log.configure(state="normal")
            self.caixa_log.insert("end", conteudo)
            self.caixa_log.see("end")
            self.caixa_log.configure(state="disabled")

    def _limpar(self):
        log.limpar_log()
        self.caixa_log.configure(state="normal")
        self.caixa_log.delete("1.0", "end")
        self.caixa_log.configure(state="disabled")

    def _checar_fila(self):
        try:
            while True:
                linha = self._fila.get_nowait()
                self.caixa_log.configure(state="normal")
                self.caixa_log.insert("end", linha + "\n")
                self.caixa_log.see("end")
                self.caixa_log.configure(state="disabled")
        except queue.Empty:
            pass
        finally:
            self.after(500, self._checar_fila)


class FlyScannerApp(ctk.CTk):
    def __init__(self):
        super().__init__()
        self.title("FlyScanner - Buscar Passagens")
        self.geometry("980x750")

        self.robo = buscador.Robo(intervalo_segundos=60)
        self.config_apis = carregar_config_apis()

        self.modulos_input = apis.listar_apis_input()
        self.modulos_output = apis.listar_apis_output()

        # Garante que novas APIs adicionadas aos arquivos apareçam na ordem
        for ch in self.modulos_input:
            if ch not in self.config_apis["ordem_inputs"]:
                self.config_apis["ordem_inputs"].append(ch)
        for ch in self.modulos_output:
            if ch not in self.config_apis["ordem_outputs"]:
                self.config_apis["ordem_outputs"].append(ch)

        self._entradas_input = {}
        self._checkbox_input = {}
        self._entradas_output = {}
        self._checkbox_output = {}

        self._montar_ui()
        self._janela_log = JanelaLog(self)
        self._janela_log.withdraw()

        log.registrar("Interface iniciada.", nivel="INFO", origem="interface")

    # ------------------------------------------------------------------ UI

    def _montar_ui(self):
        barra_topo = ctk.CTkFrame(self)
        barra_topo.pack(fill="x", padx=10, pady=10)

        ctk.CTkLabel(barra_topo, text="FlyScanner", font=ctk.CTkFont(size=20, weight="bold")).pack(side="left", padx=5)
        ctk.CTkButton(barra_topo, text="Ver Log", width=100, command=self._abrir_janela_log).pack(side="right", padx=5)

        self.botao_robo = ctk.CTkButton(
            barra_topo, text="▶ Rodar Robô", fg_color="#2e7d32", hover_color="#1b5e20",
            width=140, command=self._alternar_robo,
        )
        self.botao_robo.pack(side="right", padx=5)

        self.abas = ctk.CTkTabview(self)
        self.abas.pack(fill="both", expand=True, padx=10, pady=(0, 10))

        self.abas.add("Fila de Inputs")
        self.abas.add("Condições")
        self.abas.add("Retornos")

        self._montar_aba_inputs(self.abas.tab("Fila de Inputs"))
        self._montar_aba_condicoes(self.abas.tab("Condições"))
        self._montar_aba_retorno(self.abas.tab("Retornos"))

    # ---- Aba 1: Inputs (Reativos e Reordenáveis) ------------------------

    def _montar_aba_inputs(self, aba):
        aba.configure(fg_color=COR_FUNDO)
        self.scroll_inputs = ctk.CTkScrollableFrame(aba, fg_color="transparent")
        self.scroll_inputs.pack(fill="both", expand=True, padx=20, pady=10)

        self.container_cards_input = ctk.CTkFrame(self.scroll_inputs, fg_color="transparent")
        self.container_cards_input.pack(fill="x", expand=True)

        btn_salvar = ctk.CTkButton(
            self.scroll_inputs, text="Salvar Fila e Integrações", font=ctk.CTkFont(size=15, weight="bold"),
            fg_color=COR_DESTAQUE, hover_color=COR_HOVER_DESTAQUE, height=50, corner_radius=10,
            command=self._salvar_inputs
        )
        btn_salvar.pack(pady=20, fill="x", padx=100)

        self._renderizar_cards_inputs()

    def _renderizar_cards_inputs(self):
        # Limpa tudo antes de redesenhar
        for widget in self.container_cards_input.winfo_children():
            widget.destroy()

        self._entradas_input.clear()
        self._checkbox_input.clear()

        ativas_salvas = set(self.config_apis.get("input_ativas", []))
        ordem = [ch for ch in self.config_apis["ordem_inputs"] if ch in self.modulos_input]

        if not ordem:
            ctk.CTkLabel(self.container_cards_input, text="Nenhuma API encontrada.", text_color=COR_TEXTO_SECUNDARIO).pack(pady=20)
            return

        for index, chave in enumerate(ordem):
            modulo = self.modulos_input[chave]
            
            card = ctk.CTkFrame(self.container_cards_input, fg_color=COR_CARD, corner_radius=12)
            card.pack(fill="x", pady=(0, 15))
            
            # --- HEADER DO CARD (Reordenação + Toggle) ---
            header = ctk.CTkFrame(card, fg_color="transparent")
            header.pack(fill="x", padx=20, pady=(15, 10))
            
            frame_setas = ctk.CTkFrame(header, fg_color="transparent")
            frame_setas.pack(side="left", padx=(0, 15))
            
            # Botão Subir
            btn_up = ctk.CTkButton(frame_setas, text="▲", width=30, height=20, fg_color=COR_INPUT_BG, hover_color=COR_INPUT_HOVER, text_color=COR_TEXTO_SECUNDARIO)
            btn_up.pack(pady=(0, 2))
            if index > 0:
                btn_up.configure(command=lambda c=chave, d=-1: self._mover_card_input(c, d))
            else:
                btn_up.configure(state="disabled", fg_color="transparent")
                
            # Botão Descer
            btn_down = ctk.CTkButton(frame_setas, text="▼", width=30, height=20, fg_color=COR_INPUT_BG, hover_color=COR_INPUT_HOVER, text_color=COR_TEXTO_SECUNDARIO)
            btn_down.pack()
            if index < len(ordem) - 1:
                btn_down.configure(command=lambda c=chave, d=1: self._mover_card_input(c, d))
            else:
                btn_down.configure(state="disabled", fg_color="transparent")

            var = ctk.BooleanVar(value=(chave in ativas_salvas))
            self._checkbox_input[chave] = var
            
            chk = ctk.CTkSwitch(
                header, text=f"{index + 1}º Fila | {modulo.NOME} [{'Ativa' if var.get() else 'Inativa'}]", 
                variable=var, font=ctk.CTkFont(*FONTE_TITULO), text_color=COR_TEXTO,
                progress_color=COR_DESTAQUE, button_color="#FFFFFF", button_hover_color=COR_TEXTO
            )
            chk.configure(command=lambda v=var, c=chk, n=modulo.NOME, i=index: c.configure(text=f"{i + 1}º Fila | {n} [{'Ativa' if v.get() else 'Inativa'}]"))
            chk.pack(side="left")

            # --- CONTEÚDO DO CARD (Credenciais e Intervalo) ---
            self._entradas_input[chave] = {}
            valores_salvos = self.config_apis["input"].get(chave, {})
            
            conteudo = ctk.CTkFrame(card, fg_color="transparent")
            conteudo.pack(fill="x", padx=20, pady=(0, 15))

            # Campo Fixo: Cooldown (Intervalo)
            linha_tempo = ctk.CTkFrame(conteudo, fg_color="transparent")
            linha_tempo.pack(fill="x", pady=(0, 10))
            ctk.CTkLabel(linha_tempo, text="Repetir busca a cada (Minutos)", text_color=COR_DESTAQUE, font=ctk.CTkFont(*FONTE_LABEL, weight="bold"), width=200, anchor="w").pack(side="left", padx=(0, 10))
            
            ent_tempo = ctk.CTkEntry(linha_tempo, height=40, border_width=1, corner_radius=8, width=120)
            ent_tempo.pack(side="left")
            ent_tempo.insert(0, str(valores_salvos.get("intervalo_minutos", "60")))
            self._entradas_input[chave]["intervalo_minutos"] = ent_tempo

            for campo in getattr(modulo, "CAMPOS_CONFIG", []):
                linha = ctk.CTkFrame(conteudo, fg_color="transparent")
                linha.pack(fill="x", pady=5)
                
                ctk.CTkLabel(linha, text=campo["label"], text_color=COR_TEXTO_SECUNDARIO, font=ctk.CTkFont(*FONTE_LABEL), width=200, anchor="w").pack(side="left", padx=(0, 10))
                
                is_senha = campo.get("tipo") == "senha"
                entrada = ctk.CTkEntry(linha, height=40, border_width=1, corner_radius=8, show="*" if is_senha else "")
                entrada.pack(side="left", fill="x", expand=True)
                
                if campo["chave"] in valores_salvos:
                    entrada.insert(0, valores_salvos[campo["chave"]])
                
                self._entradas_input[chave][campo["chave"]] = entrada
                
                if is_senha:
                    def toggle_senha(e=entrada, b=None):
                        if e.cget("show") == "*":
                            e.configure(show="")
                            b.configure(text="Ocultar")
                        else:
                            e.configure(show="*")
                            b.configure(text="Mostrar")

                    btn_olho = ctk.CTkButton(
                        linha, text="Mostrar", width=70, height=40, fg_color=COR_INPUT_BG, 
                        text_color=COR_TEXTO_SECUNDARIO, hover_color=COR_INPUT_HOVER, corner_radius=8
                    )
                    btn_olho.configure(command=lambda e=entrada, b=btn_olho: toggle_senha(e, b))
                    btn_olho.pack(side="left", padx=(10, 0))

    def _mover_card_input(self, chave, direcao):
        """Salva o estado atual, move o array e redesenha a tela."""
        self._salvar_inputs(silencioso=True)
        
        ordem = self.config_apis["ordem_inputs"]
        idx = ordem.index(chave)
        novo_idx = idx + direcao
        
        # Faz o Swap
        ordem[idx], ordem[novo_idx] = ordem[novo_idx], ordem[idx]
        self._renderizar_cards_inputs()

    def _salvar_inputs(self, silencioso=False):
        for chave, campos in self._entradas_input.items():
            self.config_apis["input"][chave] = {
                campo_chave: widget.get() for campo_chave, widget in campos.items()
            }
            # Converte o intervalo pra int no JSON
            try:
                self.config_apis["input"][chave]["intervalo_minutos"] = int(self.config_apis["input"][chave].get("intervalo_minutos", 60))
            except:
                self.config_apis["input"][chave]["intervalo_minutos"] = 60
        
        ativas = [chave for chave, var in self._checkbox_input.items() if var.get()]
        self.config_apis["input_ativas"] = ativas
        
        # Mantém a ordem definida pela UI
        self.config_apis["ordem_inputs"] = [ch for ch in self.config_apis["ordem_inputs"] if ch in self.modulos_input]
        salvar_config_apis(self.config_apis)
        
        if not silencioso:
            msg_log = f"Fila de Inputs salva. APIs ativas: {len(ativas)}"
            log.registrar_sucesso(msg_log, origem="interface")

    # ---- Aba 2: Condições (Padrão Startup) -----------------------------

    def _montar_aba_condicoes(self, aba):
        aba.configure(fg_color=COR_FUNDO) 
        scroll = ctk.CTkScrollableFrame(aba, fg_color="transparent")
        scroll.pack(fill="both", expand=True, padx=20, pady=10)

        atuais = condicoes_mod.carregar()
        self._campos_condicoes = {}

        # CARD 1: ROTA
        card_rota = ctk.CTkFrame(scroll, fg_color=COR_CARD, corner_radius=12)
        card_rota.pack(fill="x", pady=(0, 15))
        
        ctk.CTkLabel(card_rota, text="✈️ Rota de Voo", font=ctk.CTkFont(*FONTE_TITULO), text_color=COR_TEXTO).pack(anchor="w", padx=20, pady=(15, 10))

        frame_grid_rota = ctk.CTkFrame(card_rota, fg_color="transparent")
        frame_grid_rota.pack(fill="x", padx=20, pady=(0, 15))
        frame_grid_rota.grid_columnconfigure((0, 1), weight=1)

        ctk.CTkLabel(frame_grid_rota, text="Origem", font=ctk.CTkFont(*FONTE_LABEL), text_color=COR_TEXTO_SECUNDARIO).grid(row=0, column=0, sticky="w", pady=(0, 5))
        self._entrada_origem = ctk.CTkEntry(frame_grid_rota, height=40, border_width=1, corner_radius=8, placeholder_text="Ex: GIG, CGH, LIS")
        self._entrada_origem.grid(row=1, column=0, sticky="ew", padx=(0, 10))
        self._entrada_origem.insert(0, str(atuais.get("origem", "")))
        self._entrada_origem.bind("<KeyRelease>", lambda e: self._sugerir_multiplos_aeroportos(e, self._entrada_origem))
        self._campos_condicoes["origem"] = self._entrada_origem

        ctk.CTkLabel(frame_grid_rota, text="Destino", font=ctk.CTkFont(*FONTE_LABEL), text_color=COR_TEXTO_SECUNDARIO).grid(row=0, column=1, sticky="w", pady=(0, 5))
        self._entrada_destino = ctk.CTkEntry(frame_grid_rota, height=40, border_width=1, corner_radius=8, placeholder_text="Ex: JFK, MCO")
        self._entrada_destino.grid(row=1, column=1, sticky="ew")
        self._entrada_destino.insert(0, str(atuais.get("destino", "")))
        self._entrada_destino.bind("<KeyRelease>", lambda e: self._sugerir_multiplos_aeroportos(e, self._entrada_destino))
        self._campos_condicoes["destino"] = self._entrada_destino

        # CARD 2: DATAS E FLEXIBILIDADE
        card_datas = ctk.CTkFrame(scroll, fg_color=COR_CARD, corner_radius=12)
        card_datas.pack(fill="x", pady=15)
        
        ctk.CTkLabel(card_datas, text="📅 Planejamento de Tempo", font=ctk.CTkFont(*FONTE_TITULO), text_color=COR_TEXTO).pack(anchor="w", padx=20, pady=(15, 10))

        frame_grid_datas = ctk.CTkFrame(card_datas, fg_color="transparent")
        frame_grid_datas.pack(fill="x", padx=20, pady=(0, 15))
        frame_grid_datas.grid_columnconfigure((0, 1, 2), weight=1)

        ctk.CTkLabel(frame_grid_datas, text="Modalidade", font=ctk.CTkFont(*FONTE_LABEL), text_color=COR_TEXTO_SECUNDARIO).grid(row=0, column=0, sticky="w", pady=(0, 5))
        self.var_tipo_viagem = ctk.StringVar(value=atuais.get("tipo_viagem", "ida_volta"))
        btn_tipo = ctk.CTkSegmentedButton(
            frame_grid_datas, values=["ida", "ida_volta"], variable=self.var_tipo_viagem,
            command=self._alternar_datas, selected_color=COR_DESTAQUE, selected_hover_color=COR_HOVER_DESTAQUE, height=35
        )
        btn_tipo.grid(row=1, column=0, sticky="ew", padx=(0, 10))
        self._campos_condicoes["tipo_viagem"] = btn_tipo

        ctk.CTkLabel(frame_grid_datas, text="Data de Ida (DD/MM/AAAA)", font=ctk.CTkFont(*FONTE_LABEL), text_color=COR_TEXTO_SECUNDARIO).grid(row=0, column=1, sticky="w", pady=(0, 5))
        self.entrada_ida = ctk.CTkEntry(frame_grid_datas, height=40, border_width=1, corner_radius=8, placeholder_text="Ex: 15/08/2026")
        self.entrada_ida.grid(row=1, column=1, sticky="ew", padx=(0, 10))
        self.entrada_ida.insert(0, atuais.get("data_ida", ""))
        self.entrada_ida.bind("<KeyRelease>", lambda e: self._aplicar_mascara_data(e, self.entrada_ida))

        ctk.CTkLabel(frame_grid_datas, text="Data de Volta (DD/MM/AAAA)", font=ctk.CTkFont(*FONTE_LABEL), text_color=COR_TEXTO_SECUNDARIO).grid(row=0, column=2, sticky="w", pady=(0, 5))
        self.entrada_volta = ctk.CTkEntry(frame_grid_datas, height=40, border_width=1, corner_radius=8, placeholder_text="Ex: 25/08/2026")
        self.entrada_volta.grid(row=1, column=2, sticky="ew")
        self.entrada_volta.insert(0, atuais.get("data_volta", ""))
        self.entrada_volta.bind("<KeyRelease>", lambda e: self._aplicar_mascara_data(e, self.entrada_volta))

        # CARD 3: ORÇAMENTO
        card_financas = ctk.CTkFrame(scroll, fg_color=COR_CARD, corner_radius=12)
        card_financas.pack(fill="x", pady=15)
        
        ctk.CTkLabel(card_financas, text="💰 Inteligência Financeira", font=ctk.CTkFont(*FONTE_TITULO), text_color=COR_TEXTO).pack(anchor="w", padx=20, pady=(15, 10))

        frame_grid_financas = ctk.CTkFrame(card_financas, fg_color="transparent")
        frame_grid_financas.pack(fill="x", padx=20, pady=(0, 20))
        frame_grid_financas.grid_columnconfigure((0, 1, 2), weight=1)

        ctk.CTkLabel(frame_grid_financas, text="Moeda Base", font=ctk.CTkFont(*FONTE_LABEL), text_color=COR_TEXTO_SECUNDARIO).grid(row=0, column=0, sticky="w", pady=(0, 5))
        self.var_moeda = ctk.StringVar(value=atuais.get("moeda", "BRL - Real"))
        self.combo_moeda = ctk.CTkOptionMenu(
            frame_grid_financas, values=["BRL - Real", "USD - Dólar", "EUR - Euro", "GBP - Libra"], 
            variable=self.var_moeda, command=self._atualizar_sifrao, height=40, 
            fg_color=COR_INPUT_BG, button_color=COR_INPUT_HOVER, button_hover_color=COR_DESTAQUE
        )
        self.combo_moeda.grid(row=1, column=0, sticky="ew", padx=(0, 10))
        self._campos_condicoes["moeda"] = self.combo_moeda

        ctk.CTkLabel(frame_grid_financas, text="Máximo Teto", font=ctk.CTkFont(*FONTE_LABEL), text_color=COR_TEXTO_SECUNDARIO).grid(row=0, column=1, sticky="w", pady=(0, 5))
        self.entrada_vmax = ctk.CTkEntry(frame_grid_financas, height=40, border_width=1, corner_radius=8, font=ctk.CTkFont(*FONTE_LABEL))
        self.entrada_vmax.grid(row=1, column=1, sticky="ew")
        self.entrada_vmax.insert(0, self._formatar_para_moeda(atuais.get("valor_maximo", ""), atuais.get("moeda", "BRL")))
        self.entrada_vmax.bind("<FocusOut>", lambda e: self._aplicar_mascara_moeda(self.entrada_vmax))
        
        self.var_menor_preco = ctk.BooleanVar(value=str(atuais.get("apenas_menor_preco", "false")).lower() == "true")
        chk_historico = ctk.CTkSwitch(
            card_financas, text="🔥 Apenas Menor Preço Histórico", variable=self.var_menor_preco,
            font=ctk.CTkFont(*FONTE_TITULO), text_color=COR_DESTAQUE, progress_color=COR_DESTAQUE
        )
        chk_historico.pack(padx=20, pady=(0, 20), anchor="w")

        btn_salvar = ctk.CTkButton(
            scroll, text="Salvar Estratégia de Busca", font=ctk.CTkFont(size=15, weight="bold"),
            fg_color=COR_DESTAQUE, hover_color=COR_HOVER_DESTAQUE, height=50, corner_radius=10,
            command=self._salvar_condicoes
        )
        btn_salvar.pack(pady=20, fill="x", padx=100)

        self._alternar_datas(self.var_tipo_viagem.get())

    # --- Funções Auxiliares Aba 2 ---
    def _sugerir_multiplos_aeroportos(self, event, widget):
        if event.keysym in ("BackSpace", "Shift_L", "Shift_R", "Control_L"): return
        texto_completo = widget.get().upper()
        termos = [t.strip() for t in texto_completo.split(",")]
        termo_atual = termos[-1]
        if len(termo_atual) < 3: return
        db_aeroportos = {"RIO": "GIG", "SAO": "GRU", "NOV": "JFK", "LIS": "LIS", "PAR": "CDG"}
        for chave, codigo in db_aeroportos.items():
            if termo_atual.startswith(chave):
                termos[-1] = codigo
                novo_texto = ", ".join(termos) + ", "
                widget.delete(0, "end")
                widget.insert(0, novo_texto)
                widget.icursor("end")
                break

    def _aplicar_mascara_data(self, event, widget):
        if event.keysym in ("BackSpace", "Delete", "Left", "Right"): return
        texto = re.sub(r"[^\d]", "", widget.get())
        if len(texto) > 2: texto = texto[:2] + "/" + texto[2:]
        if len(texto) > 5: texto = texto[:5] + "/" + texto[5:9]
        widget.delete(0, "end")
        widget.insert(0, texto[:10])

    def _alternar_datas(self, valor_selecionado):
        if valor_selecionado == "ida":
            self.entrada_volta.configure(state="disabled", fg_color=COR_INPUT_BG, text_color="#52525B")
        else:
            self.entrada_volta.configure(state="normal", fg_color=["#F9F9FA", "#343638"], text_color=["gray10", "#DCE4EE"])

    def _atualizar_sifrao(self, valor_selecionado):
        self._aplicar_mascara_moeda(self.entrada_vmax, valor_selecionado)

    def _obter_sifrao(self, moeda_str):
        mapa = {"BRL": "R$ ", "USD": "$ ", "EUR": "€ ", "GBP": "£ "}
        return mapa.get(moeda_str[:3], "$ ")

    def _formatar_para_moeda(self, valor_bruto, moeda_str):
        if not valor_bruto: return ""
        try:
            valor_float = float(str(valor_bruto).replace(",", ".").replace(self._obter_sifrao(moeda_str), "").strip())
            sifrao = self._obter_sifrao(moeda_str)
            return f"{sifrao}{valor_float:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")
        except ValueError:
            return str(valor_bruto)

    def _aplicar_mascara_moeda(self, widget, moeda_forca=None):
        moeda_str = moeda_forca if moeda_forca else self.var_moeda.get()
        texto_limpo = re.sub(r"[^\d,.-]", "", widget.get())
        texto_formatado = self._formatar_para_moeda(texto_limpo, moeda_str)
        widget.delete(0, "end")
        widget.insert(0, texto_formatado)

    def _limpar_moeda_para_salvar(self, texto_formatado):
        if not texto_formatado: return ""
        limpo = re.sub(r"[^\d,.-]", "", texto_formatado)
        return limpo.replace(".", "").replace(",", ".")

    def _salvar_condicoes(self):
        novas = {
            "origem": self._campos_condicoes["origem"].get(),
            "destino": self._campos_condicoes["destino"].get(),
            "tipo_viagem": self.var_tipo_viagem.get(),
            "data_ida": self.entrada_ida.get(),
            "data_volta": self.entrada_volta.get() if self.var_tipo_viagem.get() == "ida_volta" else "",
            "valor_maximo": self._limpar_moeda_para_salvar(self.entrada_vmax.get()),
            "moeda": self.var_moeda.get()[:3],
            "apenas_menor_preco": self.var_menor_preco.get()
        }
        condicoes_mod.salvar(novas)
        log.registrar_sucesso("Estratégia de busca salva.", origem="interface")


    # ---- Aba 3: Retorno (UX Premium Reordenável) ------------------------

    def _montar_aba_retorno(self, aba):
        aba.configure(fg_color=COR_FUNDO)
        self.scroll_outputs = ctk.CTkScrollableFrame(aba, fg_color="transparent")
        self.scroll_outputs.pack(fill="both", expand=True, padx=20, pady=10)

        self.container_cards_output = ctk.CTkFrame(self.scroll_outputs, fg_color="transparent")
        self.container_cards_output.pack(fill="x", expand=True)

        btn_salvar = ctk.CTkButton(
            self.scroll_outputs, text="Salvar Destinos de Retorno", font=ctk.CTkFont(size=15, weight="bold"),
            fg_color=COR_DESTAQUE, hover_color=COR_HOVER_DESTAQUE, height=50, corner_radius=10,
            command=self._salvar_retorno
        )
        btn_salvar.pack(pady=20, fill="x", padx=100)

        self._renderizar_cards_outputs()

    def _renderizar_cards_outputs(self):
        for widget in self.container_cards_output.winfo_children():
            widget.destroy()

        self._entradas_output.clear()
        self._checkbox_output.clear()

        ativas_salvas = set(self.config_apis.get("output_ativas", []))
        ordem = [ch for ch in self.config_apis["ordem_outputs"] if ch in self.modulos_output]

        if not ordem:
            ctk.CTkLabel(self.container_cards_output, text="Nenhuma API de saída encontrada.", text_color=COR_TEXTO_SECUNDARIO).pack(pady=20)
            return

        for index, chave in enumerate(ordem):
            modulo = self.modulos_output[chave]
            
            card = ctk.CTkFrame(self.container_cards_output, fg_color=COR_CARD, corner_radius=12)
            card.pack(fill="x", pady=(0, 15))
            
            # --- HEADER ---
            header = ctk.CTkFrame(card, fg_color="transparent")
            header.pack(fill="x", padx=20, pady=(15, 10))
            
            frame_setas = ctk.CTkFrame(header, fg_color="transparent")
            frame_setas.pack(side="left", padx=(0, 15))
            
            btn_up = ctk.CTkButton(frame_setas, text="▲", width=30, height=20, fg_color=COR_INPUT_BG, hover_color=COR_INPUT_HOVER, text_color=COR_TEXTO_SECUNDARIO)
            btn_up.pack(pady=(0, 2))
            if index > 0: btn_up.configure(command=lambda c=chave, d=-1: self._mover_card_output(c, d))
            else: btn_up.configure(state="disabled", fg_color="transparent")
                
            btn_down = ctk.CTkButton(frame_setas, text="▼", width=30, height=20, fg_color=COR_INPUT_BG, hover_color=COR_INPUT_HOVER, text_color=COR_TEXTO_SECUNDARIO)
            btn_down.pack()
            if index < len(ordem) - 1: btn_down.configure(command=lambda c=chave, d=1: self._mover_card_output(c, d))
            else: btn_down.configure(state="disabled", fg_color="transparent")

            var = ctk.BooleanVar(value=(chave in ativas_salvas))
            self._checkbox_output[chave] = var
            
            chk = ctk.CTkSwitch(
                header, text=f"{modulo.NOME} [{'Ativa' if var.get() else 'Inativa'}]", 
                variable=var, font=ctk.CTkFont(*FONTE_TITULO), text_color=COR_TEXTO,
                progress_color=COR_DESTAQUE, button_color="#FFFFFF"
            )
            chk.configure(command=lambda v=var, c=chk, n=modulo.NOME: c.configure(text=f"{n} [{'Ativa' if v.get() else 'Inativa'}]"))
            chk.pack(side="left")

            # --- CONTEÚDO ---
            self._entradas_output[chave] = {}
            valores_salvos = self.config_apis["output"].get(chave, {})
            
            conteudo = ctk.CTkFrame(card, fg_color="transparent")
            conteudo.pack(fill="x", padx=20, pady=(0, 15))

            if not getattr(modulo, "CAMPOS_CONFIG", []):
                ctk.CTkLabel(conteudo, text="Pronto para uso (Sem configuração adicional).", text_color=COR_TEXTO_SECUNDARIO, font=ctk.CTkFont(*FONTE_LABEL)).pack(anchor="w", pady=(0, 5))
                continue

            for campo in modulo.CAMPOS_CONFIG:
                linha = ctk.CTkFrame(conteudo, fg_color="transparent")
                linha.pack(fill="x", pady=5)
                
                ctk.CTkLabel(linha, text=campo["label"], text_color=COR_TEXTO_SECUNDARIO, font=ctk.CTkFont(*FONTE_LABEL), width=200, anchor="w").pack(side="left", padx=(0, 10))
                
                is_senha = campo.get("tipo") == "senha"
                entrada = ctk.CTkEntry(linha, height=40, border_width=1, corner_radius=8, show="*" if is_senha else "")
                entrada.pack(side="left", fill="x", expand=True)
                
                if campo["chave"] in valores_salvos:
                    entrada.insert(0, valores_salvos[campo["chave"]])
                
                self._entradas_output[chave][campo["chave"]] = entrada

    def _mover_card_output(self, chave, direcao):
        self._salvar_retorno(silencioso=True)
        ordem = self.config_apis["ordem_outputs"]
        idx = ordem.index(chave)
        novo_idx = idx + direcao
        ordem[idx], ordem[novo_idx] = ordem[novo_idx], ordem[idx]
        self._renderizar_cards_outputs()

    def _salvar_retorno(self, silencioso=False):
        for chave, campos in self._entradas_output.items():
            self.config_apis["output"][chave] = {campo_chave: widget.get() for campo_chave, widget in campos.items()}
            
        ativas = [chave for chave, var in self._checkbox_output.items() if var.get()]
        self.config_apis["output_ativas"] = ativas
        self.config_apis["ordem_outputs"] = [ch for ch in self.config_apis["ordem_outputs"] if ch in self.modulos_output]
        
        salvar_config_apis(self.config_apis)
        
        if not silencioso:
            log.registrar_sucesso(f"Saídas salvas. Ativas: {len(ativas)}", origem="interface")

    # ---- Robô -------------------------------------------------------

    def _alternar_robo(self):
        if self.robo.rodando:
            self.robo.stop()
            self.botao_robo.configure(text="▶ Rodar Robô", fg_color="#2e7d32", hover_color="#1b5e20")
            return

        self._salvar_inputs(silencioso=True)
        self._salvar_condicoes()
        self._salvar_retorno(silencioso=True)

        # Respeita a ordem definida na UI
        apis_input_selecionadas = {}
        for chave in self.config_apis.get("ordem_inputs", []):
            if chave in self.config_apis.get("input_ativas", []):
                apis_input_selecionadas[chave] = self.config_apis["input"].get(chave, {})
            
        apis_output_selecionadas = {}
        for chave in self.config_apis.get("ordem_outputs", []):
            if chave in self.config_apis.get("output_ativas", []):
                apis_output_selecionadas[chave] = self.config_apis["output"].get(chave, {})

        if not apis_input_selecionadas:
            log.registrar_erro("Nenhuma Fila de Input ATIVA.", origem="interface")
            return
        if not apis_output_selecionadas:
            log.registrar_erro("Nenhum Retorno ATIVO.", origem="interface")
            return

        self.robo.configurar(apis_input_selecionadas, apis_output_selecionadas)
        self.robo.start()
        self.botao_robo.configure(text="■ Parar Robô", fg_color="#c62828", hover_color="#8e0000")

    def _abrir_janela_log(self):
        self._janela_log.deiconify()
        self._janela_log.lift()


if __name__ == "__main__":
    app = FlyScannerApp()
    app.mainloop()