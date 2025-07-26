import Calificaciones
Lista=[]
opcion1=True
while opcion1:
    opcion2=Calificaciones.MenuPrincipal()
    match opcion2:
        case "1":
            Calificaciones.Agregar()
            Calificaciones.EsperarTecla()
        case "2":
            Calificaciones.MostrarCalificaciones()
            Calificaciones.EsperarTecla()
        case "3":
            Calificaciones.CalcularPromedios()
            Calificaciones.EsperarTecla()
        case "4":
            Calificaciones.Buscar()
            Calificaciones.EsperarTecla()
        case "5":
            Calificaciones.BorrarPantalla()
            print("Has finalizado el sitema...Gracias...")
            opcion1=False
        case _:
            print("Ingrese una opcion valida por favor")

    

    
