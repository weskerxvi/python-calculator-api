import pytest
from src.api import resultado, Historico

def test_soma():
    assert resultado(1, 2, 3) == 5

def test_subtracao():
    assert resultado(2, 10, 4) == 6

def test_divisao():
    assert resultado(3, 10, 2) == 5

def test_divisao_por_zero():
    with pytest.raises(ZeroDivisionError):
        resultado(3, 10, 0)

