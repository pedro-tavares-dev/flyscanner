"""
apis_output/whatsapp.py
-------------------------
Envia as passagens encontradas via WhatsApp usando a Evolution API
(https://github.com/EvolutionAPI/evolution-api).

Fluxo (igual ao markdown_export.py):
1. Formata os dados do voo em um texto bonito (com emojis e a sintaxe de
   estilo do WhatsApp: *negrito*, _itálico_ etc).
2. Monta o payload esperado pelo endpoint de envio de texto da Evolution API.
3. Faz o POST para a instância configurada.

Endpoint usado: POST {url_base}/message/sendText/{instancia}
Header: apikey: {api_key}
Body:  {"number": "<DDI+numero>", "text": "<mensagem formatada>"}

Documentação de referência: https://doc.evolution-api.com/

OBS: o terreno está pronto (formatação + montagem da chamada HTTP), mas o
envio real está atrás de MODO_SIMULADO = True até validarmos a instância da
Evolution API (URL, nome da instância e apikey).
"""

import json
import urllib.request
import urllib.error

import log

NOME = "WhatsApp (Evolution API)"

CAMPOS_CONFIG = [
    {"chave": "url_base", "label": "URL da Evolution API (ex: http://localhost:8080)", "tipo": "texto"},
    {"chave": "instancia", "label": "Nome da Instância", "tipo": "texto"},
    {"chave": "api_key", "label": "API Key (apikey)", "tipo": "senha"},
    {"chave": "numero", "label": "Número de destino (com DDI, ex: 5511999999999)", "tipo": "texto"},
]

# Tradutor de siglas para nome de cidade "bonito" na mensagem
_CIDADES = {
    "GRU": "São Paulo", "GIG": "Rio de Janeiro", "JFK": "Nova York",
    "MCO": "Orlando", "LIS": "Lisboa", "OPO": "Porto",
    "CDG": "Paris", "MAD": "Madri",
}


def _formatar_mensagem(voo: dict) -> str:
    """Monta o texto da oferta formatado com a sintaxe de estilo do WhatsApp
    (*negrito*, _itálico_, ~tachado~, ``` monoespaçado ```)."""
    origem = voo.get("origem", "")
    destino = voo.get("destino", "")
    ida = voo.get("data_ida", "")
    volta = voo.get("data_volta", "")
    valor = voo.get("valor", 0)
    moeda = voo.get("moeda", "R$")
    cia = voo.get("companhia", "N/A")
    link = voo.get("link", "")
    score = int(voo.get("score", 0))

    valor_fmt = f"{float(valor):,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

    nome_destino = _CIDADES.get(destino, destino)
    nome_origem = _CIDADES.get(origem, origem)

    chamas = "🔥" * min((score // 10) + 1, 5) if score > 0 else ""
    tipo_txt = "Ida e Volta" if volta else "Apenas Ida"

    linhas = []
    linhas.append(f"✈️ *{nome_origem} ({origem}) ➔ {nome_destino} ({destino})*")
    if score > 0:
        linhas.append(f"_Score: {score}%_ {chamas}")
    linhas.append("")
    linhas.append(f"💰 *{moeda} {valor_fmt}*")
    linhas.append(f"🏷️ {cia} | {tipo_txt}")
    linhas.append("")
    linhas.append(f"🛫 Ida: {ida}")
    if volta:
        linhas.append(f"🛬 Volta: {volta}")
    linhas.append("")
    if link:
        linhas.append(f"🔗 {link}")

    return "\n".join(linhas)


def _montar_url(url_base: str, instancia: str) -> str:
    url_base = (url_base or "").strip().rstrip("/")
    instancia = (instancia or "").strip()
    return f"{url_base}/message/sendText/{instancia}"


def _enviar_para_evolution_api(url: str, api_key: str, numero: str, texto: str) -> None:
    """Faz o POST para a Evolution API. Lança exceção em caso de falha."""
    payload = {
        "number": numero,
        "text": texto,
    }

    dados = json.dumps(payload).encode("utf-8")
    requisicao = urllib.request.Request(
        url,
        data=dados,
        method="POST",
        headers={
            "Content-Type": "application/json",
            "apikey": api_key,
        },
    )

    with urllib.request.urlopen(requisicao, timeout=15) as resposta:
        resposta.read()


def enviar(voo: dict, config: dict, log_callback=None) -> None:
    callback = log_callback or log.registrar
    config = config or {}

    url_base = config.get("url_base", "").strip()
    instancia = config.get("instancia", "").strip()
    api_key = config.get("api_key", "").strip()
    numero = config.get("numero", "").strip()

    if not url_base or not instancia or not api_key or not numero:
        callback(
            "WhatsApp (Evolution API) não configurado corretamente "
            "(preencha URL, Instância, API Key e Número).",
            "AVISO", "whatsapp",
        )
        return

    texto = _formatar_mensagem(voo)
    url = _montar_url(url_base, instancia)

    # Terreno pronto para o envio real. Enquanto a instância não for validada,
    # deixamos em modo simulado (apenas loga o que seria enviado).
    MODO_SIMULADO = True

    if MODO_SIMULADO:
        callback(
            f"[SIMULADO] Enviaria via Evolution API ({url}) para {numero}:\n{texto}",
            "INFO", "whatsapp",
        )
        return

    try:
        _enviar_para_evolution_api(url, api_key, numero, texto)
        callback(f"Oferta {voo.get('origem')}->{voo.get('destino')} enviada ao WhatsApp {numero}.",
                  "SUCESSO", "whatsapp")
    except urllib.error.HTTPError as e:
        corpo_erro = e.read().decode("utf-8", errors="ignore")
        callback(f"Erro HTTP ao enviar WhatsApp ({e.code}): {corpo_erro}", "ERRO", "whatsapp")
    except urllib.error.URLError as e:
        callback(f"Erro de conexão com a Evolution API: {e.reason}", "ERRO", "whatsapp")
    except Exception as e:
        callback(f"Erro inesperado ao enviar WhatsApp: {e}", "ERRO", "whatsapp")