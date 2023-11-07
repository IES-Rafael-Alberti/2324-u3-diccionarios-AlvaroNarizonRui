from src.ejercicio7 import devolver_listaCompra
import pytest

def test_lista_compra():
    almacen = {"garbanzos": 3.50, "lentejas": 4.50, "carbón": 5.0}
    resultado = devolver_listaCompra(almacen)
    assert resultado == "Lista de la compra\n" + "garbanzos 3.5\n" + "lentejas 4.5\n" + "carbón 5.0\n" + "\nTotal Coste"


if __name__ == "__main__":
    pytest.main()