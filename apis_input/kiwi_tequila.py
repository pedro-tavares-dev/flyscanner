"""
apis_input/kiwi_tequila.py
--------------------------
Integração com a API gratuita do Kiwi.com (Tequila).
Retorna links diretos para compra.
"""
import requests
import log

NOME = "Kiwi Tequila"

CAMPOS_CONFIG = [
    {"chave": "api_key", "label": "Chave da API (Tequila)", "tipo": "senha"},
]

def buscar(config: dict, condicoes: dict) -> list:
    api_key = config.get("api_key")
    if not api_key:
        log.registrar_erro("API Key do Kiwi não configurada.", origem=NOME)
        return []

    # Fallback estratégico para testes (ex: rotas de expansão global)
    origem = condicoes.get("origem", "GRU")
    destino = condicoes.get("destino", "JFK")
    data_ida = condicoes.get("data_ida", "10/12/2026") # Formato dd/mm/yyyy esperado pela Kiwi

    url = "https://api.tequila.kiwi.com/v2/search"
    headers = {"apikey": api_key}
    params = {
        "fly_from": origem,
        "fly_to": destino,
        "date_from": data_ida,
        "date_to": data_ida,
        "curr": "USD", # Padrão global
        "limit": 10
    }

    try:
        resp = requests.get(url, headers=headers, params=params)
        resp.raise_for_status()
        dados = resp.json()

        voos = []
        for voo in dados.get("data", []):
            voos.append({
                "origem": voo.get("flyFrom"),
                "destino": voo.get("flyTo"),
                "tipo_viagem": "ida",
                "data_ida": voo.get("local_departure"),
                "data_volta": None,
                "valor": voo.get("price"),
                "moeda": "USD",
                "companhia": ",".join(voo.get("airlines", [])),
                "link": voo.get("deep_link"), # O bot já entrega o link de checkout
                "fonte": NOME
            })
        return voos
    except Exception as e:
        log.registrar_erro(f"Falha na requisição: {e}", origem=NOME)
        return []