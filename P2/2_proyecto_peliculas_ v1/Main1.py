#Crear un proyecto que permita gestionar/admisitrar peliculas, colocar un menu de opciones para agregar, borrar, modificar,mostrar, buscar, limpiar una lista de peliculas
#Notas:Utilizar funciones y mandar llamar desde otro archivo
#Nota 2:Utilizar listas para almacenar los nombres de las peliculas 
import Peliculas
opcion=True
while opcion:
    Peliculas.borrarPantalla()
    print("\n\t\t\t.:::Gestion de peliculas:::.\n\t 1.Agregar \n\t 2.Borrar \n\t 3.Modificar \n\t 4.Mostrar \n\t 5.Buscar \n\t 6.Limpiar \n\t 7.Salir")
    opcion=input("\n\t\t Elige una opcion ").upper()
    match opcion:
        case "1":
            Peliculas.agregarPeliculas()
            Peliculas.espereTecla()
        case "2":
            Peliculas.borrarPeliculas()
            Peliculas.espereTecla()
        case "3":
            Peliculas.modificarPeliculas()
            Peliculas.espereTecla()
        case "4":
            Peliculas.mostrarPeliculas()
            Peliculas.espereTecla()
        case "5":
            Peliculas.buscarPeliculas()
            Peliculas.espereTecla()
        case "6":
            Peliculas.limpiarPeliculas()
            Peliculas.espereTecla()
            #Deseas eleiminar la peliculas?
        case "7":
            opcion = False
            Peliculas.borrarPantalla()
            print("\n\tTerminaste la ejecucion del Sistema...Gracias...")
        case _:
            opcion=True
            Peliculas.espereTecla()
            print("\n\tOpcion invalida por favor intente de nuevo ")
    
    