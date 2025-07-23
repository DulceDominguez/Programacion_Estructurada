import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="ejemplo1"
)
cursor=mydb.cursor()
cursor.execute("select * from usuarios")
resultados = cursor.fetchall()
for fila in resultados:
    print(f"ID:{fila[0]}|Nombre: {fila[1]} | Direccion: {fila[2]} ")
