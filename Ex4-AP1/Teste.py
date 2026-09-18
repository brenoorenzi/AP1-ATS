# Teste.py
import pytest
from Funcao import calcula_total

def test_calcula_total_sem_fixture():
    carrinho = [
        {'nome': 'Maçã', 'preco': 2.0, 'quantidade': 3},
        {'nome': 'Banana', 'preco': 1.5, 'quantidade': 2}
    ]
    
    resultado = calcula_total(carrinho)
    assert resultado == 9.0