import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="ejemplo"
)
cursor=mydb.cursor()
sql=("Insert into usuarios (id,nombre,direccion) values (null,%s,%s)")
values=("Jazmin","Domingo Arrieta")
cursor.execute(sql, values)
mydb.commit()
cursor.execute("select * from usuarios")
resultados = cursor.fetchall()
for fila in resultados:
    print(f"ID:{fila[0]}|Nombre: {fila[1]} | Direccion: {fila[2]} ")
