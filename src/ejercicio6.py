"""
Ejercicio 3.2.6¶
Escribir un programa que cree un diccionario vacío y 
lo vaya llenado con información sobre una persona 
(por ejemplo nombre, edad, sexo, teléfono, correo electrónico, etc.) 
que se le pida al usuario. 
Cada vez que se añada un nuevo dato debe 
imprimirse el contenido del diccionario.
"""

def añadir_datos(datos,nombre,edad,sexo,telefono,correo):
    contenedor_valores = []
    datos[nombre] = contenedor_valores
    contenedor_valores.append(edad)
    

if __name__ == "__main__":
    #Entrada
    datos = {}
    nombre = input("Escribe el nombre de usuario : ")
    edad = int(input("Escribe tu edad : "))
    sexo = input("Cuál es tu genero : ")
    telefono = input("Introduce tu telefono : ")
    correo = input("Introduce tu correo electronico : ")
    #Procesamiento
