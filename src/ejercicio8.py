"""
Ejercicio 3.2.8¶
Escribir un programa que cree un diccionario de 
traducción español-inglés. El usuario introducirá las palabras en español 
e inglés separadas por dos puntos, y cada par <palabra>:<traducción> 
separados por comas. El programa debe crear un diccionario con 
las palabras y sus traducciones. Después pedirá una frase en español y 
utilizará el diccionario para traducirla palabra a palabra. 
Si una palabra no está en el diccionario debe dejarla sin traducir.
"""
def traductor_español_ingles(diccionario_español_ingles:dict,busqueda:str) -> str:
    """Traduce una palabra en español a ingles
    :param diccionario_español_ingles: diccionario que almacena la clave(palabra en español) y su valor(palabra en inglés).
    :type diccionario_español_ingles: dict
    :param busqueda: palabra a buscar en el diccionario
    :returns: traducción de la palabra. Si la encuentra devuelve su traducción al inglés, si no, devuelve un string vacío.
    :rtype: str
    """
    return diccionario_español_ingles.get(busqueda,"")

if __name__ == "__main__":
    diccionario_español_ingles = {}
    #Entrada
    palabras = input("Escribe palabras en español e inglés de la siguiente manera (español:ingles) separados por comas: ")
    lista_palabras_sin_separar = palabras.split(",")
    for i in lista_palabras_sin_separar:
        diccionario_español_ingles[i[0:i.find(":"):]] = i[i.find(":")+1::]
    busqueda = input("Escribe una palabra a buscar : ")
    #Procesamiento
    palabra_traducida = traductor_español_ingles(diccionario_español_ingles,busqueda)
    #Salida
    if palabra_traducida:
        print(f"La traducción de la palabra {busqueda} en inglés es {palabra_traducida}")
    else:
        print("No existe en el diccionario la palabra que buscas")
