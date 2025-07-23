peliculas=[]
pelicula={}
def borrarPantalla():
    import os
    os.system("cls")
    
def espereTecla():
    input("\n\t...Oprima cualquier tecla para continuar...")

def crearPelicula():
    borrarPantalla()
    print("\n\t.::Crear atributos de la Pelicula::.\n")
    pelicula.update({"nombre":input("Ingrese el nombre de la pelicula").upper().strip()})
    #pelicula["Nombre"]=input("Ingrese el nombre de la pelicula: ")
    pelicula.update({"categoria":input("Ingrese la categoria de la pelicula").upper().strip()})
    pelicula.update({"clasificasion":input("Ingrese la clasificacion de la pelicula").upper().strip()})
    pelicula.update({"genero":input("Ingrese el genero de la pelicula").upper().strip()})
    pelicula.update({"idioma":input("Ingrese el idioma de la pelicula").upper().strip()})
    print("\n\t\t::: ¡LA OPERACION SE REALIZO CON EXITO! :::")#Avisar el usuario que sucedio

def mostrarPelicula():
    borrarPantalla()
    print("\n\t.::Mostrar atributos de la Pelicula::.\n")
    if len(pelicula)>0:
        for i in pelicula:
            print(f"{i}:{pelicula[i]}")
    else :
        print("\n\t\t::: NO SE ENCUENTRA NINGUN REGISTRO :::")

def limpiarPelicula():
    borrarPantalla()
    print("\n\t.::Limpiar todos los atributos de la Pelicula::.\n")
    if len(pelicula)>0:
        confirmacion=input("Realmente desea borrar todos los atributos de la peliculas? si/no").upper().strip()
        while confirmacion=="SI" and confirmacion=="NO":
         confirmacion=input("Realmente desea borrar todos los atributos de la pelicula? por favor conteste solamente si o no").upper().strip()
        if confirmacion=="SI":
            pelicula.clear
            print("\n\t\t::: ¡SE HAN ELIMINADOS LOS ATRIBUTOS DE LA PELICULA CON EXITO! :::")
        else:
            print("No existen atributos de la pelicula")

def AgregarCaracteristica():
    borrarPantalla()
    print("\n\t.::Agregar atributos de la Pelicula::.\n")
    pelicula.update({input("Ingrese el nombre del atributo que desea agregar: ").lower().strip():input("Ingrese el valor del atributo: ").upper().strip()})
    #El nombre del atributo es como el nombre de una variable asi que debe seguir ciertas caracteristicas y por eso se convierte a minusculas 
    print("\n\t\t::: ¡LA OPERACION SE REALIZO CON EXITO! :::")

def ModificarCaracteristica():
    borrarPantalla()
    print("\n\t.::Modificar atributos de la Pelicula::.\n")
    if len(pelicula)>0:
        for i in pelicula:
            resp=input(f"Desea modificar el valor {pelicula[i]} del atributo {i} de la pelicula? si/no: ").upper().strip()
            while resp!="SI" and resp!="NO":
                    resp=input(f"Desea modificar el valor {pelicula[i]} del atributo {i} de la pelicula? debe responder si/no: ").upper().strip()
            if resp=="SI":
                pelicula.update({i:input(f"Ingrese el valor modificado de {pelicula[i]}").upper().strip()})
                print("\n\t\t::: ¡LA OPERACION SE REALIZO CON EXITO! :::")
    else:
        print("No hay atrobutos de la pelicula")

def BorrarCaracteristica():
     borrarPantalla()
     print("\n\t.::Borrar atributos de la Pelicula::.\n")
     #Borrar el atributo
     for i in pelicula :
         print(f"{i}:{pelicula[i]}")
     atributo=input("Ingrese el atributo que desea borrar: ").lower().strip()
     confirmacion=input("Desea borrar el atributo? ")
     if confirmacion=="SI":
        if  not(atributo in pelicula):
            print("No existe el atributo de la pelicula")
        else:
            pelicula.pop(atributo)
            print("\n\t\t::: ¡LA OPERACION SE REALIZO CON EXITO! :::")

def Borrar2Caracteristica():
     borrarPantalla()
     print("\n\t.::Borrar atributos de la Pelicula::.\n")
     #Borrar el atributo
     atributo=input("Ingrese el atributo que desea borrar: ").lower().strip()
     pelicula.pop(atributo)
     print("\n\t\t::: ¡LA OPERACION SE REALIZO CON EXITO! :::")
     #Borrar solo la clave
     atributo=input("Ingrese el atributo del que desea borrar solo su valor: ").lower().strip()
     pelicula.update({atributo:""})#Puede ser "" o None 
     print("\n\t\t::: ¡LA OPERACION SE REALIZO CON EXITO! :::")

#Union de diccionarios:
#c = a | b   # nuevo dict con la unión de a y b
#a |= b      # actualiza a con b
