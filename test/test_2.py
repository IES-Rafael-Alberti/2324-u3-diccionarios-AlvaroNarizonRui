from src.ejercicio2 import añadir_usuario
import pytest

def test_ingreso_usuario():
    assert añadir_usuario("Daniel",21,"Barriada Rio San Pedro",667304353) == {"Daniel":[21,"Barriada Rio San Pedro",667304353]}

if __name__ == "__main__":
    pytest.main()