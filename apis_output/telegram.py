"""
apis_output/telegram.py
-----------------------
Envia notificações de passagens para o Telegram usando templates dinâmicos.
Preparado para o futuro anexo de imagens globais (sendPhoto).
"""
import requests
import random
import log

NOME = "Telegram"

CAMPOS_CONFIG = [
    {"chave": "bot_token", "label": "Bot Token (@BotFather)", "tipo": "senha"},
    {"chave": "chat_id", "label": "Seu Chat ID", "tipo": "texto"},
    {"chave": "estilo", "label": "Estilo da Mensagem (1 a 10 ou 'aleatorio')", "tipo": "texto"},
]

# Banco de dados rápido para mapear aeroportos para Nomes e Bandeiras
_AEROPORTOS = {
    "GRU": {"cidade": "Guarulhos", "bandeira": "🇧🇷"},
    "GIG": {"cidade": "Rio de Janeiro", "bandeira": "🇧🇷"},
    "JFK": {"cidade": "Nova York", "bandeira": "🇺🇸"},
    "MCO": {"cidade": "Orlando", "bandeira": "🇺🇸"},
    "LIS": {"cidade": "Lisboa", "bandeira": "🇵🇹"},
    "OPO": {"cidade": "Porto", "bandeira": "🇵🇹"},
    "CDG": {"cidade": "Paris", "bandeira": "🇫🇷"},
}

def _formatar_moeda(valor):
    """Garante que 6796.0 vire 6.796,00"""
    return f"{valor:,.2f}".replace(",", "X").replace(".", ",").replace("X", ".")

def _gerar_mensagem(voo: dict, estilo: str) -> str:
    """Gera o texto com base no estilo escolhido ou sorteia um."""
    
    origem_cod = voo.get("origem", "")
    destino_cod = voo.get("destino", "")
    
    dados_origem = _AEROPORTOS.get(origem_cod, {"cidade": origem_cod, "bandeira": ""})
    dados_destino = _AEROPORTOS.get(destino_cod, {"cidade": destino_cod, "bandeira": ""})
    
    cid_orig = dados_origem["cidade"]
    cid_dest = dados_destino["cidade"]
    band_orig = dados_origem["bandeira"]
    band_dest = dados_destino["bandeira"]
    
    ida = voo.get("data_ida", "")
    volta = voo.get("data_volta", "Não definida")
    valor_fmt = _formatar_moeda(voo.get("valor", 0))
    moeda = voo.get("moeda", "R$")
    cia = voo.get("companhia", "N/A")
    link = voo.get("link", "")

    templates = {
        "1": f"✈️ Passagem encontrada!\nSaindo de {cid_orig} ({origem_cod}) para {cid_dest} ({destino_cod}) em {ida}, com retorno de {cid_dest} para {cid_orig} em {volta}.\n💰 Valor: {moeda} {valor_fmt}\n🛫 Companhia: {cia}\n🔗 Confira: {link}",
        
        "2": f"🚨 ALERTA DE PASSAGEM\n{cid_orig} {band_orig} → {cid_dest} {band_dest}\nIda: {ida}\nVolta: {volta}\n✈️ {cia}\n💵 {moeda} {valor_fmt}\n👉 Confira a oferta: {link}",
        
        "3": f"✈️ Achei uma passagem!\n{cid_orig} → {cid_dest}\n📅 Ida: {ida}\n📅 Volta: {volta}\n💰 {moeda} {valor_fmt}\n🛫 {cia}\n\n🔗 Link da passagem:\n{link}",
        
        "4": f"🔥 OPORTUNIDADE DE VOO\nEncontramos uma passagem de {cid_orig} para {cid_dest} por apenas {moeda} {valor_fmt}.\n\n✈️ {cia}\n🗓️ Ida: {ida}\n🗓️ Retorno: {volta}\n\n🔎 Ver passagem: {link}",
        
        "5": f"✈️ {origem_cod} → {destino_cod} | {ida} → {volta}\n{cia} | {moeda} {valor_fmt}\n🔗 {link}",
        
        "6": f"Encontramos uma passagem saindo de {cid_orig} para {cid_dest} no dia {ida}, com retorno no dia {volta}.\nO voo está sendo oferecido pela {cia} por {moeda} {valor_fmt}.\n\nConfira os detalhes: {link}",
        
        "7": f"🎯 Nova passagem encontrada!\n\n📍 {cid_orig} ({origem_cod}) → {cid_dest} ({destino_cod})\n📅 {ida} → {volta}\n✈️ {cia}\n💰 {moeda} {valor_fmt}\n\n🔗 Ver oferta: {link}",
        
        "8": f"{cid_orig} → {cid_dest}\n{ida} — {volta}\n\n{cia}\n{moeda} {valor_fmt}\n\nConsulte os detalhes da tarifa:\n{link}",
        
        "9": f"🔔 Nova passagem encontrada\n{origem_cod} → {destino_cod}\n{ida} a {volta}\n{cia}\n{moeda} {valor_fmt}\n\n🔗 Acessar: {link}",
        
        "10": f"✈️ Oferta de viagem encontrada\n\nOrigem: {cid_orig} ({origem_cod})\nDestino: {cid_dest} ({destino_cod})\nIda: {ida}\nVolta: {volta}\nCompanhia: {cia}\nValor: {moeda} {valor_fmt}\n\n🔗 Consulte a passagem: {link}"
    }

    estilo_str = str(estilo).strip().lower()
    if estilo_str not in templates:
        estilo_str = str(random.randint(1, 10))

    return templates[estilo_str]


def enviar(voo: dict, config: dict, log_callback=None) -> None:
    token = config.get("bot_token", "").strip()
    chat_id = config.get("chat_id", "").strip()
    estilo_escolhido = config.get("estilo", "aleatorio")
    
    if not token or not chat_id:
        if log_callback: log_callback("Telegram: Token ou Chat ID vazios.", nivel="ERRO", origem=NOME)
        return

    texto_final = _gerar_mensagem(voo, estilo_escolhido)

    # FUTURO: Dicionário de imagens globais
    db_imagens = {
        "JFK": "https://images.unsplash.com/photo-1496442226666-8d4d0e62e6e9?w=800", # NY
        "LIS": "https://images.unsplash.com/photo-1585208798174-6cedd86e019a?w=800", # Lisboa
    }
    
    imagem_url = db_imagens.get(voo.get("destino", ""))
    
    try:
        if imagem_url:
            # Se tiver imagem mapeada, envia como foto (o texto vai na legenda)
            url = f"https://api.telegram.org/bot{token}/sendPhoto"
            payload = {
                "chat_id": chat_id,
                "photo": imagem_url,
                "caption": texto_final,
                "parse_mode": "HTML"
            }
        else:
            # Se não tiver, envia apenas o texto limpo
            url = f"https://api.telegram.org/bot{token}/sendMessage"
            payload = {
                "chat_id": chat_id,
                "text": texto_final,
                "parse_mode": "HTML",
                "disable_web_page_preview": True
            }

        resp = requests.post(url, json=payload)
        resp.raise_for_status()
        if log_callback:
            log_callback(f"Notificação premium enviada: {voo.get('origem')}->{voo.get('destino')}", nivel="SUCESSO", origem=NOME)
            
    except Exception as e:
        if log_callback:
            log_callback(f"Falha ao notificar via Telegram: {e}", nivel="ERRO", origem=NOME)