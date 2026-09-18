# Teste_refatorado.py
import pytest
from Funcao import calcula_total

@pytest.fixture
def carrinho_de_compras():
    return [
        {'nome': 'Maçã', 'preco': 2.0, 'quantidade': 3},
        {'nome': 'Banana', 'preco': 1.5, 'quantidade': 2}
    ]

def test_calcula_total_com_fixture(carrinho_de_compras):
    resultado = calcula_total(carrinho_de_compras)
    assert resultado == 9.0