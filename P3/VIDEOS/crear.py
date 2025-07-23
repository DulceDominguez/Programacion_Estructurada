import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root",
    database="ejemplo"
)
cursor=mydb.cursor()
cursor.execute("create table usuarios (id int auto_increment primary key,nombre varchar (20),direccion varchar (60))")



