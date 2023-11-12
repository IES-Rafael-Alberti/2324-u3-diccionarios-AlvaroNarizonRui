"""Ejercicio 3.2.3¶
Escribir un programa que guarde en un diccionario los precios de las frutas de la tabla, pregunte 
al usuario por una fruta, un número de kilos y muestre por pantalla el precio de ese número de kilos 
de fruta. Si la fruta no está en el diccionario debe mostrar un mensaje informando de ello.

Fruta	Precio
Plátano	1.35
Manzana	0.80
Pera	0.85
Naranja	0.70
"""
def calcular_kilos_fruta(fruta,kilos,frutas):
    if fruta in frutas:
        precio_total = frutas[fruta] * kilos
        return round(precio_total,2)
    else:
        raise NameError

if __name__ == "__main__":
    try:
        frutas = {"Plátano":1.35,"Manzana":0.80,"Pera":0.85,"Naranja":0.70}
        #Entrada
        fruta = input("Elige una fruta : ")
        kilos = int(input(f"Cuántos kilos de {fruta} quiere : "))
        #Procesamiento
        precio_total = calcular_kilos_fruta(fruta,kilos,frutas)
        #Salida
        print(f"{kilos} kg de {fruta} cuestan {precio_total} euros en total")
    except NameError:
        print("La fruta que introdujiste no se encuentra en el almacén")