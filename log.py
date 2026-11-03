"""
log.py
------
Sistema central de logs do FlyScanner.

Qualquer parte do sistema (interface, buscador, apis_input, apis_output)
manda mensagens pra cá através da função `registrar()`. O log.py guarda
tudo em arquivo (log/flyscanner.log) e também distribui as mensagens pra
quem estiver "ouvindo" (a janela de Log da interface), via uma fila
thread-safe (queue.Queue).

Não depende do customtkinter, só de bibliotecas padrão, pra poder ser
chamado de qualquer script (inclusive os que rodam em thread separada).
"""

import os
import queue
import threading
from datetime import datetime

_LOCK = threading.Lock()
_LISTENERS = []  # lista de queue.Queue que recebem cada nova linha de log

LOG_DIR = os.path.join(os.path.dirname(os.path.abspath(__file__)), "log")
LOG_FILE = os.path.join(LOG_DIR, "flyscanner.log")

NIVEIS = ("INFO", "SUCESSO", "AVISO", "ERRO")


def _garantir_pasta():
    if not os.path.exists(LOG_DIR):
        os.makedirs(LOG_DIR, exist_ok=True)


def registrar(mensagem: str, nivel: str = "INFO", origem: str = "sistema"):
    """
    Registra uma mensagem de log.

    nivel: INFO, SUCESSO, AVISO ou ERRO
    origem: de onde veio (ex: 'google_flight', 'terminal', 'buscador', 'interface')
    """
    nivel = nivel.upper() if nivel.upper() in NIVEIS else "INFO"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    linha = f"[{timestamp}] [{nivel}] [{origem}] {mensagem}"

    with _LOCK:
        _garantir_pasta()
        try:
            with open(LOG_FILE, "a", encoding="utf-8") as f:
                f.write(linha + "\n")
        except OSError:
            pass  # se não conseguir gravar em disco, ao menos os listeners recebem

        for fila in list(_LISTENERS):
            try:
                fila.put_nowait(linha)
            except Exception:
                pass

    return linha


def registrar_erro(mensagem: str, origem: str = "sistema"):
    return registrar(mensagem, nivel="ERRO", origem=origem)


def registrar_sucesso(mensagem: str, origem: str = "sistema"):
    return registrar(mensagem, nivel="SUCESSO", origem=origem)


def registrar_aviso(mensagem: str, origem: str = "sistema"):
    return registrar(mensagem, nivel="AVISO", origem=origem)


def nova_fila_de_escuta() -> queue.Queue:
    """
    A janela de Log da interface chama isso pra ganhar uma fila própria.
    Toda nova mensagem registrada também cai nessa fila, e a interface
    fica dando `fila.get_nowait()` periodicamente (via `after()` do Tkinter)
    pra jogar na tela sem travar a UI.
    """
    fila = queue.Queue()
    _LISTENERS.append(fila)
    return fila


def ler_log_completo() -> str:
    """Lê o arquivo de log inteiro (útil pra popular a janela ao abrir)."""
    _garantir_pasta()
    if not os.path.exists(LOG_FILE):
        return ""
    with open(LOG_FILE, "r", encoding="utf-8") as f:
        return f.read()


def limpar_log():
    _garantir_pasta()
    with _LOCK:
        with open(LOG_FILE, "w", encoding="utf-8") as f:
            f.write("")
    registrar("Log limpo pelo usuário.", nivel="INFO", origem="log")
