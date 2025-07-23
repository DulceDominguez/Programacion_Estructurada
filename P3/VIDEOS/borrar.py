import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    database="ejemplo"
)
cursor=mydb.cursor()
id_a_borrar = 3
sql = "DELETE FROM metaforas_cosmicas WHERE id = %s"
valores = (id_a_borrar,)
cursor.execute(sql, valores)
mydb.commit()

print(f"Usuario con ID {id_a_borrar} se ha borrado exitosamente")
