"""
apis_input/aviasales.py
-----------------------
Integração com a API da Aviasales (via Travelpayouts).
Suporta múltiplos aeroportos gerando requisições combinadas.
"""
import requests
import log

NOME = "Aviasales"

CAMPOS_CONFIG = [
    {"chave": "token", "label": "Token da API (Travelpayouts)", "tipo": "senha"},
]

def buscar(config: dict, condicoes: dict) -> list:
    token = config.get("token")
    if not token:
        log.registrar_erro("Token da Aviasales não configurado.", origem=NOME)
        return []

    # Separa os aeroportos digitados ou cria lista com string vazia para rodar busca global
    origens_raw = condicoes.get("origem", "").strip()
    destinos_raw = condicoes.get("destino", "").strip()

    # Se estiver vazio, a lista recebe [""] para o loop acontecer. Se tiver, fatia as vírgulas.
    origens = [o.strip()[:3].upper() for o in origens_raw.split(",")] if origens_raw else [""]
    destinos = [d.strip()[:3].upper() for d in destinos_raw.split(",")] if destinos_raw else [""]
    moeda = condicoes.get("moeda", "BRL").upper()
    
    url = "https://api.travelpayouts.com/v1/prices/cheap"
    voos_totais = []

    # Faz uma varredura para cada combinação
    for origem in origens:
        for destino in destinos:
            params = {
                "token": token,
                "currency": moeda.lower()
            }
            # Só envia o parâmetro para a API se ele existir
            if origem: 
                params["origin"] = origem
            if destino: 
                params["destination"] = destino

            try:
                resp = requests.get(url, params=params)
                resp.raise_for_status()
                dados = resp.json()
                
                if dados.get("success"):
                    rotas = dados.get("data", {}).get(destino, {})
                    
                    for id_voo, voo in rotas.items():
                        data_ida_api = voo.get("departure_at", "")[:10]
                        data_link = data_ida_api.replace('-', '')[4:] 
                        link_checkout = f"https://www.aviasales.com/search/{origem}{data_link}{destino}1"
                        
                        voos_totais.append({
                            "origem": origem,
                            "destino": destino,
                            "tipo_viagem": "ida_volta" if voo.get("return_at") else "ida",
                            "data_ida": data_ida_api,
                            "data_volta": voo.get("return_at", "")[:10] if voo.get("return_at") else "",
                            "valor": float(voo.get("price", 0)),
                            "moeda": moeda,
                            "companhia": voo.get("airline", ""),
                            "link": link_checkout,
                            "fonte": NOME
                        })
            except requests.exceptions.RequestException as e:
                # Registra o erro específico daquela rota, mas continua buscando as outras
                log.registrar_aviso(f"Rota {origem}-{destino} falhou na Aviasales: {e}", origem=NOME)

    return voos_totais