def calcular_desconto(valor):
    if valor <= 0:
        raise ValueError("Valor inválido")
    if valor > 500.0:
        return valor * 0.80
    if valor > 100.0:
        return valor * 0.90
    return valor