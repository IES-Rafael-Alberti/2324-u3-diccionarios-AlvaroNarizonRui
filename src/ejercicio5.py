"""Ejercicio 3.2.5¶
Escribir un programa que almacene el diccionario con 
los créditos de las asignaturas de un curso 
{'Matemáticas': 6, 'Física': 4, 'Química': 5} 
y después muestre por pantalla los créditos de 
cada asignatura en el formato <asignatura> 
tiene <créditos> créditos, 
donde <asignatura> es cada una 
de las asignaturas del curso, 
y <créditos> son sus créditos. 
Al final debe mostrar también el número 
total de créditos del curso."""

def calcular_creditos(asignaturas:dict) -> int:
    sumatoria = 0
    for i in asignaturas.values():
        sumatoria += i
    return sumatoria


if __name__ == "__main__":
    asignaturas = {'Matemáticas': 6, 'Física': 4, 'Química': 5}
    #Procesamiento
    total_creditos = calcular_creditos(asignaturas)
    #Salida
    for i, j in asignaturas.items():
        print(f"La asignatura {i} tiene {j} créditos")
    print(f"El total de créditos del curso : {total_creditos}")