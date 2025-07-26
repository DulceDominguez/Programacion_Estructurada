#Crear un proyecto que permita gestionar/admisitrar peliculas, colocar un menu de opciones para agregar, borrar, modificar,mostrar, buscar, limpiar una lista de peliculas
#Notas:Utilizar funciones y mandar llamar desde otro archivo
#Nota 2:Utilizar diccionarios para guardar los atributos de las peliculas nombre,categoria,clasificasion,genero,idioma #Metodo clear(limpiar objeto)
import Peliculas
opcion=True
while opcion:
    Peliculas.borrarPantalla()
    print("\n\t\t\t.:::Implementar y utiliza una base de datos relacional:::.\n\t 1.Agregar \n\t 2.Mostrar \n\t 3.Buscar \n\t 4.Modificar Peliculas \n\t 5.Borrar Peliculas\n\t 6.Salir")
    opcion=input("\n\t\t Elige una opcion ").upper()
    match opcion:
        case "1":
            Peliculas.AgregarPelicula()
            Peliculas.espereTecla()
        case "2":
            Peliculas.MostrarPeliculas()
            Peliculas.espereTecla()
        case "3":
            Peliculas.BuscarPeliculas()
            Peliculas.espereTecla()
        case "4":
            Peliculas.ModificarPeliculas()
            Peliculas.espereTecla()
        case "5":
            Peliculas.BorrarPeliculas()
            Peliculas.espereTecla()
        case "6":
            opcion = False
            Peliculas.borrarPantalla()
            print("\n\tTerminaste la ejecucion del Sistema...Gracias...")
        case _:
            opcion=True
            Peliculas.espereTecla()
            print("\n\tOpcion invalida por favor intente de nuevo ")
    
    