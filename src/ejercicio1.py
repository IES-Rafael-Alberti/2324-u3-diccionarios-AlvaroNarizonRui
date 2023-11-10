"""
Ejercicio 3.2.1¶
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si 
la divisa no está en el diccionario"""

def buscar_divisa(divisas:dict,codigo_divisa:str) -> str:
    """Devuelve el simbolo de una divisa

    :param divisas: diccionario con el par codigo_divisa:simbolo_divisa
    :type divisas: dict
    :param codigo_divisa: Código de la divisa a buscar
    :type codigo_divisa: str
    :returns: el simbolo de la divisa. Si codigo_divisa no esta en el diccioario devuleve "".
    :rtype: str
    """
    return divisas.get(codigo_divisa,"")
    

if __name__ == "__main__":
    divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}

    #Entrada
    codigo_divisa = input("Escribe una divisa a buscar : ")

    #Procesamiento
    simbolo = buscar_divisa(divisas,codigo_divisa)
    
    #Salida
    if simbolo:
        print(f"El simbolo de la divisa {codigo_divisa} es : {simbolo}")
    else:
        print("No se encuentra la divisa que introdujiste")

