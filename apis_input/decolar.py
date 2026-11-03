"""
apis_input/decolar.py
-----------------------
Stub (esqueleto) para uma futura integração com Decolar/Despegar.
Siga o mesmo contrato de google_flight.py.
"""

NOME = "Decolar"

CAMPOS_CONFIG = [
    {"chave": "api_key", "label": "Chave da API", "tipo": "senha"},
    {"chave": "afiliado_id", "label": "ID de Afiliado", "tipo": "texto"},
]


def buscar(config: dict, condicoes: dict) -> list:
    # TODO: implementar chamada real à API/scraper da Decolar.
    return []
