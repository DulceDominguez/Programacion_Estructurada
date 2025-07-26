from conexionBD import *
import datetime
def crear(usuario_id,titulo,descripcion):
    try:
        fecha=datetime.datetime.now()
        cursor.execute("insert into notas (usuario_id,titulo,descripcion,fecha) values (%s,%s,%s,%s)",(usuario_id,titulo,descripcion,fecha))
        conexion.commit()
        return True
    except:
        return False 
    
def Mostrar2(usuario_id):
        print("Entro")
        cursor.execute("select * from notas where usuario_id=%s",(usuario_id,))
        print("Entro")
        h=cursor.fetchall()
    
def Mostrar(usuario_id):
    try:
        cursor.execute("select * from notas where usuario_id=%s",(usuario_id,))
        return cursor.fetchall()
    
    except:
        return []

def Mostrar2(usuario_id,id):
    try:
        cursor.execute("select * from notas where usuario_id=%s and id=%s",(usuario_id,id))
        return cursor.fetchall()
    
    except:
        return []
    
    
def Modificar(id,titulo,descripcion):
    try:
        fecha=datetime.datetime.now()
        cursor.execute("update notas set titulo=%s,descripcion=%s,fecha=%s where id=%s",(titulo,descripcion,fecha,id))
        conexion.commit()
        return True
    except:
        return False
    
def Eliminar(id):
    try:
        cursor.execute("Delete from notas where usuario_id=%s ",(id,))
        print("Entro")
        return True
        
    except:
        return False 
    
def Buscar(usuario_id,id):
    try:
        cursor.execute("select * from notas where usuario_id=%s and id=%s",(usuario_id,id))
        lista=cursor.fetchall
        if id!=lista[0]:
            h=False
            return h 
        return True

    except:
        return False
    
def Buscar2(usuario_id,id):
        cursor.execute("select * from notas where usuario_id=%s and id=%s",(usuario_id,id))
        return cursor.fetchall



    
