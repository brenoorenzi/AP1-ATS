def calcular_desconto(valor):
    if valor <= 0:
        raise ValueError("Valor inválido")
    if valor <= 100.0:
        return valor
    if valor > 100.0 and valor <= 500.0:
        return valor - (valor * 0.10)
    if valor > 500.0:
        return valor - (valor * 0.20)