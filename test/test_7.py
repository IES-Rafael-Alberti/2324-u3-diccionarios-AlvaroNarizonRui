from src.ejercicio7 import devolver_listaCompra
import pytest

def test_lista_compra():
    almacen = {"garbanzos":3.50,"lentejas":4.50,"carbón":5.0}
    assert devolver_listaCompra(almacen) == "Lista de la compra\ngarbanzos 3.50\nlentejas 4.50\ncarbón 5.0\n\nTotal Coste"

if __name__ == "__main__":
    pytest.main()