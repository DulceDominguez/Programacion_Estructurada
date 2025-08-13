from ConexionDB import *
from mysql.connector import Error
import datetime
import hashlib

def hash_password(Password):
    return hashlib.sha256(Password.encode()).hexdigest()

def AgregarEmpleado(rfc,Nombre,Apellidos,Password):
    try:
        Fecha=datetime.datetime.now()
        Password=hash_password(Password)
        cursor.execute("insert into empleados (RFC,Nombre,Apellidos,Password,fecha) values (%s,%s,%s,%s,%s)",(Nombre,Apellidos,rfc,Password,Fecha))
        conexion.commit()
        respuesta="Correct"
        return respuesta
    except mysql.connector.errors.IntegrityError:
        respuesta="key duplicada"
        return respuesta
    except:
        respuesta=None
        return respuesta
    
    
def Inicio_sesion(rfc,Password):
    try:
        #contrasenia=hash_password(Password)
        cursor.execute("select * from empleados where RFC=%s and Password=%s",(rfc,Password))
        Lista=cursor.fetchone()
        return Lista
    except:
        return []
  




