import Calificaciones
Lista=[]
opcion1=True
while opcion1:
    opcion2=Calificaciones.MenuPrincipal()
    match opcion2:
        case "1":
            Calificaciones.BorrarPantalla()
            Calificaciones.Agregar()
        case "2":
            Calificaciones.BorrarPantalla()
            Calificaciones.Mostrar()
        case "3":
            Calificaciones.BorrarPantalla()
            Calificaciones.CalcularPromedios()
        case "4":
            Calificaciones.BorrarPantalla()
            Calificaciones.Buscar()
        case "5":
            Calificaciones.BorrarPantalla()
            print("Has finalizado el sitema...Gracias...")
            opcion1=False
        case _:
            print("Ingrese una opcion valida por favor")

    

    
