import Agenda
def main():
    opcion2=True
    while opcion2:
        opcion1=Agenda.MenuPrincipal()
        match opcion1:
            case "1":
                Agenda.AgregarContactos()
                Agenda.EsperarTecla()
            case "2":
                Agenda.MostrarContactos()
                Agenda.EsperarTecla()
            case "3":
                Agenda.BuscarContactos()
                Agenda.EsperarTecla()
            case "4":
                Agenda.ModificarContactos()
                Agenda.EsperarTecla()
            case "5":
                Agenda.EliminarContactos()
                Agenda.EsperarTecla()
            case "6":
                print("\n\tTerminaste la ejecucion del Sistema...Gracias...")
                opcion2= False
            case _:
                opcion1=True
                print("\n\tOpcion invalida por favor intente de nuevo ")
                Agenda.EspereTecla()

#El guien bajo main no dara error con tal simbolo 
if  __name__=="__main__":
    main()

    
    