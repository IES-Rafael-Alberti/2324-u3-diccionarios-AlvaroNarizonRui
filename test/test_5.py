from src.ejercicio5 import calcular_creditos
import pytest

def test_calcular_creditos():
    asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
    assert calcular_creditos(asignaturas) == 15


if __name__ == "__main__":
    pytest.main()