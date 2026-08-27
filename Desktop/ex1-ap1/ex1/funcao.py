def calcular_area(base, altura):
    
    if not isinstance(base, (int, float)) or not isinstance(altura, (int, float)):
        raise TypeError("A base e a altura devem ser números.")
    
    if base <= 0 or altura <= 0:
        raise ValueError("A base e a altura não podem ser zero ou negativas.")
    
    return base * altura