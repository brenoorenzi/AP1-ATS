def calcular_classificacao_imc(altura, peso, nome):

    if not isinstance(altura, (int, float)) or not isinstance(peso, (int, float)):
        raise TypeError("Altura e peso devem ser do tipo float ou int.")
    
 
    imc = peso / (altura ** 2)
    
   
    if imc < 18.5:
        classificacao = "Abaixo do peso"
    elif imc <= 24.9:
        classificacao = "Peso normal"
    elif imc <= 29.9:
        classificacao = "Sobrepeso"
    elif imc <= 34.9:
        classificacao = "Obesidade grau I"
    elif imc <= 39.9:
        classificacao = "Obesidade grau II"
    else:
        classificacao = "Obesidade grau III"
        
    return f"{nome}: {classificacao}"