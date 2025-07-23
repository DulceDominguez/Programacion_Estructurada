#Crear un proyecto que permita gestionar/admisitrar peliculas, colocar un menu de opciones para agregar, borrar, modificar,mostrar, buscar, limpiar una lista de peliculas
#Notas:Utilizar funciones y mandar llamar desde otro archivo
#Nota 2:Utilizar diccionarios para guardar los atributos de las peliculas nombre,categoria,clasificasion,genero,idioma #Metodo clear(limpiar objeto)
import Peliculas
opcion=True
while opcion:
    Peliculas.borrarPantalla()
    print("\n\t\t\t.:::Gestion de peliculas:::.\n\t 1.Crear \n\t 2.Borrar \n\t 3.Mostrar \n\t 4.Agregar caracteristica \n\t 5.Modificar caracteristica \n\t 6.Borrar caracteristica \n\t 7.Salir")
    opcion=input("\n\t\t Elige una opcion ").upper()
    match opcion:
        case "1":
            Peliculas.crearPelicula()
            Peliculas.espereTecla()
        case "2":
            Peliculas.limpiarPelicula()
            Peliculas.espereTecla()
        case "3":
            Peliculas.mostrarPelicula()
            Peliculas.espereTecla()
        case "4":
            Peliculas.AgregarCaracteristica()
            Peliculas.espereTecla()
        case "5":
            Peliculas.ModificarCaracteristica()
            Peliculas.espereTecla()
        case "6":
            Peliculas.BorrarCaracteristica()
            Peliculas.espereTecla()
            #Deseas eliminar la peliculas?
        case "7":
            opcion = False
            Peliculas.borrarPantalla()
            print("\n\tTerminaste la ejecucion del Sistema...Gracias...")
        case _:
            opcion=True
            Peliculas.espereTecla()
            print("\n\tOpcion invalida por favor intente de nuevo ")
    
    