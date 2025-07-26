import mysql.connector
from mysql.connector import Error
Agenda={}

def BorrarPantalla():
    import os
    os.system("cls")

def EsperarTecla():
    input("🕒 Presione cualquier tecla para continuar... ")

def conexion():
    try:
        myconnect=mysql.connector.connect(
            user="root",
            host="localhost",
            password="",
            database="bd_agenda"
        )
        return myconnect
    except Error as e:
        print(f"⚠️ El error que se encontro fue:{e}")
        return None

def MenuPrincipal():
    BorrarPantalla()
    print("\n\t\t\t ⬜...:: Sistema de gestion de agenda ::...⬜ \n\t 1️⃣ .Agregar contactos \n\t 2️⃣ .-Mostrar contactos \n\t 3️⃣ .-Buscar contactos \n\t 4️⃣ .Modificar contactos \n\t 5️⃣ .Eliminar contactos \n\t 6.-SALIR \n\t")
    opcion=input("👉 Elije una opcion del 1-6: ")
    return opcion

def AgregarContactos():
    BorrarPantalla()
    ConectorBD=conexion()
    cursor=ConectorBD.cursor()
    print("\n\t.:: Agregar Contactos ::.\n")
    Agenda.update({"Nombre":input("Ingrese el nombre del contacto: ").upper()})
    Agenda.update({"Telefono":input("Ingrese el numero telefonico: ")})
    Agenda.update({"Correo":input("Ingrese el correo electronico: ")})
    #Agregar los datos a la base de datos 
    try:
        sql=("insert into agenda (Nombre,Telefono,Correo) values (%s,%s,%s)")
        values=(Agenda['Nombre'],Agenda['Telefono'],Agenda['Correo'])
        cursor.execute(sql,values)
        ConectorBD.commit()
        print("✅ Se ha agregado el contacto con exito")
    except Error as e:
        print(f"⚠️ El error que se encontro fue:{e}")
    
def MostrarContactos():
    BorrarPantalla()
    ConectorBD=conexion()
    cursor=ConectorBD.cursor()
    cursor.execute("select * from agenda")
    Lista=cursor.fetchall()
    if len(Lista)>0:
        try:
            print("\n\t.:: Mostrar Contactos ::.\n")
            print(f"{'ID':^6}{'Nombre':^15}{'Telefono':^15}{'Correo':^15}")
            print("-"*60)
            for fila in Lista:
                print(f"{fila[0]:^6}{fila[1]:^15}{fila[2]:^15}{fila[3]:^15}")
                print("-"*60)
        except Error as e:
            print(f"⚠️ El error que se encontro fue:{e}")
    else:
        print("⚠️ No hay contactos en el sistema")

def BuscarContactos():
    BorrarPantalla()
    ConexionBD=conexion()
    cursor=ConexionBD.cursor()
    print("\n\t.:: Buscar Contactos ::.\n")
    try:
        cursor.execute("select * from agenda")
        Lista=cursor.fetchall()
        if len(Lista)>0:
            contacto=input("Ingrese el nombre del contacto que desea buscar: ").upper()
            cursor.execute("select * from agenda where Nombre=%s",(contacto,))
            Lista2=cursor.fetchall()
            if len(Lista2)>0:
                print(f"\n{'ID':^6}{'Nombre':^15}{'Telefono':^15}{'Correo':^15}")
                print("-"*60)
                for fila in Lista2:
                    print(f"{fila[0]:^6}{fila[1]:^15}{fila[2]:^15}{fila[3]:^15}")
                    print("-"*60)
            else:
                print("⚠️ No se encontro el contanto en los registros")
        else:
            print("⚠️ No hay contactos en el sistema ")
    except Error as e:
        print(f"El error que se encontro fue:{e}")

def ModificarContactos():
    BorrarPantalla()
    ConexionBD=conexion()
    cursor=ConexionBD.cursor()
    try:
        cursor.execute("select * from agenda")
        Lista=cursor.fetchall()
        if len(Lista)>0:
            print("\n\t.:: Modificar Contactos ::.\n")
            contacto=input("Ingrese el nombre del contacto que desea modificar: ").upper()
            cursor.execute("select * from agenda where Nombre=%s",(contacto,))
            Lista2=cursor.fetchall()
            if len(Lista2)>0:
                print(f"\n{'ID':^6}{'Nombre':^15}{'Telefono':^15}{'Correo':^15}")
                print("-"*60)
                for fila in Lista2:
                    print(f"{fila[0]:^6}{fila[1]:^15}{fila[2]:^15}{fila[3]:^15}")
                    print("-"*60)
                conf=input("Confirma que desea modificar datos del registro?si/no: ").upper()
                while conf!="SI" and conf!="NO":
                    conf=input("Por favor intente de nuevo \n Confirma que desea modificar datos del registro? DEBE CONTESTAR SI/NO: ").upper()
                if conf=="SI":
                    Nombre=input("Ingrese el nombre del contacto: ").upper()
                    Agenda.update({"Nombre":Nombre})
                    conf=True
                    while conf:
                        try:
                            Telefono=float(input("Ingrese el numero telefonico: "))
                            Agenda.update({"Telefono":Telefono})
                            conf=False
                        except ValueError:
                            print("Por favor intente de nuevo debe ingresar valores numericos")
                    Correo=input("Ingrese el correo electronico: ")
                    Agenda.update({"Correo":Correo})
                    cursor.execute("update agenda set Nombre=%s,Telefono=%s,Correo=%s where Nombre=%s",(Nombre,Telefono,Correo,contacto))
                    ConexionBD.commit()
                    print("✅ Se ha modificado el contacto con exito")
            else:
                print("⚠️ No se encontro el contacto")  
        else:
            print("⚠️ No hay contactos en el sistema")

    except Error as e:
        print(f"⚠️ El error que se encontro fue:{e}")


def EliminarContactos():
    BorrarPantalla()
    ConexionBD=conexion()
    cursor=ConexionBD.cursor()
    try:
        cursor.execute("select * from agenda")
        Lista=cursor.fetchall()
        if len(Lista)>0:
            print("\n\t.:: Eliminar Contactos ::.\n")
            contacto=input("Ingrese el nombre del contacto que desea eliminar: ").upper()
            cursor.execute("select * from agenda where Nombre=%s",(contacto,))
            Lista2=cursor.fetchall()
            if len(Lista2)>0:
                print(f"\n{'ID':^6}{'Nombre':^15}{'Telefono':^15}{'Correo':^15}")
                print("-"*60)
                for fila in Lista2:
                    print(f"{fila[0]:^6}{fila[1]:^15}{fila[2]:^15}{fila[3]:^15}")
                    print("-"*60)
                conf=input("Confirma que desea eliminar el registro?si/no: ").upper()
                while conf!="SI" and conf!="NO":
                    conf=input("Por favor intente de nuevo \n Confirma que desea eliminar el registro? DEBE CONTESTAR SI/NO: ").upper()
                if conf=="SI":
                    cursor.execute("delete from agenda where Nombre=%s",(contacto,))
                    ConexionBD.commit()
                    print("✅ Se ha eliminado el contacto con exito")
            else:
                print("⚠️ No se encontro el contacto")  
        else:
            print("⚠️ No hay contactos en el sistema")

    except Error as e:
        print(f"⚠️ El error que se encontro fue:{e}")





