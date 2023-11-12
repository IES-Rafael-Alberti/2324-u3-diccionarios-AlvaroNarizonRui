"""Ejercicio 3.2.4¶
Escribir un programa que pregunte una fecha en formato 
dd/mm/aaaa y muestre por pantalla la misma fecha en formato 
dd de <mes> de aaaa donde <mes> es el nombre del mes."""


def convertidor_meses(mes):
    meses = {"01":"enero","02":"febrero","03":"marzo","04":"abril","05":"mayo","06":"junio","07":"julio","08":"agosto","09":"septiembre","10":"octubre","11":"noviembre","12":"diciembre"}
    if mes in meses:
        return meses[mes]
    else:
        raise ValueError

if __name__ == "__main__":
    try:
        #Entrada
        fecha = input("Introduce una fecha en formato dd/mm/aaaa : ")
        dia, mes, año = fecha.split("/")
        #Procesamiento
        mes_convertido = convertidor_meses(mes)
        #Salida
        print(f"{dia} de {mes_convertido} de {año}")
    except ValueError:
        print("No introdujiste un valor correcto")