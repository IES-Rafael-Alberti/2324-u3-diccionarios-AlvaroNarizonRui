from src.ejercicio4 import convertidor_meses
import pytest

def test_convertidor_meses_correcto():
    assert convertidor_meses("03") == "marzo"

def test_convertidor_meses_error():
    with pytest.raises(ValueError):
        assert convertidor_meses("13")

def test_convertidor_meses_0():
    with pytest.raises(ValueError):
        assert convertidor_meses("00")

if __name__ == "__main__":
    pytest.main()