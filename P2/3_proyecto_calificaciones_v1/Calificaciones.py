def BorrarPantalla():
    import os
    os.system("cls")
def EspereTecla():
    print("🕒Presione cualquier tecla para continuar...🕒")

def MenuPrincipal():
    #🟪 ⬜
    print("\n\t\t\t ⬜...:: Sistema de gestion de calificaciones ::...⬜ \n\t 1️⃣.Agregar \n\t 2️⃣.-Mostrar \n\t 3️⃣.-Calcular promedios \n\t 4️⃣.Buscar  \n\t 5️⃣.-SALIR \n\t")
    opcion=input("👉 Elije una opcion del 1-4: ")
    return opcion

def Agregar(Lista):
    print("\n\t.:: Agregar calificaciones ::.\n")
    nombre=input("Ingrese el nombre del alumno: ").upper().strip()
    calificaciones=[]
    for i in range(1,4):
        continua=True
        while continua:
            try:
                cal=float(input(f"📝Ingrese la calificacion #{i}: "))
                if cal>=0 and cal<=10:
                    calificaciones.append(cal)
                    continua=False
                else:
                    print("❌ Intente de nuevo ingrese un valor numerico por favor")
            except ValueError:
                print("❌Intente de nuevo ingrese un valor numerico por favor")
    Lista.append([nombre]+calificaciones)
    print("\n\t\t::: ✅¡LA OPERACION SE REALIZO CON EXITO! :::")
    EspereTecla()

def Mostrar(Lista):
    print("\n\t.:: Mostrar calificaciones ::.\n")
    if len(Lista)>0:
        print(f"{'Nombre':<15}{'Calif 1':<10}{'Calif 2':<10}{'Calif 3':<10}")
        print("-"*50)
        for fila in Lista:
            print(f" {fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}")
            print("-"*50)
            cuantos=len(Lista)
        print(f"Son {cuantos} alumnos")
    else:
        print("❌ No hay calificaciones en el sistema")
    EspereTecla()

def Buscar2(Lista):
    nombre=input("Ingrese el nombre: ").upper().strip()
    for fila in Lista:
        if nombre == fila[0]:
            print(f"El alunno :{fila[0]} c1 {fila[1]} c2 {fila[2]}")
        elif not(nombre in Lista):
            print(f"El alumno{nombre} no esta en el registro")

def Buscar(Lista):
    nombre=input("Ingrese el nombre: ").upper().strip()
    for fila in Lista:
        if not(nombre in Lista):
            print(f"El alumno{nombre} no esta en el registro")
        else:
            print(f"El alunno :{fila[0]} c1 {fila[1]} c2 {fila[2]}")

            

def Mos(Lista):
    if len(Lista)>0:
        print(f"{'Nombre':<15}{'Calif 1':<10}{'calf 2':<10}{'calf 3':<10}")
        print("-"*50)
        for fila in Lista:
            print(f"{fila[0]:<15}{fila[1]:<10}{fila[2]:<10}{fila[3]:<10}")
            print("-"*50)
    else:
        print("❌ No hay calificaciones en el sistema")

def promedio():
    print("Promedio de alumnos: ")
    print(f"{'Nombre':<15}{'Calf 1':<10}{'Calf 2':<10}{'Calf 3':<10}")


def CalcularPromedio(Lista):
    print("\n\t.::📝 Promedio de alumnos ::.\n")
    if len(Lista)>0:
        print(f"{'Nombre':<15}{'Promedio':<10}")
        print("-"*40)
        promedio_grupal=0
        for fila in Lista:
            nombre=fila[0]
            promedio=(fila[1]+fila[2]+fila[3])/3
            promedio_grupal=promedio_grupal+promedio
            print(f"{nombre:<15}{promedio:.2f}")
        print("-"*40)
        promedio_grupal=promedio_grupal/len(Lista)
        print(f"📝El promedio del grupo es:{promedio_grupal}")
        EspereTecla()
    else:
        print("❌No hay resgistros en el sistema ")
        #Hacer un subdtring 





#print(f"{'Hola':<10}")  # izquierda
#print(f"{'Hola':^10}")  # centrado
#print(f"{'Hola':>10}")  # derecha

