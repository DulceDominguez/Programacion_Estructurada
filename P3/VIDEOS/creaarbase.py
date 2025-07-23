#pip install mysql-connector-python
import mysql.connector

mydb=mysql.connector.connect(
    host="localhost",
    user="root"
)

cursor=mydb.cursor()
cursor.execute("create database ejemplo")
print("Se creo correctamente la base de datos")
