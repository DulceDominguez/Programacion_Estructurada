import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="ejemplo1"
)
cursor=mydb.cursor()
sql = "UPDATE usuarios SET name= %s WHERE id = %s"
valores = ("Esperanza",1)
cursor.execute(sql, valores)
mydb.commit()

print("Se actualizo correctamente el registro\n")
cursor.execute("select * from usuarios")
resultados = cursor.fetchall()
for fila in resultados:
    print(f"Nombre: {fila[0]} | Direccion: {fila[1]} ")
