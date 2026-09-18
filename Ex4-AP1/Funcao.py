# Funcao.py

def calcula_total(carrinho):
    return sum(item['preco'] * item['quantidade'] for item in carrinho)