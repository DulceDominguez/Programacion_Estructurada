print("EJEMPLO 1")
#Ejemplo 1 Crear una lista de numeros e imprimir el contenido
numeros=[10,20,30,40]
#1ra manera de imprimir listas
print(numeros)
#2da manera de imprimir listas con ciclo for
#3ra manera de imprimir listas con ciclo for pero con 
#4ta manera de imprimir listas con ciclo while 
print("EJEMPLO 2")
#Ejemplo 2 Crear una lista de palabras y posteriormente buscar la coincidencia de una palabra 
materias=["Calculo","Sotenibilidad","Literatura","Programacion"]
palabra=input("Ingrese la palabra a buscar: ")
resu=palabra in materias
#Forma numero uno 
if resu==True:
    print(f"La palabra {palabra} se encuentra en la lista")
else:
    print(f"La palabra {palabra} no se encuentra en la lista")
#Forma numero 2
encontro=False
cuantas=0
for i in materias:
    if i==palabra:
        posiciones=[]
        encontro=True
        cuantas=cuantas+1
        posicion=materias.index(i)
        posiciones.append(posicion)
    else:
        print("No se encontro la palabra")
    if encontro:
        print(f"Se encontro la palabra {cuantas} veces")
        print("La/las")
#Manera numero 3

#Bandera variables que cambian  de estado

print("EJEMPLO 3")
#Ejemplo 3 Añadir elementos a la lista
materias.append("Filosofia")
for i in materias:
    print(i)
#Version profe
op1="SI"
while op1=="SI":
    numeros=[2,4,6,8]
    fila1=[]
    numero=input("Ingrese su telefono: ")
    fila1.append(numero)
    numeros.append(fila)
    for fila in numeros:
        print(fila)
    op1=input("Desea ingresar otro registro de nombre y telefono a la agenda?")
    while op1!="SI" and op1!="NO":
        op1=input("Desea ingresar otro registro de nombre y telefono a la agenda? ").upper()


print("EJEMPLO 4")
#Ejemplo 4 Crear una lista multidimensional que permita almacenar el nombre y telefono de una agenda
lista=[]
op="SI"
while op=="SI":
    fila=[]
    name=input("Ingrese su nombre: ")
    telefono=input("Ingrese su telefono: ")
    fila.append(name)
    fila.append(telefono)
    lista.append(fila)
    for fila in lista:
        print(fila)
    op=input("Desea ingresar otro registro de nombre y telefono a la agenda?")
    while op!="SI" and op!="NO":
        op=input("Desea ingresar otro registro de nombre y telefono a la agenda? ").upper()



