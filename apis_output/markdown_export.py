"""
apis_output/markdown_export.py
------------------------------
Salva as passagens em um arquivo Markdown (.md) local,
com banners visuais das cidades de destino e tipografia limpa.
"""
import os
import datetime

NOME = "Exportar Markdown"

CAMPOS_CONFIG = [
    {"chave": "nome_arquivo", "label": "Nome do Arquivo (ex: ofertas.md)", "tipo": "texto"},
]

# Tradutor de siglas para a API de imagens buscar a foto certa
_CIDADES = {
    "GRU": "sao+paulo,city", "GIG": "rio+de+janeiro,city", "JFK": "new+york,city",
    "MCO": "orlando,city", "LIS": "lisbon,city", "OPO": "porto,city",
    "CDG": "paris,city", "MAD": "madrid,city"
}

def enviar(voo: dict, config: dict, log_callback=None) -> None:
    nome_arquivo = config.get("nome_arquivo", "passagens_encontradas.md").strip()
    if not nome_arquivo: nome_arquivo = "passagens_encontradas.md"
    if not nome_arquivo.endswith(".md"): nome_arquivo += ".md"

    caminho_arquivo = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), nome_arquivo)

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
    
    # Flags visuais e de Inteligência
    chamas = "🔥" * min((score // 10) + 1, 5) if score > 0 else ""
    badge_score = f" `SCORE {score}%` {chamas}" if score > 0 else ""
    tipo_txt = "Ida e Volta" if volta else "Apenas Ida"

    # Geração da Imagem Dinâmica (Banner Largo 800x250)
    # LoremFlickr é grátis e não exige chave. Ele usa a tag (ex: lisbon,city) para achar a foto.
    tag_imagem = _CIDADES.get(destino, f"{destino},landmark")
    url_imagem = f"https://loremflickr.com/800/250/{tag_imagem}/all"

    # Construção do Card Visual em Markdown
    md_text = f"## ✈️ {origem} ➔ {destino} {badge_score}\n\n"
    md_text += f"![Foto de {destino}]({url_imagem})\n\n"
    md_text += f"**{moeda} {valor_fmt}** | {cia} | {tipo_txt}\n\n"
    md_text += f"- **Ida:** {ida}\n"
    if volta:
        md_text += f"- **Volta:** {volta}\n"
    md_text += f"- **Capturado:** {datetime.datetime.now().strftime('%d/%m %H:%M')}\n\n"
    md_text += f"🔗 **[Finalizar Compra no Google Flights]({link})**\n"
    md_text += "---\n<br>\n\n"

    try:
        with open(caminho_arquivo, "a", encoding="utf-8") as f:
            f.write(md_text)
            
        if log_callback:
            log_callback(f"Oferta visual {origem}->{destino} anexada ao log.", nivel="SUCESSO", origem=NOME)
    except Exception as e:
        if log_callback:
            log_callback(f"Erro ao salvar arquivo MD: {e}", nivel="ERRO", origem=NOME)