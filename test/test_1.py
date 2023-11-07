from src.ejercicio1 import buscar_divisa
import pytest

def test_buscar_divisa():
    divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    assert buscar_divisa(divisas,"Euro") == "€"

def test_buscar_divisa_error():
    divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    assert buscar_divisa(divisas,"Pesos") == ""

if __name__ == "__main__":
    pytest.main()