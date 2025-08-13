from ConexionDB import *
from fpdf import FPDF



def AgregarProducto(codigo,Id_empleado,nombre,categoria,precio,unidades,cantidad,caducidad):
    try:
        cursor.execute("insert into inventario (codigo,Id_empleado,nombre,categoria,precio,cantidad_unidades,cantidad_producto,caducidad) values (%s,%s,%s,%s,%s,%s,%s,%s) ",(codigo,Id_empleado,nombre,categoria,precio,unidades,cantidad,caducidad))
        conexion.commit()
        return True
    except:
        return False
    
def MostrarProductos():
    try:
        cursor.execute("select * from inventario")
        Lista=cursor.fetchall()
        return Lista
    except:
        return []
    
def BuscarProductos(codigo):
    try:
        cursor.execute("select * from inventario where codigo=%s",(codigo,))
        Lista=cursor.fetchone()
        return Lista
    except:
        return []
    
def ModificarProducto(Id_empleado,nombre,categoria,precio,unidades,cantidad,caducidad,codigo):
    try:
        cursor.execute("update inventario set Id_empleado=%s,nombre=%s,categoria=%s,precio=%s,cantidad_unidades=%s,cantidad_producto=%s,caducidad=%s where codigo=%s",(Id_empleado,nombre,categoria,precio,unidades,cantidad,caducidad,codigo))
        conexion.commit()
        return True
    except:
        return False

    
def VentaProducto(codigo,cantidad_productos):
    Lista=BuscarProductos(codigo)
    newcantidad=Lista[5]-cantidad_productos
    cursor.execute("update inventario set cantidad_unidades=%s where codigo=%s",(newcantidad,Lista[0]))
    
def BorrarProducto(Codigo):
    try:
        cursor.execute("delete from inventario where codigo=%s",(Codigo,))
        conexion.commit()
        return True
    except:
        return False
