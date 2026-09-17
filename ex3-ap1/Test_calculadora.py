import pytest
from calculadora import calcular_desconto

def test_valor_zero_ou_negativo():
    with pytest.raises(ValueError):
        calcular_desconto(0)
    with pytest.raises(ValueError):
        calcular_desconto(-10.50)

def test_compras_sem_desconto():
    assert calcular_desconto(50.0) == 50.0
    assert calcular_desconto(100.0) == 100.0

def test_compras_dez_porcento_desconto():
    assert calcular_desconto(150.0) == 135.0
    assert calcular_desconto(500.0) == 450.0

def test_compras_vinte_porcento_desconto():
    assert calcular_desconto(600.0) == 480.0
    assert calcular_desconto(1000.0) == 800.0