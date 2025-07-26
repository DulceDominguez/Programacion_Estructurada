import funciones
from notas import nota
from usuarios import usuario
import getpass

def main():
    opcion=True
    while opcion:
        funciones.borrarPantalla()
        opcion=funciones.menu_usurios()

        if opcion=="1" or opcion=="REGISTRO":
            funciones.borrarPantalla()
            print("\n \t ..:: Registro en el Sistema ::..")
            nombre=input("\t ¿Cual es tu nombre?: ").upper().strip()
            apellidos=input("\t ¿Cuales son tus apellidos?: ").upper().strip()
            email=input("\t Ingresa tu email: ").lower().strip()
            # password=input("\t Ingresa tu contraseña: ").strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo
            resultado=usuario.registrar(nombre,apellidos,email,password)
            if resultado:
                print(f"\n\tSe registro el usuario {nombre} {apellidos} correctamente")
            else:
                print(f"\n\t..No fue posible registrar el usuario en este momento, intentalo mas tarde ...")    
            funciones.esperarTecla()
        elif opcion=="2" or opcion=="LOGIN": 
            funciones.borrarPantalla()
            print("\n \t ..:: Inicio de Sesión ::.. ")     
            email=input("\t Ingresa tu E-mail: ").lower().strip()
            password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
            #Agregar codigo 
            lista_usuarios=usuario.inicio_sesion(email,password)
            if len(lista_usuarios)>0:
               menu_notas(lista_usuarios[0],lista_usuarios[1],lista_usuarios[2])
            else:
                print(f"\n\tE-mail y/o contraseña incorrectas por favor verifique ....")
            funciones.esperarTecla()    
        elif opcion=="3" or opcion=="SALIR": 
            print("Termino la Ejecución del Sistema")
            opcion=False
            funciones.esperarTecla()  
        else:
            print("Opcion no valida")
            opcion=True
            funciones.esperarTecla() 

def menu_notas(usuario_id,nombre,apellidos):
    while True:
        funciones.borrarPantalla()
        print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
        opcion=funciones.menu_notas()

        if opcion == '1' or opcion=="CREAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: Crear Nota ::. ")
            titulo=input("\tTitulo: ")
            descripcion=input("\tDescripción: ")
            #Agregar codigo
            respuesta=nota.crear(usuario_id,titulo,descripcion)
            if respuesta :
                print(f"Se creo la nota {titulo} con exito ")
            else:
                print("No se ha podido crear la nota, por favor intente de nuevo")
            funciones.esperarTecla()    
        elif opcion == '2' or opcion=="MOSTRAR":
            funciones.borrarPantalla()
            #Agregar codigo 
            Lista_Notas=nota.Mostrar(usuario_id)
            if len(Lista_Notas)>0:
                print(f"{'ID':^10}{'Usuario':^15}{'Titulo':^15}{'Descripcion':^15}{'Fecha':^15}")
                print(f"-"*80)
                for fila in Lista_Notas:
                    print(f"{fila[0]:^10}{fila[1]:^15}{fila[2]:^15}{fila[3]:^15} {str(fila[4]):^15}")
                    print(f"-"*80)
            else:
                print("No hay notas para este usuario")
            funciones.esperarTecla()
        elif opcion == '3' or opcion=="CAMBIAR":
            funciones.borrarPantalla()
            Lista_Notas=nota.Mostrar(usuario_id)
            if len(Lista_Notas)>0:
                print(f"{'ID':^10}{'Usuario':^15}{'Titulo':^15}{'Descripcion':^15}{'Fecha':^15}")
                print(f"-"*80)
                for fila in Lista_Notas:
                    print(f"{fila[0]:^10}{fila[1]:^15}{fila[2]:^15}{fila[3]:^15} {str(fila[4]):^15}")
                    print(f"-"*80)
                resp=input("Deseas modificar alguna nota? si/no: ").strip().upper()
                if resp=="SI":
                    print(f"\n \t .:: {nombre} {apellidos}, vamos a modificar un Nota ::. \n")
                    id = input("\t \t ID de la nota a actualizar: ")
                    titulo = input("\t Nuevo título: ")
                    descripcion = input("\t Nueva descripción: ")
                    respuesta=nota.Modificar(id,titulo,descripcion)
                    if respuesta:
                        print("Se modifico los campos de la nota con exito")
                    else:
                        print("No se logro modificar los campos de la nota con exito ")
                if resp=="NO":
                    return
                #Agregar codigo
            funciones.esperarTecla()      
        elif opcion == '4' or opcion=="ELIMINAR":
            funciones.borrarPantalla()
            Lista_Notas=nota.Mostrar(usuario_id)
            if len(Lista_Notas)>0:
                print(f"{'ID':^10}{'Usuario':^15}{'Titulo':^15}{'Descripcion':^15}{'Fecha':^15}")
                print(f"-"*80)
                for fila in Lista_Notas:
                    print(f"{fila[0]:^10}{fila[1]:^15}{fila[2]:^15}{fila[3]:^15} {str(fila[4]):^15}")
                    print(f"-"*80)
                resp=input("Deseas eliminar alguna nota? si/no: ").strip().upper()
            if resp=="SI":
                    print(f"\n \t .:: {nombre} {apellidos}, vamos a eliminar un Nota ::. \n")
                    id = input("\t \t ID de la nota a eliminar: ")
                    respuesta=nota.Eliminar(id)
                    if respuesta:
                        print("Se elimino la nota con exito")
                    else:
                        print("No se logro eliminar la nota con exito ")
            if resp=="NO":
                return
            funciones.esperarTecla()

        elif opcion=='5' or opcion=="BUSCAR":
            funciones.borrarPantalla()
            print(f"\n \t .:: {nombre} {apellidos}, vamos a buscar un Nota ::. \n")
            id = input("\t \t ID de la nota a buscar: ")
            resp=nota.Buscar(usuario_id,id)
            if resp==True:
                Lista_Notas=nota.Mostrar2(usuario_id,id)
                if len(Lista_Notas)>0:
                    print(f"{'ID':^10}{'Usuario':^15}{'Titulo':^15}{'Descripcion':^15}{'Fecha':^15}")
                    print(f"-"*80)
                    for fila in Lista_Notas:
                        print(f"{fila[0]:^10}{fila[1]:^15}{fila[2]:^15}{fila[3]:^15} {str(fila[4]):^15}")
                        print(f"-"*80)
            elif resp==False:
                print("No se encontro la nota ")
            funciones.esperarTecla()

        elif opcion == '6' or opcion=="SALIR":
            break
        else:
            print("\n \t \t Opción no válida. Intenta de nuevo.")
            funciones.esperarTecla()

if __name__ == "__main__":
    main()    


