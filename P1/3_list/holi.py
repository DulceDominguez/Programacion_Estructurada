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
