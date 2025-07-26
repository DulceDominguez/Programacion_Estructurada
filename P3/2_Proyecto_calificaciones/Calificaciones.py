import mysql.connector
def BorrarPantalla():
    import os
    os.system("cls")

def EsperarTecla():
    input("Presione cualquier tecla para continuar...")

def MenuPrincipal():
    print("\n\t\t\t .:: Sistema de calificaciones ::. \n\t 1-Agregar \n\t2-Mostrar \n\t 3-Calcular promedios \n\t 4-Buscar \n\t 5-Salir")
    opcion2=input("Ingrese una opcion del 1-5:")
    return opcion2

myconnection=mysql.connector(
    user="root",
    host="localhost",
    password="",
    database="bd_calificaciones"
)

#def Agregar():
    