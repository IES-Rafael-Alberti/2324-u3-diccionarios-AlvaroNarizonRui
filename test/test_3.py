from src.ejercicio3 import calcular_kilos_fruta
import pytest

def test_calcular_kilos_fruta():
    frutas = {"Plátano":1.35,"Manzana":0.80,"Pera":0.85,"Naranja":0.70}
    assert calcular_kilos_fruta("Plátano",3,frutas) == 4.05

def test_calcular_kilos_fruta_error():
    frutas = {"Plátano":1.35,"Manzana":0.80,"Pera":0.85,"Naranja":0.70}
    with pytest.raises(NameError):
        calcular_kilos_fruta("Piña",5,frutas)

def test_calcular_kilos_fruta_0():
    frutas = {"Plátano":1.35,"Manzana":0.80,"Pera":0.85,"Naranja":0.70}
    assert calcular_kilos_fruta("Manzana",0,frutas) == 0.0

if __name__ == "__main__":
    pytest.main()
