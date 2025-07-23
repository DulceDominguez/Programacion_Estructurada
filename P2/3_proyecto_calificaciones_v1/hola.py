import pdb
Lista=[]
nombre=input("Ingrese el nombre del alumno: ").upper().strip()
calificaciones=[]
for i in range(1,4):
    cal=float(input(f"📝Ingrese la calificacion #{i}: "))
    calificaciones.append(cal)
Lista.append([nombre]+calificaciones)
nombre=input("Ingrese el nombre 2 del alumno: ").upper().strip()
calificaciones=[]
for i in range(1,4):
    cal=float(input(f"📝Ingrese la calificacion #{i}: "))
    calificaciones.append(cal)
Lista.append([nombre]+calificaciones)
nombre=input("Ingrese el nombre abuscar : ").upper().strip()
for fila in Lista:
    if not(nombre in Lista):
        pdb.set_trace()
        print(f"El alumno{nombre} no esta en el registro")
    else:
        print(f"El alunno :{fila[0]} c1 {fila[1]} c2 {fila[2]}")
