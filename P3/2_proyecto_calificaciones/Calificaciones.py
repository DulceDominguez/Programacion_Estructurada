import mysql.connector
from mysql.connector import Error
Calificaciones={}

def BorrarPantalla():
    import os
    os.system("cls")

def EsperarTecla():
    input("🕒 Presione cualquier tecla para continuar... ")

def MenuPrincipal():
    print("\n\t\t\t ⬜...:: Sistema de gestion de agenda ::...⬜ \n\t 1️⃣ -Agregar \n\t 2️⃣ -Mostrar \n\t  3️⃣ -Calcular promedios \n\t 4️⃣ -Buscar \n\t 5️⃣ -Salir")
    opcion2=input("Ingrese una opcion del 1-5:")
    return opcion2
def conexion():
    try:
        myconnection=mysql.connector.connect(
            user="root",
            host="localhost",
            password="",
            database="bd_calificaciones"
        )
        return myconnection
    except Error as e:
        print(f"⚠️ El error que sucedio es: {e}")
        return None

def Agregar():
    BorrarPantalla()
    ConectorBD=conexion()
    cursor=ConectorBD.cursor()
    print("\n\t.::Agregar Calificaciones::.\n")
    Calificaciones.update({"Nombre":input("Ingrese el nombre del alumno: ").upper()})
    conf=True
    while conf:
        try:
            Calificaciones.update({"Calificacion1":float(input("Ingrese la calificacion 1"))})
            Calificaciones.update({"Calificacion2":float(input("Ingrese la calificacion 2"))})
            Calificaciones.update({"Calificacion3":float(input("Ingrese la calificacion 3"))})
            conf=False
        except ValueError:
            print("⚠️ Por favor intente de nuevo debe ingresar un valor numerico")
    #Agregar los datos a la base de datos 
    try:
        sql=("insert into calificaciones (Nombre,Calif1,Calif2,Calif3) values (%s,%s,%s,%s)")
        values=(Calificaciones['Nombre'],Calificaciones['Calificacion1'],Calificaciones['Calificacion2'],Calificaciones['Calificacion3'])
        cursor.execute(sql,values)
        ConectorBD.commit()
        print("✅ Se ha agregado el contacto con exito")
    except Error as e:
        print(f"⚠️ El error que se encontro fue:{e}")
    
def MostrarCalificaciones():
    BorrarPantalla()
    ConectorBD=conexion()
    cursor=ConectorBD.cursor()
    cursor.execute("select * from calificaciones")
    Lista=cursor.fetchall()
    if len(Lista)>0:
        try:
            print("\n\t.::Mostrar Calificaciones::.\n")
            print(f"{'ID':^6}{'Nombre':^15}{'Calif 1':^10}{'Calif 2':^10}{'Calif 3':^10}")
            print("-"*60)
            for fila in Lista:
                print(f"{fila[0]:^6}{fila[1]:^15}{fila[2]:^10}{fila[3]:^10}{fila[4]:^10}")
                print("-"*60)
        except Error as e:
            print(f"⚠️ El error que se encontro fue:{e}")
    else:
        print("⚠️ No hay calificaciones en el sistema")

def Buscar():
    BorrarPantalla()
    ConexionBD=conexion()
    cursor=ConexionBD.cursor()
    print("\n\t.::Buscar Calificaciones::.\n")
    try:
        cursor.execute("select * from calificaciones")
        Lista=cursor.fetchall()
        if len(Lista)>0:
            alumno=input("Ingrese el nombre del alumno que desea buscar:\n ").upper()
            cursor.execute("select * from calificaciones where Nombre=%s",(alumno,))
            Lista2=cursor.fetchall()
            if len(Lista2)>0:
                print(f"{'ID':^6}{'Nombre':^15}{'Calif 1':^10}{'Calif 2':^10}{'Calif 3':^10}")
                print("-"*60)
                for fila in Lista2:
                    print(f"{fila[0]:^6}{fila[1]:^15}{fila[2]:^10}{fila[3]:^10}{fila[4]:^10}")
                    print("-"*60)
            else:
                print("⚠️ No se encontro al alumno en los registros")
        else:
            print("⚠️ No hay calificaciones en el sistema ")
    except Error as e:
        print(f"⚠️ El error que se encontro fue:{e}")
    
def CalcularPromedios():
    BorrarPantalla()
    ConexcionBD=conexion()
    cursor=ConexcionBD.cursor()
    print("\n\t.:: Calcular promedios ::.\n")
    cursor.execute("select * from calificaciones")
    Lista=cursor.fetchall()
    promedio_grupal=0
    promedio_alumno=0
    if len(Lista)>0:
        for fila in Lista:
            nombre=fila[1]
            promedio_alumno=(fila[2]+fila[3]+fila[4])/3
            promedio_grupal=promedio_grupal+promedio_alumno
            print(f"Alumno: {nombre} promedio: {promedio_alumno}")
        promedio_grupal=promedio_grupal/len(Lista)
        print(f"El promedio grupal es: {promedio_grupal}")
    else:
        print("⚠️ No hay calificaciones en el sistema")

