"""Ejercicio 3.2.9¶
Escribir un programa que gestione las facturas pendientes 
de cobro de una empresa. Las facturas se almacenarán en un 
diccionario donde la clave de cada factura será el número 
de factura y el valor el coste de la factura. El programa 
debe preguntar al usuario si quiere añadir una nueva factura, 
pagar una existente o terminar. Si desea añadir una nueva 
factura se preguntará por el número de factura y su coste y 
se añadirá al diccionario. Si se desea pagar una factura 
se preguntará por el número de factura y se eliminará 
del diccionario. Después de cada operación 
el programa debe mostrar por pantalla la cantidad 
cobrada hasta el momento y la cantidad pendiente de cobro."""

def añadir_factura(facturas:dict,numero_factura:int,coste_factura:float):
    """Añade una factura a un diccionario de facturas
    :param facturas: diccionario que contendrá los numeros de facturas y los costes de cada una.
    :type facturas: dict
    :param numero_factura: Clave dentro del diccionario. El identificador de cada factura.
    :type numero_factura: int
    :param coste_factura: Valor dentro del diccionario. Almacenará el coste de cada factura
    :type coste_factura: float
    """
    facturas[numero_factura] = coste_factura

def eliminar_factura(facturas:dict,numero_factura:int,cantidad_cobrada:float) -> float:
    """Elimina una factura de un diccionario de facturas. Además, eliminar del diccionario una
    factura significa haberla pagado por lo que su coste se sumará a una variable y se devolverá
    al finalizar la operación.
    :param facturas: diccionario que contendrá los numeros de facturas y los costes de cada una.
    :type facturas: dict
    :param numero_factura: Clave dentro del diccionario. El identificador de cada factura.
    :type numero_factura: int
    :param cantidad_cobrada: La cantidad de dinero total de todas las facturas que han sido eliminadas(pagadas).
    :type cantidad_cobrada: float
    :returns: La cantidad pagada. Es la suma de todas las facturas que se han eliminado hasta el momento
    :rtype: float
    """
    cantidad_cobrada += facturas[numero_factura]
    del facturas[numero_factura]
    return cantidad_cobrada

def calcular_facturas_pendientes(facturas:dict) -> float:
    """Calcula las facturas pendientes de pago (Las que están almacenadas dentro del diccionario)
    :param facturas: diccionario que contendrá los numeros de facturas y los costes de cada una.
    :type facturas: dict
    :returns: La cantidad pendiente de pago. Es la suma de todas las facturas que hay dentro del
    diccionario de facturas.
    :rtype: float
    """
    cantidad_pendiente = sum(facturas.values())
    return cantidad_pendiente



if __name__ == "__main__":
    facturas = {}
    cantidad_pendiente = 0.0
    cantidad_cobrada = 0.0
    terminar = False
    while terminar != True:
        eleccion = int(input("Qué desea hacer :\n1. Añadir factura\n2. Pagar una existente\n3. Terminar\n Eleccion : "))

        if eleccion == 1:
            #Entrada
            numero_factura = int(input("Escribe el número de tu factura : "))
            coste_factura = float(input("Escribe el coste de tu factura : "))
            #Procesamiento
            añadir_factura(facturas,numero_factura,coste_factura)
            cantidad_pendiente = calcular_facturas_pendientes(facturas)
            #Salida
            print(f"Tienes {cantidad_pendiente} euros pendientes de pago y {cantidad_cobrada} pagada")

        elif eleccion == 2:
            #Entrada
            numero_factura = int(input("Escribe un número de factura a pagar : "))
            #Procesamiento
            cantidad_cobrada += eliminar_factura(facturas,numero_factura,cantidad_cobrada)
            cantidad_pendiente -= cantidad_cobrada
            #Salida
            print(f"Tienes {cantidad_pendiente} euros pendientes de pago y {cantidad_cobrada} pagada") 
        
        elif eleccion == 3:
            terminar = True
        