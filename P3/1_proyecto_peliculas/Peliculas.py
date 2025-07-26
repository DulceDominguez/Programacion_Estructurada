import mysql.connector
from mysql.connector import Error
#dict u objeto para almacenar los atributos (nombre, categoria, clasificacion, genero, idioma)

# pelicula={
#             "nombre":"",
#             "categoria":"",
#             "clasificacion":"",
#             "genero":"",
#             "idioma":""
#           }

peliculas={}
def Conectar():
    try:
        Conexion=mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="bd_peliculas"
        )
        return Conexion
    except Error as e:
        print(f"El error que sucedio es: {e}")
        return None
    
def borrarPantalla():
    import os
    os.system("cls")
    
def espereTecla():
    input("\n\t...Oprima cualquier tecla para continuar...")

def AgregarPelicula():
    borrarPantalla()
    ConexionBD=Conectar()
    print("Heyy")
    if ConexionBD!=None:
        print("\n\t.::Crear atributos de la Pelicula::.\n")
        peliculas.update({"nombre":input("Ingrese el nombre de la pelicula: ").upper().strip()})
        #pelicula["Nombre"]=input("Ingrese el nombre de la pelicula: ")
        peliculas.update({"categoria":input("Ingrese la categoria de la pelicula: ").upper().strip()})
        peliculas.update({"clasificasion":input("Ingrese la clasificacion de la pelicula: ").upper().strip()})
        peliculas.update({"genero":input("Ingrese el genero de la pelicula: ").upper().strip()})
        peliculas.update({"idioma":input("Ingrese el idioma de la pelicula: ").upper().strip()})
        #Agregar datos a base de datos 
        try:
            cursor=ConexionBD.cursor()
            sql=("insert into peliculas (nombre,categoria,clasificasion,genero,idioma) values(%s,%s,%s,%s,%s)")
            values=(peliculas['nombre'],peliculas['categoria'],peliculas['clasificasion'],peliculas['genero'],peliculas['idioma'])
            cursor.execute(sql,values)
            ConexionBD.commit()
        except Error as e:
            print(f"El error que se encontro fue:{e}")

def MostrarPeliculas():
   borrarPantalla()
   conexionBD=Conectar()
   if conexionBD!=None:
     print("\n\t.:: Mostrar las Peliculas ::.\n ")
     cursor=conexionBD.cursor()
     sql="select * from peliculas"
     cursor.execute(sql)
     registros=cursor.fetchall()
     if registros:
       print(f"\n\tMostrar las Peliculas")
       print(f"{'ID':^6}{'Nombre':^20}{'Categoria':^23}{'Clasificasión':^15}{'Genero':^18}{'Idioma':^10}")
       print(f"-"*93)
       for fila in registros:
         print(f"{fila[0]:^6}{fila[1]:^20}{fila[2]:^23}{fila[3]:^15}{fila[4]:^18}{fila[5]:^10}")
         print(f"-"*93)  
     else:
       print("\t .:: No hay peliculas en el sistema ::.")
    
def BorrarPeliculas():
    borrarPantalla()
    ConexionBD=Conectar()
    if ConexionBD!=None:
        nombre=input("Ingrese el nombre de la pelcula que desea eliminar: ").strip().upper()
        cursor=ConexionBD.cursor()
        sql=("select * from peliculas where nombre=%s")
        value=(nombre,)
        cursor.execute(sql,value)
        registros=cursor.fetchall()
        if registros:
            print(f"{'ID':^6}{'Nombre':^20}{'Categoria':^23}{'Clasificasión':^15}{'Genero':^18}{'Idioma':^10}")
            print(f"-"*93)
            for fila in registros:
                print(f"{fila[0]:^6}{fila[1]:^20}{fila[2]:^23}{fila[3]:^15}{fila[4]:^18}{fila[5]:^10}")
                print(f"-"*93)  
        confi=input("Desea eliminar el registro? si/no:").strip().upper()
        if confi=="SI":
            sql2=("Delete from peliculas where nombre=%s")
            value2=(nombre,)
            cursor.execute(sql2,value2)
            ConexionBD.commit()
            print("Se ha eliminado correctamente el registro")
        else:
            return


def MostrarPeliculas2():
    borrarPantalla()
    ConexionBD=Conectar()
    if ConexionBD!=None:
        cursor=mysql.connector.cursor()
        sql=("select * from peliculas")
        cursor.execute(sql)
        registros=cursor.fetchall()
        if registros:
            print(F"{'ID':<10},{'Nombre':<10},{'Categoria':<10},{'Clasificasion':<10},{'Genero':<10},{'Idioma':<10}")
            for pelis in registros:
                print(f"{peliculas[0]:^10},{peliculas[1]:^15},{peliculas[2]:^15},{peliculas[3]:^15},{peliculas[4]:^15},{peliculas[5]:^15}")

def BuscarPeliculas():
    borrarPantalla()
    ConexionBD=Conectar()
    if ConexionBD!=None:
        nombre=input("Ingrese el nombre de la pelcula que desea buscar: ").strip().upper()
        cursor=ConexionBD.cursor()
        sql=("select * from peliculas where nombre=%s")
        value=(nombre,)
        cursor.execute(sql,value)
        registros=cursor.fetchall()
        if registros:
            print(f"\n\tMostrar las Peliculas")
            print(f"{'ID':^6}{'Nombre':^20}{'Categoria':^23}{'Clasificasión':^15}{'Genero':^18}{'Idioma':^10}")
            print(f"-"*93)
            for fila in registros:
                print(f"{fila[0]:^6}{fila[1]:^20}{fila[2]:^23}{fila[3]:^15}{fila[4]:^18}{fila[5]:^10}")
            print(f"-"*93) 
    
def ModificarPeliculas():
    borrarPantalla()
    ConexionBD=Conectar()
    if ConexionBD!=None:
        nombre=input("Ingrese el nombre de la pelicula que desea actualizar: ").strip().upper()
        cursor=ConexionBD.cursor()
        sql=("select * from peliculas where nombre=%s")
        value=(nombre,)
        cursor.execute(sql,value)
        registros=cursor.fetchall()
        if registros:
            print(f"{'ID':^6}{'Nombre':^20}{'Categoria':^23}{'Clasificasión':^15}{'Genero':^18}{'Idioma':^10}")
            print(f"-"*93)
            for fila in registros:
                print(f"{fila[0]:^6}{fila[1]:^20}{fila[2]:^23}{fila[3]:^15}{fila[4]:^18}{fila[5]:^10}")
                print(f"-"*93)
        confi=input("Desea modificar el registro? si/no:").strip().upper()
        if confi=="SI":
            peliculas.update({"nombre":input("Ingrese el nombre de la pelicula: ").upper().strip()})
            peliculas.update({"categoria":input("Ingrese la categoria de la pelicula: ").upper().strip()})
            peliculas.update({"clasificasion":input("Ingrese la clasificasion de la pelicula: ").upper().strip()})
            peliculas.update({"genero":input("Ingrese el genero de la pelicula: ").upper().strip()})
            peliculas.update({"idioma":input("Ingrese el idioma de la pelicula: ").upper().strip()})
            #Agregar datos a base de datos 
            sql2=("Update peliculas set nombre=%s,categoria=%s,clasificasion=%s,genero=%s,idioma=%s where nombre=%s")
            values2=(peliculas['nombre'],peliculas['categoria'],peliculas['clasificasion'],peliculas['genero'],peliculas['idioma'],nombre)
            cursor.execute(sql2,values2)
            ConexionBD.commit()
            print("Se ha modificado correctamente el registro")
        else:
            return


def modificarPeliculas2():
    borrarPantalla()
    conexionBD = Conectar()
    if conexionBD is not None:
        cursor = conexionBD.cursor()
        sql = "SELECT * FROM peliculas"
        cursor.execute(sql)
        registros = cursor.fetchall()
        print("\n\t .:: Modificar Películas ::.\n")
        if registros:
            print(f"{'ID':<10}{'Nombre':<15}{'Categoria':<15}{'Clasificación':<15}{'Genero':<15}{'Idioma':<15}")
            print("-" * 80)
            for fila in registros:
                print(f"{fila[0]:<10}{fila[1]:<15}{fila[2]:<15}{fila[3]:<15}{fila[4]:<15}{fila[5]:<15}")
            print("-" * 80)
            try:
                id_modificar = int(input("\nIngrese el ID de la película que desea modificar: "))
                cursor.execute("SELECT * FROM peliculas WHERE id = %s", (id_modificar,))
                pelicula = cursor.fetchall()
                if pelicula:
                    print("\nDeje vacío el campo que no desee modificar.\n")
                    nuevo_nombre = input(f"Nombre ({pelicula[1]}): ") or pelicula[1]
                    nueva_categoria = input(f"Categoría ({pelicula[2]}): ") or pelicula[2]
                    nueva_clasificacion = input(f"Clasificación ({pelicula[3]}): ") or pelicula[3]
                    nuevo_genero = input(f"Género ({pelicula[4]}): ") or pelicula[4]
                    nuevo_idioma = input(f"Idioma ({pelicula[5]}): ") or pelicula[5]
                    sql_update = """
                        UPDATE peliculas 
                        SET nombre=%s, categoria=%s, clasificacion=%s, genero=%s, idioma=%s 
                        WHERE id=%s
                    """
                    datos = (nuevo_nombre, nueva_categoria, nueva_clasificacion, nuevo_genero, nuevo_idioma, id_modificar)
                    cursor.execute(sql_update, datos)
                    conexionBD.commit()
                    print("\n\tPelícula modificada correctamente.\n")
                else:
                    print("\n\tNo se encontró una película con ese ID.\n")
            except Exception as e:
                print(f"\n\tEl error fue: {e}\n")
        else:
            print("\n\t .:: No hay películas en el Sistema ::.\n")


#Union de diccionarios:
#c = a | b   # nuevo dict con la unión de a y b
#a |= b      # actualiza a con b
