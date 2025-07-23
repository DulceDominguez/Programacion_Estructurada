import Agenda
def main():
    Datos={}
    opcion2=True
    while opcion2:
        opcion1=Agenda.MenuPrincipal()
        match opcion1:
            case "1":
                Agenda.BorrarPantalla()
                Agenda.AgregarContactos(Datos)
            case "2":
                Agenda.BorrarPantalla()
                Agenda.MostrarContactos(Datos)
            case "3":
                Agenda.BorrarPantalla()
                Agenda.BuscarContacto(Datos)
            case "4":
                Agenda.BorrarPantalla()
                Agenda.ModificarContactos(Datos)
            case "5":
                Agenda.BorrarPantalla()
                Agenda.BorrarContacto(Datos)
            case "6":
                opcion1 = False
                print("\n\tTerminaste la ejecucion del Sistema...Gracias...")
            case _:
                opcion1=True
                print("\n\tOpcion invalida por favor intente de nuevo ")
                Agenda.EspereTecla()

#El guien bajo main no dara error con tal simbolo 
if  __name__=="__main__":
    main()

    
    