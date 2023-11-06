from src.ejercicio1 import buscar_divisa
import pytest

def test_buscar_divisa():
    assert buscar_divisa("Euro") == "€"

def test_buscar_divisa_error():
    with pytest.raises(NameError):
        buscar_divisa("Pesetas")

if __name__ == "__main__":
    pytest.main()