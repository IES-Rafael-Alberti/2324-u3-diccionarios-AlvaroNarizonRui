from src.ejercicio9 import eliminar_factura,calcular_facturas_pendientes
import pytest

def test_eliminar_factura():
    facturas = {1:20.0,2:20.0}
    cantidad_cobrada = 0
    assert eliminar_factura(facturas,1,0) == 20.0

def test_calcular_facturas_pendientes():
    facturas = {1:20.0,2:30.0,3:40.0}
    assert calcular_facturas_pendientes(facturas) == 90.0

if __name__ == "__main__":
    pytest.main()
