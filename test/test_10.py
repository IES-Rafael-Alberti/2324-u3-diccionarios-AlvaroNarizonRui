from src.ejercicio10 import mostrar_cliente_especifico,mostrar_clientes
import pytest

def test_mostrar_cliente_especifico():
    clientes = {1 : {"nombre" : "Pepe","direccion" : "Calle Alfonso X","telefono" : 6645343,"correo":"pepereina@gmail.com","preferente":True}}
    resultado = mostrar_cliente_especifico(clientes,1)
    assert mostrar_cliente_especifico(clientes,1) == resultado

def test_mostrar_clientes():
    clientes = {1 : {"nombre" : "Pepe","direccion" : "Calle Alfonso X","telefono" : 6645343,"correo":"pepereina@gmail.com","preferente":True} , 2 : {"nombre" : "Jorge","direccion" : "Calle San Fernando n1","telefono" : 960459081,"correo":"jorgeherrera@gmail.com","preferente":False} , 3 : {"nombre" : "Helena","direccion" : "Los Gallos","telefono" : 567908121,"correo":"helenagarciadiz@gmail.com","preferente":True}}
    resultado = mostrar_clientes(clientes)
    assert mostrar_clientes(clientes) == resultado

if __name__ == "__main__":
    pytest.main()