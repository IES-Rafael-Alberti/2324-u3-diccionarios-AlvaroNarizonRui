"""
Ejercicio 3.2.10¶
Escribir un programa que permita gestionar la base de datos de clientes de una 
empresa. Los clientes se guardarán en un diccionario en el que la clave de cada 
cliente será su NIF, y el valor será otro diccionario con los datos del 
cliente (nombre, dirección, teléfono, correo, preferente), 
donde preferente tendrá el valor True si se trata de un cliente preferente. 
El programa debe preguntar al usuario por una opción del siguiente menú: 
(1) Añadir cliente, (2) Eliminar cliente, (3) Mostrar cliente, 
(4) Listar todos los clientes, (5) Listar clientes preferentes, 
(6) Terminar. En función de la opción elegida el programa tendrá que hacer 
lo siguiente:

1. Preguntar los datos del cliente, crear un diccionario con los datos y añadirlo a la base de datos.
2. Preguntar por el NIF del cliente y eliminar sus datos de la base de datos.
3. Preguntar por el NIF del cliente y mostrar sus datos.
4. Mostrar lista de todos los clientes de la base datos con su NIF y nombre.
5. Mostrar la lista de clientes preferentes de la base de datos con su NIF y nombre.
6. Terminar el programa.
"""

def añadir_cliente(clientes:dict,datos:dict,nif:int,nombre:str,direccion:str,telefono:int,correo:str,preferente):
    datos["nombre"] = nombre
    datos["direccion"] = direccion
    datos["telefono"] = telefono
    datos["correo"] = correo
    datos["preferente"] = preferente
    clientes[nif] = datos

def añadir_cliente_preferente(clientes:dict,clientes_preferentes:dict,nif:int):
    clientes_preferentes[nif] = clientes[nif]

def eliminar_cliente(clientes:dict,clientes_preferentes:dict,nif:int):
    del clientes[nif]
    if nif in clientes_preferentes:
        del clientes_preferentes[nif]

def mostrar_cliente_especifico(clientes:dict,nif:int) -> str:
    datos_cliente = ""
    for i,j in clientes[nif].items():
        datos_cliente += str(i) + " : " + str(j) + "\n"
    return datos_cliente

def mostrar_clientes(clientes:dict) -> str:
    datos_clientes = ""
    for i,j in clientes.items():
        datos_clientes += str(i) + " : " + str(j["nombre"]) + "\n"
    return datos_clientes



if __name__ == "__main__":

    clientes = {}
    clientes_preferentes = {}
    salir = False

    while salir != True:
        eleccion = int(input("Qué desea hacer : \n (1) Añadir Cliente \n (2) Eliminar cliente \n (3) Mostrar cliente \n (4) Listar todos los clientes \n (5) Listar clientes preferentes \n (6) Salir \n Elección : "))
        
        if eleccion == 1:
            datos = {}
            #Entrada
            nif = int(input("Escribe tu NIF : "))
            nombre = input("Escribe tu nombre :")
            direccion = input("Escribe tu dirección : ")
            telefono = int(input("Escribe tu numero de telefono : "))
            correo = input("Escribe tu correo electronico : ")
            preferente = input("Es un cliente preferente (s/n) : ")
            if preferente.lower() == "s":
                preferente = True
                #Procesamiento
                añadir_cliente(clientes,datos,nif,nombre,direccion,telefono,correo,preferente)
                añadir_cliente_preferente(clientes,clientes_preferentes,nif)
            elif preferente.lower() == "n":
                preferente = False
                #Procesamiento
                añadir_cliente(clientes,datos,nif,nombre,direccion,telefono,correo,preferente)           
        
        elif eleccion == 2:
            #Entrada
            nif = int(input("Escribe el NIF del cliente a eliminar : "))
            #Procesamiento
            eliminar_cliente(clientes,clientes_preferentes,nif)
        
        elif eleccion == 3:
            try:
                #Entrada
                nif = int(input("Escribe el NIF del cliente a mostrar : "))
                #Procesamiento
                datos_cliente = mostrar_cliente_especifico(clientes,nif)
                #Salida
                print(f"Datos del cliente {clientes[nif]["nombre"]} \n\n{datos_cliente}")
            except:
                print("No hay ningun usuario registrado en la base de datos")

        elif eleccion == 4:
            #Procesamiento
            datos_clientes = mostrar_clientes(clientes)
            if datos_clientes == "":
                print("Error, no hay ningun usuario en la base de datos")
            else:
                #Salida
                print(f"Clientes almacenados en la base de datos : \n {datos_clientes}")

        elif eleccion == 5:
            #Procesamiento
            datos_clientes_preferentes = mostrar_clientes(clientes_preferentes)
            if datos_clientes_preferentes == "":
                print("Error, no hay registrado ningún cliente preferente.")
            else:
                #Salida
                print(f"Clientes preferentes registrados : \n {datos_clientes_preferentes}")

        elif eleccion == 6:
            print("Hasta otra :) ")
            salir = True
            