"""
condicoes.py
------------
Guarda e avalia as "Condições" (filtros) que o tópico 2 da interface
configura. Tudo é opcional: quanto mais campos preenchidos, mais
específica é a passagem que o buscador vai deixar passar pro output.

As condições são persistidas em condicoes.json (na raiz do projeto),
e o buscador.py lê esse arquivo pra saber o que validar a cada voo
retornado pelas apis_input.
"""

import json
import os

ARQUIVO_CONDICOES = os.path.join(os.path.dirname(os.path.abspath(__file__)), "condicoes.json")

# Campos suportados. Todos opcionais (None ou "" = sem filtro nesse campo).
CAMPOS_PADRAO = {
    "origem": "",          # ex: "Rio de Janeiro (GIG)"
    "destino": "",         # ex: "Lisboa (LIS)"
    "tipo_viagem": "",     # "ida", "ida_volta" ou "" (sem filtro)
    "mes": "",             # ex: "12" (dezembro)
    "ano": "",             # ex: "2025"
    "data_ida": "",        # opcional, formato livre "DD/MM/AAAA"
    "data_volta": "",      # opcional
    "valor_minimo": "",    # string numérica, ex: "0"
    "valor_maximo": "",    # string numérica, ex: "3000"
    "moeda": "BRL",
    "observacoes": "",     # anotação livre do usuário sobre esse filtro
}


def carregar() -> dict:
    """Carrega as condições salvas. Se não existir arquivo, retorna padrão vazio."""
    if not os.path.exists(ARQUIVO_CONDICOES):
        return dict(CAMPOS_PADRAO)
    try:
        with open(ARQUIVO_CONDICOES, "r", encoding="utf-8") as f:
            dados = json.load(f)
        completo = dict(CAMPOS_PADRAO)
        completo.update(dados)
        return completo
    except (json.JSONDecodeError, OSError):
        return dict(CAMPOS_PADRAO)


def salvar(condicoes: dict) -> None:
    """Salva as condições vindas da interface (tópico 2)."""
    completo = dict(CAMPOS_PADRAO)
    completo.update(condicoes or {})
    with open(ARQUIVO_CONDICOES, "w", encoding="utf-8") as f:
        json.dump(completo, f, ensure_ascii=False, indent=2)


def _texto_bate(filtro: str, valor: str) -> bool:
    """
    Compara texto ignorando maiúsculas/minúsculas.
    Agora suporta múltiplos valores separados por vírgula na interface (Ex: LIS, OPO).
    Filtro vazio = sempre bate.
    """
    if not filtro:
        return True
    if not valor:
        return False
        
    # Separa os filtros por vírgula e limpa os espaços
    termos_filtro = [t.strip().lower() for t in filtro.split(",") if t.strip()]
    valor_voo = valor.strip().lower()
    
    # Se a origem/destino do voo bater com qualquer um dos itens separados por vírgula, passa
    for termo in termos_filtro:
        if termo in valor_voo or valor_voo in termo:
            return True
            
    return False


def _numero(valor):
    try:
        return float(str(valor).replace(",", ".").strip())
    except (ValueError, TypeError):
        return None


def passagem_atende(voo: dict, condicoes: dict = None) -> bool:
    """
    Verifica se um voo (dict retornado por uma api_input) atende às
    condições configuradas. Estrutura esperada de `voo` (chaves opcionais,
    cada api_input deve tentar preencher o máximo possível):

    {
        "origem": "Rio de Janeiro (GIG)",
        "destino": "Lisboa (LIS)",
        "tipo_viagem": "ida_volta",
        "data_ida": "10/12/2025",
        "data_volta": "20/12/2025",
        "valor": 2850.00,
        "moeda": "BRL",
        "companhia": "TAP",
        "link": "https://...",
    }

    Regra: campo de condição vazio = não filtra por ele.
    Campo de condição preenchido, mas o voo não tem essa informação = não bate
    (não arriscamos falso positivo).
    """
    condicoes = condicoes or carregar()

    if not _texto_bate(condicoes.get("origem", ""), voo.get("origem", "")):
        return False
    if not _texto_bate(condicoes.get("destino", ""), voo.get("destino", "")):
        return False

    tipo_filtro = (condicoes.get("tipo_viagem") or "").strip().lower()
    if tipo_filtro:
        if (voo.get("tipo_viagem") or "").strip().lower() != tipo_filtro:
            return False

    mes_filtro = (condicoes.get("mes") or "").strip()
    ano_filtro = (condicoes.get("ano") or "").strip()
    if mes_filtro or ano_filtro:
        data_ida = voo.get("data_ida", "")
        partes = data_ida.split("/") if data_ida else []
        if len(partes) != 3:
            return False
        _, mes_voo, ano_voo = partes
        if mes_filtro and mes_filtro.zfill(2) != mes_voo.zfill(2):
            return False
        if ano_filtro and ano_filtro != ano_voo:
            return False

    if condicoes.get("data_ida") and condicoes["data_ida"] != voo.get("data_ida", ""):
        return False
    if condicoes.get("data_volta") and condicoes["data_volta"] != voo.get("data_volta", ""):
        return False

    valor_min = _numero(condicoes.get("valor_minimo"))
    valor_max = _numero(condicoes.get("valor_maximo"))
    valor_voo = _numero(voo.get("valor"))

    if (valor_min is not None or valor_max is not None) and valor_voo is None:
        return False
    if valor_min is not None and valor_voo < valor_min:
        return False
    if valor_max is not None and valor_voo > valor_max:
        return False
    
    # Filtro de Menor Preço Histórico
    # Se o checkbox estiver marcado, a passagem PRECISA ter uma pontuação mínima (ex: 10 pontos/10% mais barata)
    exige_historico = str(condicoes.get("apenas_menor_preco", "false")).lower() == "true"
    
    if exige_historico:
        score = int(voo.get("score", 0))
        # Define o nível de exigência. 10 = só deixa passar se for 10% mais barato que a média local.
        if score < 10:
            return False

    return True
