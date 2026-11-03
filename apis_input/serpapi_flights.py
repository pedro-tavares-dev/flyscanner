"""
apis_input/serpapi_flights.py
-----------------------------
Integração com SerpApi (Google Flights em tempo real).
Suporta múltiplas origens/destinos e converte datas automaticamente.
"""
import requests
import log

NOME = "Google Flights (SerpApi)"

CAMPOS_CONFIG = [
    {"chave": "api_key", "label": "Chave da API (SerpApi)", "tipo": "senha"},
]

def _formatar_data(data_br):
    """Converte DD/MM/AAAA para YYYY-MM-DD exigido pela API."""
    if not data_br: return ""
    partes = data_br.split("/")
    if len(partes) == 3: 
        return f"{partes[2]}-{partes[1]}-{partes[0]}"
    return data_br

def buscar(config: dict, condicoes: dict) -> list:
    # O .strip() de segurança que implementamos antes
    api_key = config.get("api_key", "").strip()
    if not api_key:
        log.registrar_erro("API Key do SerpApi não configurada.", origem=NOME)
        return []

    # Separa os aeroportos ou usa padrões de segurança para evitar loops infinitos
    origens_raw = condicoes.get("origem", "").strip()
    destinos_raw = condicoes.get("destino", "").strip()
    origens = [o.strip()[:3].upper() for o in origens_raw.split(",")] if origens_raw else ["GRU"]
    destinos = [d.strip()[:3].upper() for d in destinos_raw.split(",")] if destinos_raw else ["JFK"]
    
    data_ida = _formatar_data(condicoes.get("data_ida", ""))
    data_volta = _formatar_data(condicoes.get("data_volta", ""))
    tipo_viagem = condicoes.get("tipo_viagem", "ida")

    if not data_ida:
        log.registrar_erro("SerpApi exige que a data de ida seja preenchida nas condições.", origem=NOME)
        return []

    voos_totais = []
    url = "https://serpapi.com/search.json"

    for origem in origens:
        for destino in destinos:
            if not origem or not destino: continue
            
            params = {
                "engine": "google_flights",
                "departure_id": origem,
                "arrival_id": destino,
                "outbound_date": data_ida,
                "currency": condicoes.get("moeda", "BRL")[:3].upper(),
                "hl": "pt-br",
                "api_key": api_key
            }
            
            if tipo_viagem == "ida_volta" and data_volta:
                params["return_date"] = data_volta
                params["type"] = "1" # 1 = Ida e Volta no SerpApi
            else:
                params["type"] = "2" # 2 = Apenas Ida

            try:
                resp = requests.get(url, params=params)
                resp.raise_for_status()
                dados = resp.json()
                
                # Gera a query correta em inglês para a URL do Google Flights (otimizado fora do loop inferior)
                if tipo_viagem == "ida":
                    query_google = f"One way flights to {destino} from {origem} on {data_ida}"
                else:
                    query_google = f"Flights to {destino} from {origem} on {data_ida} return on {data_volta}"
                
                # Substitui os espaços por %20 para a URL não quebrar
                query_formatada = query_google.replace(" ", "%20")

                # A SerpApi divide os voos em "melhores" e "outros"
                lista_voos = dados.get("best_flights", []) + dados.get("other_flights", [])
                
                for voo in lista_voos:
                    preco = voo.get("price", 0)
                    if preco == 0: continue
                    
                    flights_arr = voo.get("flights", [{}])
                    companhia = flights_arr[0].get("airline", "Múltiplas") if flights_arr else "N/A"
                    
                    voos_totais.append({
                        "origem": origem,
                        "destino": destino,
                        "tipo_viagem": tipo_viagem,
                        "data_ida": condicoes.get("data_ida"),
                        "data_volta": condicoes.get("data_volta") if tipo_viagem == "ida_volta" else "",
                        "valor": float(preco),
                        "moeda": params["currency"],
                        "companhia": companhia,
                        "link": f"https://www.google.com/travel/flights?q={query_formatada}",
                        "fonte": NOME
                    })
            except Exception as e:
                log.registrar_aviso(f"Rota {origem}-{destino} falhou no SerpApi: {e}", origem=NOME)

    return voos_totais