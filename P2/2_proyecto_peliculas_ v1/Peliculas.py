peliculas=[]
def borrarPantalla():
    import os
    os.system("cls")

def espereTecla():
    input("\n\t...Oprima cualquier tecla para continuar...")

def agregarPeliculas():
    borrarPantalla()
    print("\n\t.::Agregar Peliculas::.\n")
    peliculas.append(input("Ingrese el nombre de la pelicula: ").upper().strip())#Strip quita espacios
    print("\n\t\t::: ¡LA OPERACION SE REALIZO CON EXITO! :::")#Avisar el usuario que sucedio
    espereTecla()

def borrar2Peliculas():
    print("\n\t.::Borrar Peliculas::.\n")
    peliculas.remove(input("Ingrese el nombre de la pelicula que quiera borrar: ").upper())
    print("\n\t\t::: ¡SE HA ELIMINADO LA PELICULA CON EXITO! :::")
    espereTecla()

def borrarPeliculas():
    encontro=0
    print("\n\t.::Borrar Peliculas::.\n")
    registro=input("Ingrese el nombre de la pelicula que quiera borrar: ").upper().strip()
    while  (registro in  peliculas) :
        for i in range (0,len(peliculas)):
            confirmacion=input("Realmente desea borrar todos los registros de peliculas? si/no").upper().strip()
            while confirmacion=="SI" and confirmacion=="NO":
                confirmacion=input("Realmente desea borrar todos los registros de peliculas? por favor conteste solamente si o no").upper().strip()
            if confirmacion=="SI":
                if not(registro in peliculas):
                    print("\n\t\tLa pelicula no se encuentra en el registro")
                else:
                    peliculas.remove(registro)
                    encontro+=1
                    print(f"\n\t\tLa pelicula {registro} se borro {encontro} veces")


    print("\n\t\t::: ¡SE HA ELIMINADO LA PELICULA CON EXITO! :::")
    espereTecla()

def modificar2Peliculas():
     borrarPantalla()
     print("\n\t.::Modificar Peliculas::.\n")
     posicion=peliculas.index(input("Ingrese el registro que desea modificar: "))
     new=input("Ingrese el registro modificado: ").upper()
     confi=input("Confirma modificar el registro? si/no").upper()
     if confi=="SI":
         peliculas[posicion]=confi
         print("\n\t\t::: ¡SE HA MODIFICADO EL REGISTRO CON EXITO! :::")
     espereTecla()

def modificarPeliculas():
    borrarPantalla()
    print("\n\t.::Modificar Peliculas::.\n")
    registro=input("Ingrese el registro que desea modificar: ")
    if not(registro in peliculas):
        print("\n\t\tLa pelicula no se encuentra en el registro")
    else:
        for i in range (0,len(peliculas)):
            resp=input("Desea actualizar el registro? si/no: ")
            if resp=="SI":
                peliculas[i]=input("Ingrese el registro modificado: ").upper().strip()
                encontro+=1
                print("\n\t\t::: ¡SE HA MODIFICADO EL REGISTRO CON EXITO! :::")
    print("\n\t\t::: ¡SE HA MODIFICADO EL REGISTRO CON EXITO! :::")
    espereTecla() 

def buscarPeliculas():
    borrarPantalla()
    print("\n\t.::Buscar Peliculas::.\n")
    registro=input("Ingrese el registro que desea buscar: ").upper()
    if not(registro in peliculas):
        print("\n\t\tLa pelicula no se encuentra en el registro")
    else:
        for i in range(0,len(peliculas)):
            if registro==peliculas(i):
                print("")
    espereTecla()

def limpiarPeliculas():
    borrarPantalla()
    print("\n\t.::Limpiar todas las Peliculas::.\n")
    confirmacion=input("Realmente desea borrar todos los registros de peliculas? si/no").upper().strip()
    while confirmacion=="SI" and confirmacion=="NO":
        confirmacion=input("Realmente desea borrar todos los registros de peliculas? por favor conteste solamente si o no").upper().strip()

    if confirmacion=="SI":
        print("\n\t\t::: ¡SE HA LIMPIADO PELICULAS CON EXITO! :::")
    espereTecla()

def mostrarPeliculas():
    borrarPantalla()
    print("\n\t.::Mostrar Peliculas::.\n")
    if len(peliculas):
        n=0
        for i in peliculas:
            n=n+1
            print(f"{n}.-{i}")
        espereTecla()
    else :
        print("\n\t\t::: NO SE ENCUENTRA NINGUN REGISTRO :::")
