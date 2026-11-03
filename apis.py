"""
apis.py
-------
Ponte entre a interface e as pastas apis_input/ e apis_output/.

Cada arquivo .py dentro de apis_input/ ou apis_output/ é carregado
dinamicamente aqui. Pra um script novo aparecer na interface, basta
jogar o arquivo na pasta certa e seguir o "contrato" abaixo — não
precisa mexer em mais nada.

CONTRATO DE UMA API DE ENTRADA (apis_input/*.py)
--------------------------------------------------
NOME = "Google Flights"                # nome amigável, mostrado na interface
CAMPOS_CONFIG = [                      # campos que a interface vai desenhar
    {"chave": "api_key", "label": "Chave da API", "tipo": "senha"},
    {"chave": "regiao", "label": "Região", "tipo": "texto"},
]

def buscar(config: dict, condicoes: dict) -> list[dict]:
    '''Retorna uma lista de voos (dicts), já brutos, sem filtrar.
    O buscador.py aplica condicoes.passagem_atende() em cada um.'''
    ...

CONTRATO DE UMA API DE SAÍDA (apis_output/*.py)
--------------------------------------------------
NOME = "Terminal"
CAMPOS_CONFIG = [...]                  # igual acima, pode ser [] se não precisa config

def enviar(voo: dict, config: dict, log_callback=None) -> None:
    '''Recebe um voo que já passou pelas condições e entrega no destino.'''
    ...

Tipos de campo suportados em CAMPOS_CONFIG: "texto", "senha", "numero".
"""

import importlib.util
import os
import sys

import log

PASTA_INPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "apis_input")
PASTA_OUTPUT = os.path.join(os.path.dirname(os.path.abspath(__file__)), "apis_output")


def _carregar_modulos(pasta: str) -> dict:
    """
    Varre a pasta, importa cada .py como módulo e retorna um dict
    {nome_do_arquivo_sem_extensao: modulo}.
    Ignora arquivos que não sejam .py, comecem com "_" ou dêem erro ao importar
    (o erro vai pro log em vez de derrubar a interface).
    """
    modulos = {}
    if not os.path.isdir(pasta):
        return modulos

    for nome_arquivo in sorted(os.listdir(pasta)):
        if not nome_arquivo.endswith(".py") or nome_arquivo.startswith("_"):
            continue

        nome_modulo = nome_arquivo[:-3]
        caminho = os.path.join(pasta, nome_arquivo)

        try:
            spec = importlib.util.spec_from_file_location(nome_modulo, caminho)
            modulo = importlib.util.module_from_spec(spec)
            sys.modules[spec.name] = modulo
            spec.loader.exec_module(modulo)

            if not hasattr(modulo, "NOME"):
                modulo.NOME = nome_modulo.replace("_", " ").title()
            if not hasattr(modulo, "CAMPOS_CONFIG"):
                modulo.CAMPOS_CONFIG = []

            modulos[nome_modulo] = modulo
            log.registrar(f"Módulo carregado: {nome_arquivo}", nivel="INFO", origem="apis")
        except Exception as exc:
            log.registrar_erro(f"Falha ao carregar {nome_arquivo}: {exc}", origem="apis")

    return modulos


def listar_apis_input() -> dict:
    """Retorna {chave: modulo} de tudo que está em apis_input/."""
    return _carregar_modulos(PASTA_INPUT)


def listar_apis_output() -> dict:
    """Retorna {chave: modulo} de tudo que está em apis_output/."""
    return _carregar_modulos(PASTA_OUTPUT)


def buscar_em(modulo, config: dict, condicoes: dict) -> list:
    """Chama modulo.buscar() com segurança, logando qualquer erro."""
    try:
        if not hasattr(modulo, "buscar"):
            log.registrar_erro(f"{modulo.NOME} não implementa buscar()", origem="apis")
            return []
        return modulo.buscar(config or {}, condicoes or {}) or []
    except Exception as exc:
        log.registrar_erro(f"Erro consultando {modulo.NOME}: {exc}", origem=getattr(modulo, "NOME", "apis"))
        return []


def enviar_para(modulo, voo: dict, config: dict) -> None:
    """Chama modulo.enviar() com segurança, logando qualquer erro."""
    try:
        if not hasattr(modulo, "enviar"):
            log.registrar_erro(f"{modulo.NOME} não implementa enviar()", origem="apis")
            return
        modulo.enviar(voo, config or {}, log_callback=log.registrar)
    except Exception as exc:
        log.registrar_erro(f"Erro enviando via {modulo.NOME}: {exc}", origem=getattr(modulo, "NOME", "apis"))
