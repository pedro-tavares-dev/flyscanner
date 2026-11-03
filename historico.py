"""
historico.py
------------
Motor de inteligência de preços do FlyScanner.
Aprende a média de cada rota com base no fluxo do buscador e calcula o score de desconto.
"""
import json
import os

ARQUIVO_HISTORICO = os.path.join(os.path.dirname(os.path.abspath(__file__)), "historico.json")

def carregar_db():
    if not os.path.exists(ARQUIVO_HISTORICO):
        return {}
    try:
        with open(ARQUIVO_HISTORICO, "r", encoding="utf-8") as f:
            return json.load(f)
    except:
        return {}

def salvar_db(db):
    with open(ARQUIVO_HISTORICO, "w", encoding="utf-8") as f:
        json.dump(db, f, ensure_ascii=False, indent=2)

def processar_score(voo: dict) -> dict:
    """
    Recebe um voo, atualiza a média histórica daquela rota/mês
    e injeta a pontuação de desconto no dicionário do voo.
    """
    db = carregar_db()
    
    # Chave única para a média: Ex: "GIG-LIS-12-2026-BRL"
    mes_ano = voo.get("data_ida", "")[3:] if voo.get("data_ida") else "geral"
    chave = f"{voo.get('origem')}-{voo.get('destino')}-{mes_ano}-{voo.get('moeda')}"
    preco_atual = float(voo.get("valor", 0))

    if preco_atual <= 0:
        voo["score"] = 0
        return voo

    # Se a rota já existe no banco, calcula o score baseado na média histórica
    if chave in db:
        media_historica = db[chave]["soma"] / db[chave]["quantidade"]
        
        # Lógica de Pontos: (Média - Preço Atual) / Média * 100
        # Ex: Média 2500, Atual 2000 -> (500 / 2500) * 100 = 20 pontos
        if preco_atual < media_historica:
            desconto_percentual = ((media_historica - preco_atual) / media_historica) * 100
            voo["score"] = int(desconto_percentual)
        else:
            voo["score"] = 0 # Está mais caro ou igual à média
            
        # Atualiza o banco de dados com o novo preço encontrado para manter a média viva
        db[chave]["soma"] += preco_atual
        db[chave]["quantidade"] += 1
    else:
        # Primeira vez que o robô vê essa rota no mês. Não há como comparar ainda.
        voo["score"] = 0
        db[chave] = {"soma": preco_atual, "quantidade": 1}

    # Salva o aprendizado
    salvar_db(db)
    
    return voo