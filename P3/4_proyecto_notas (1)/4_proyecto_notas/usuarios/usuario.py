from conexionBD import *
import datetime
def Registrar(nombre,apellidos,email,contrasena):
    try:
        fecha=datetime.datetime.now()
        cursor.execute("insert into usuarios (nombre,apellidos,email,password,fecha) values (%s,%s,%s,%s,%s",nombre,apellidos,email,contrasena,fecha)
        conexion.commit()
        return True

    except:
        return False 
    
def InicioDeSesion(email,contrasena):
    try:
        cursor.execute("select * from usuarios where email=%s and password=%s",email,contrasena)
        Lista=cursor.fetchone()
        if len(Lista)>0:
            return Lista

        else:
            return []
        return True
    except:
        return []
