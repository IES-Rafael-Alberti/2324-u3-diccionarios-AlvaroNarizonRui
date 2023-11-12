"""Ejercicio 3.2.2¶
Escribir un programa que pregunte al usuario su nombre, edad, dirección
y teléfono y lo guarde en un diccionario. Después debe mostrar por pantalla
el mensaje <nombre> tiene <edad> años, vive en <dirección> y su número de 
teléfono es <teléfono>."""

def añadir_usuario(nombre,edad,direccion,telefono) -> dict:
    usuarios = {}
    usuarios[nombre] = [edad,direccion,telefono]
    return usuarios

if __name__ == "__main__":
    #Entrada
    nombre = input("Escribe tu nombre : ")
    edad = int(input("Escribe tu edad : "))
    direccion = input("Escribe tu direccion : ")
    telefono = int(input("Escribe tu numero de telefono : "))
    #Procesamiento
    usuario = añadir_usuario(usuarios,nombre,edad,direccion,telefono)
    #Salida
    print(f"{nombre} tiene {usuario[nombre][0]} años, vive en {usuario[nombre][1]} y su numero de telefono es {usuario[nombre][2]}")