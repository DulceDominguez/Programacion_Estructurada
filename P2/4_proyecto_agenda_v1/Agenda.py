def BorrarPantalla():
    import os
    os.system("cls")

def EspereTecla():
    input("🕒 Presione cualquier tecla para continuar... ")

def MenuPrincipal():
    print("\n\t\t\t ⬜...:: Sistema de gestion de agenda ::...⬜ \n\t 1️⃣.Agregar contactos \n\t 2️⃣.-Mostrar contactos \n\t 3️⃣.-Buscar contactos \n\t 4️⃣.Modificar contactos \n\t 5️⃣.Eliminar contactos \n\t 6.-SALIR \n\t")
    opcion=input("👉 Elije una opcion del 1-6: ")
    return opcion

def AgregarContactos(Agenda):
    print("\n\t.:: Agregar contactos ::.\n")
    nombre=input("Ingrese el nombre: ").upper().strip()
    telefono=input("Ingrese el numero de telefono: ")
    correo=input("Ingrese el correro electronico: ").lower().strip()
    if nombre in Agenda:
        print("⚠️ El contacto ya existe")
    else:
        Agenda[nombre]=[telefono,correo]
        print("\n\t\t::: ✅¡LA OPERACION SE REALIZO CON EXITO! :::")
    EspereTecla()

def MostrarContactos(Agenda):
    print("\n\t.:: Mostrar contactos ::.\n")
    print(f"{'Nombre':^15}{'Telefono':^12}{'Correo':^10}")
    print("-"*40)
    if not(Agenda):
        print("⚠️ No hay contactos en la agenda")
    else:
        for nombre,datos in Agenda.items():
            print(f"{nombre:^15}{datos[0]:^12}{datos[1]:^10}")
            print("-"*40)
    EspereTecla()

def BuscarContacto(Agenda):
    print("\n\t.:: Buscar contactos ::.\n")
    if not(Agenda):
        print("⚠️ No hay contactos en la agenda")
    else:
        contacto=input("Ingrese el nombre del contacto a buscar: ").upper().strip()
        if contacto in Agenda:
            print(f"{'Nombre':^15}{'Telefono':^12}{'Correo':^10}")
            print("-"*40)
            print(f"{contacto:^15}{Agenda[contacto][0]:^12}{Agenda[contacto][1]:^10}")
            print("-"*40)
            #for nombre, datos in Agenda.items(): if nombre==contacto:       
    EspereTecla()

def ModificarContactos2(Agenda):
    #Modificar puede ir con este codigo sin embargo es mas "correcto" hacerlo de manera que modifique todos los valores , 
    #Igual que como se hace en un formulario 
    if not(Agenda):
        print("⚠️ No hay contactos en la agenda ")
    else:
        entro=False
        print("\n\t.:: Modificar contactos ::.\n")
        contacto=input("Ingrese el nombre del contacto: ").upper().strip()
        if contacto in Agenda:
            entro=True
            print(f"{'Nombre':^15}{'Telefono':^12}{'Correo':^10}")
            print("-"*40)
            print(f"{contacto:^15}{Agenda[contacto][0]:^12}{Agenda[contacto][1]:^10}")
            print("-"*40)
        if entro==True:
            valor=input("Ingrese la caracteristica que desea modificar: ").upper().strip()
            while valor!="TELEFONO" and valor!="CORREO":
                print("No se encuentra dicha caracteristica del contacto, solo se puede modificar telefono o correo")
                return
            if valor=="TELEFONO":
                tel=input("Ingrese el valor modificado de telefono: ")
                #Agenda[0]=tel  
                Agenda[contacto][0].update(tel)        
                print("\n\t\t::: ✅¡LA OPERACION SE REALIZO CON EXITO! :::")
            elif valor=="CORREO":
                correo=input("Ingrese el correo modificado: ").lower().strip()
                #Agenda[1]=correo
                Agenda[contacto][1].update(correo)        
                print("\n\t\t::: ✅¡LA OPERACION SE REALIZO CON EXITO! :::")
        elif entro==False:
            print("⚠️ El contacto no se en encuentra en la agenda")
            return
    EspereTecla()

def ModificarContactos(Agenda):
    if not(Agenda):
        print("⚠️ No hay contactos en la agenda ")
    else:
        print("\n\t.:: Modificar contactos ::.\n")
        contacto=input("Ingrese el nombre del contacto: ").upper().strip()
        if contacto in Agenda:
            print("Valores actuales: ")
            print("-"*40)
            print(f"{contacto:^15}{Agenda[contacto][0]:^12}{Agenda[contacto][1]:^10}")
            print(f"Nombre:{contacto}\n Telefono:{Agenda[contacto][0]}\n Correo:{Agenda[contacto][1]}")
            confi=input("Deseas modificar los datos? si/no ").upper().strip()
            while confi!="SI" and confi!="NO":
                confi=input("Deseas modificar los datos? debe contestar solo si/no ").upper().strip()
            if confi=="SI":
                tel=input("Telefono: ")
                correo=input("Correo: ")
                Agenda[contacto]=[tel,correo]
            else:
                return
        else:
            print("⚠️ El contacto no se en encuentra en la agenda")
    EspereTecla()

def BorrarContacto(Agenda):
    if not(Agenda):
        print("⚠️ No hay contactos en la agenda ")

    else:
        if not(Agenda):
            print("⚠️ El contacto no se en encuentra en la agenda")
        else:
            contacto=input("Ingrese el contacto que desea borrar: ").upper().strip()
            conf=input("Desea borrarlo? ").upper().strip()
            if conf=="SI":
                Agenda.pop(contacto)
                print("\n\t\t::: ✅¡LA OPERACION SE REALIZO CON EXITO! :::")
            



