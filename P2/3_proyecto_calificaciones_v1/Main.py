import Calificaciones
def main():
    Datos=[]
    opcion2=True
    while opcion2:
        opcion1=Calificaciones.MenuPrincipal()
        match opcion1:
            case "1":
                Calificaciones.BorrarPantalla()
                Calificaciones.Agregar(Datos)
            case "2":
                Calificaciones.BorrarPantalla()
                Calificaciones.Mostrar(Datos)
            case "3":
                Calificaciones.BorrarPantalla()
                Calificaciones.CalcularPromedio(Datos)
            case "4":
               # Calificaciones.BorrarPantalla()
                Calificaciones.Buscar2(Datos)
            case "7":
                opcion1 = False
                print("\n\tTerminaste la ejecucion del Sistema...Gracias...")
            case _:
                opcion1=True
                print("\n\tOpcion invalida por favor intente de nuevo ")
                Calificaciones.EspereTecla()

#El guien bajo main no dara error con tal simbolo 
if  __name__=="__main__":
    main()

    
    