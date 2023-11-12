from src.ejercicio8 import traductor_español_ingles
import pytest

def test_traduccion_correcta():
    diccionario_español_ingles = {"hola":"hello","adios":"goodbye"}
    assert traductor_español_ingles(diccionario_español_ingles,"hola") == "hello"

def test_traduccion_incorrecta():
    diccionario_español_ingles = {"hola":"hello","adios":"goodbye"}
    assert traductor_español_ingles(diccionario_español_ingles,"negro") == ""

if __name__ == "__main__":
    pytest.main()