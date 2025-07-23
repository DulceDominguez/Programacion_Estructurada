"""

 
 Sets.- 
  Es un tipo de datos para tener una coleccion de valores pero no tiene ni indice ni orden

  Set es una colección desordenada, inmutable* y no indexada. No hay miembros duplicados.
"""
import os
os.system("clear")
#correos=() fila=() email=input("Ingresa el email: ") fila.append(email) correos.append(fila) print(correos)
paises=("Mexico","Brasil","España","Canada")
print(paises)
varios=(True,"UTD",33,3.14)
#Agregar datos:
paises.add("Mexico")
print(paises)
#Eliminar elementos:
paises.pop()#Elimina el ultimo elemento
print(paises)
paises.remove("Mexico")
#Solicitar los email de los alumnos de la UTD alamcenar en una lista y posteriormente mostrar en pantalla
emails=[]
resp="SI"
while resp=="SI":
    emails.append(input("Ingrese su email: "))
    resp=input("Desea agregar otro emial? si/no? ").upper()
email_sets=(emails)
emails=[email_sets]




  



