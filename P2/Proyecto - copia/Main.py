import Dulces
def main():
    Inventario={}
    n=0
    continua=True
    while continua:
        opcion=Dulces.MenuPrincipal()
        match opcion:
            case "1":
                n=n+1
                Dulces.BorrarPantalla()
                Dulces.AgregarRegistro(Inventario,n)
            case "2":
                Dulces.BorrarPantalla()
                Dulces.MostrarInventario(Inventario)
            case "3":
                Dulces.BorrarPantalla()
                Dulces.ModificarRegistros(Inventario)
            case "4":
                #Dulces.BorrarPantalla()
                Dulces.BuscarRegistros(Inventario)
            case "5":
                Dulces.BorrarPantalla()
                Dulces.BorrarRegistros(Inventario)
            case "6":
                continua = False
                Dulces.BorrarPantalla()
                print("\n\t🎉 Terminaste la ejecucion del Sistema...Gracias...")
            case _:
                continua=True
                Dulces.EspereTecla()
                print("\n\t ⚠️ Opcion invalida por favor intenta de nuevo")
if __name__=="__main__":
    main()