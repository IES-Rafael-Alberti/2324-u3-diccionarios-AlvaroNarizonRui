from src.ejercicio11 import crear_directorio_clientes
import pytest

def test_crear_directorio_clientes():
    cadena = "nif;nombre;email;teléfono;descuento\n01234567L;Luis González;luisgonzalez@mail.com;656343576;12.5\n71476342J;Macarena Ramírez;macarena@mail.com;692839321;8\n63823376M;Juan José Martínez;juanjo@mail.com;664888233;5.2\n98376547F;Carmen Sánchez;carmen@mail.com;667677855;15.7"
    lista_clientes = cadena.split("\n")
    directorio = {}
    lista_campos = lista_clientes[0].split(";")

    resultado = crear_directorio_clientes(directorio,lista_clientes,lista_campos)
    assert crear_directorio_clientes(directorio,lista_clientes,lista_campos) == resultado

if __name__ == "__main__":
    pytest.main()