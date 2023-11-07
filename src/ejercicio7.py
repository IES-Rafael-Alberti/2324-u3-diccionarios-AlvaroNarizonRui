"""
Ejercicio 3.2.7¶
Escribir un programa que cree un diccionario simulando una cesta de la compra. 
El programa debe preguntar el artículo y su precio y añadir el par al diccionario, 
hasta que el usuario decida terminar. Después se debe mostrar 
por pantalla la lista de la compra y el coste total, con el siguiente formato

Lista de la compra	
Artículo 1	Precio
Artículo 2	Precio
Artículo 3	Precio
…	…
Total	Coste
"""
def devolver_listaCompra(almacen:dict) -> str:
    """Devuelve la lista de la compra
    :param almacen: diccionario con el par articulo:precio.
    :type almacen: dict
    :returns: La lista de la compra. Convierte el contenido del diccionario a un string formateado y lo devuelve"".
    :rtype: str
    """
    compra = "Lista de la compra\n"
    for i, j in almacen.items():
        compra += str(i) + " " + str(j) + "\n"
    compra += "\nTotal Coste"
    return compra

def añadir_articulo(almacen:dict,articulo:str,precio:float):
    """Añade un par clave:valor a un diccionario
    :param almacen: diccionario al que se va a añadir el articulo.
    :type almacen: dict
    :param articulo: String que ocupará la posición de clave dentro del diccionario.
    :type articulo: str
    :param precio: Decimal, será el precio del artículo, ocupa la posición de valor dentro del diccionario.
    :type precio: float
    """
    almacen[articulo] = precio

if __name__ == "__main__":
    almacen = {}
    final = False
    while final != True:
        #Entrada
        eleccion = str(input("Desea introducir un producto)? (si/no) : "))
        if eleccion.lower() == "si":
            articulo = input("Escribe el nombre del articulo a añadir : ")
            precio = float(input("Introduce el precio del articulo : "))
            #Procesamiento
            añadir_articulo(almacen,articulo,precio)
            lista_compra = devolver_listaCompra(almacen)
        elif eleccion.lower() == "no":
            final = True
    #Salida
    print(f"{lista_compra}")

