"""
Ejercicio 3.2.1¶
Escribir un programa que guarde en una variable el diccionario {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}, 
pregunte al usuario por una divisa y muestre su símbolo o un mensaje de aviso si 
la divisa no está en el diccionario"""

def buscar_divisa(divisa):
    divisas = {'Euro':'€', 'Dollar':'$', 'Yen':'¥'}
    if divisa in divisas:
        return divisas[divisa]
    else:
        raise NameError

if __name__ == "__main__":
    try:
        #Entrada
        divisa = input("Escribe una divisa a buscar : ")
        #Procesamiento
        simbolo = buscar_divisa(divisa)
        #Salida
        print(f"El simbolo de la divisa {divisa} es : {simbolo}")
    except NameError:
        print("No se encuentra la divisa que introdujiste")