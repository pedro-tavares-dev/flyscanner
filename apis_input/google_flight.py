"""
apis_input/google_flight.py
----------------------------
Stub limpo para integração futura do Google Flights.
"""
NOME = "Google Flights"

CAMPOS_CONFIG = [
    {"chave": "api_key", "label": "Chave da API", "tipo": "senha"},
]

def buscar(config: dict, condicoes: dict) -> list:
    # TODO: Implementar scraper real ou chamada via provedor externo.
    return []