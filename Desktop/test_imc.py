import pytest
from imc import calcular_classificacao_imc

def test_type_error_altura():

    with pytest.raises(TypeError):
        calcular_classificacao_imc("1.85", 85.0, "pedro")

def test_type_error_peso():

    with pytest.raises(TypeError):
        calcular_classificacao_imc(1.85, "85", "pedro")

def test_imc_valido():

    resultado = calcular_classificacao_imc(1.85, 85, "pedro")
    assert resultado == "pedro: Peso normal"