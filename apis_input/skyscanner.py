"""
apis_input/skyscanner.py
--------------------------
Stub (esqueleto) para uma futura integração com a API do Skyscanner
(ex: via RapidAPI). Siga o mesmo contrato de google_flight.py.

Enquanto não for implementado de verdade, `buscar()` retorna lista
vazia e avisa no log que ainda não está pronto.
"""

NOME = "Skyscanner"

CAMPOS_CONFIG = [
    {"chave": "api_key", "label": "Chave da API (RapidAPI)", "tipo": "senha"},
    {"chave": "host", "label": "API Host", "tipo": "texto"},
]


def buscar(config: dict, condicoes: dict) -> list:
    # TODO: implementar chamada real à API do Skyscanner.
    # Deve retornar lista de dicts no mesmo formato usado em google_flight.py:
    # {"origem", "destino", "tipo_viagem", "data_ida", "data_volta",
    #  "valor", "moeda", "companhia", "link", "fonte"}
    return []
