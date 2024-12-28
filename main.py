def calcular_orcamento(data):
    tipo = data.get("tipo")
    comprimento = float(data.get("comprimento", 0))
    largura = float(data.get("largura", 0))
    preco_por_metro = float(data.get("preco_por_metro", 0))
    quantidade = int(data.get("quantidade", 0))
    
    # Calcula o custo total
    custo_total = preco_por_metro * comprimento * quantidade
    
    # Retorna a resposta em formato dicionário
    return {
        "tipo": tipo,
        "dimensoes": f"{comprimento}m x {largura}cm",
        "quantidade": quantidade,
        "preco_por_metro": f"R${preco_por_metro:.2f}",
        "custo_total": f"R${custo_total:.2f}"
    }
