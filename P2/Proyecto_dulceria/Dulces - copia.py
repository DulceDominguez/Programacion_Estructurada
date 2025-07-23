
def BorrarPantalla():
    import os
    os.system("cls")
def EspereTecla():
    input("\n 🕒 Presione cualquier tecla para continuar: ")

def MenuPrincipal():
    BorrarPantalla()
    print("\n\t\t\t...:: 🍬Bienvenid@ a Dulceria Las peris🍬 ::...")
    print("\n\t 1️⃣ ->📝 Agregar inventario de dulces \n\t 2️⃣ ->📄 Mostrar inventario \n\t 3️⃣ ->🔄 Modififcar registro de inventario \n\t 4️⃣ ->🔍 Buscar productos en inventario \n\t 5️⃣ ->🗑️  Borrar registro de inventario \n\t 6️⃣ ->🚪 SALIR \n\t")
    opcion=input("👉 Ingrese la opcion deseada del 1-4: ")
    return opcion

def AgregarRegistro(Inventario,n):
    from datetime import datetime
    print("\n\t..:: 📝 Agregar Productos ::..\n")
    nombre=input("🍬 Ingrese el nombre del producto: ").upper().strip()
    while nombre=="":
        nombre=input("⚠️ Por favor debe ingresar el nombre del producto: ").upper().strip()
    categoria=input("🔖 Ingrese la categoria del producto: ").upper().strip()
    while categoria=="":
        categoria=input("⚠️ Por favor debe ingresar la categoria del producto: ").upper().strip()
    codigo=input("▍▎▎▍Ingrese el codigo del producto del 8-12 digitos: ").upper().strip()
    while (len(codigo)==0) or (len(codigo)<8 or len(codigo)>12):
        codigo=input("⚠️ Por favor ingrese un codigo valido debe tener de 8-12 caracteres: ").upper().strip()
    continua=True
    while continua:
        try:
            precio=float(input("💲 Ingrese el precio del producto: "))
            continua=False
        except ValueError:
            print(" ⚠️ Por favor ingrese datos numericos en precio ")
    continua2=True
    while continua2:
        try:
            cantidad=float(input("🔢 Ingrese la cantidad de unidades del producto: "))
            continua2=False
        except ValueError:
            print("⚠️ Por favor ingrese datos numericos en cantidad ")
    continua3=True
    while continua3:
        try:
            caducidad=input("📆 Ingrese la caducidad del producto AAAA-MM-DD (ej. 2025-12-01): ").upper().strip()
            fecha = datetime.strptime(caducidad, "%Y-%m-%d")
            hoy = datetime.today()
            if fecha<hoy:
                caducidad="VENCIDO"
            continua3=False
        except ValueError:
                print("⚠️ Por favor ingrese correctamente la fecha AAAA-MM-DD")
    #Lista.append([nombre]+[categoria]+[codigo]+[precio]+[cantidad]+[caducidad])
    #Dicc[codigo[0]] = Registro
    Inventario[n]={"nombre": nombre,"categoria": categoria,"codigo":codigo,"precio":precio,"cantidad":cantidad,"caducidad":caducidad}
    for i in Inventario:
        print(f"{i}:{Inventario[i]}")
    print("\n\t\t::: ✅¡LA OPERACION SE REALIZO CON EXITO! :::")
    EspereTecla()

def MostrarInventario(Inventario):
    if len(Inventario)>0:
        print("\n\t\t\t..:: 📄 Mostrar Inventario ::..\n")
        print(f"{'ID':^5}{'Nombre':^20}{'Categoria':^14}{'Codigo':^15}{'Precio':^12}{'Cantidad':^12}{'Caducidad':^12}")
        print("-"*90)
        for id,datos in Inventario.items():
            print(f"{id:^5}:{datos.get('nombre','N/E'):^20}{datos.get('categoria','N/E'):^14}{datos.get('codigo','N/E'):^15}{datos.get('precio','N/E'):^12}{datos.get('cantidad','N/E'):^12}{datos.get('caducidad','N/E'):^12}")
            print("-"*90)
    else:
        print(" ❌ No hay productos en el inventario")
    EspereTecla()

def ModificarRegistros(Inventario):
    num=0
    print("\n\t..:: 🔄 Modificar Inventario ::..\n")
    if len(Inventario)>0:
        op="SI"
        while op=="SI":
            producto=input("➡️  Ingrese el nombre o categoria delproducto que desea modificar: ").upper().strip()
            print(f"\n👇 Los registros que coinciden con el nombre o categoria {producto} del producto son: \n")
            for id,datos in Inventario.items():
                if (datos["nombre"]==producto or datos["categoria"]==producto):
                    num=num+1
                    print(f"{'ID':^5}{'Nombre':^20}{'Categoria':^14}{'Codigo':^15}{'Precio':^12}{'Cantidad':^12}{'Caducidad':^12}")
                    print("-"*90)
                    print(f"{id:^5}{datos.get('nombre','N/E'):^20}{datos.get('categoria','N/E'):^14}{datos.get('codigo','N/E'):^15}{datos.get('precio','N/E'):^12}{datos.get('cantidad','N/E'):^12}{datos.get('caducidad','N/E'):^12}")
                    print("-"*90)
                    atributo=input("\n➡️  Ingrese el nombre de la caracteristica que desea modificar: ").lower().strip()
                    while atributo=="":
                        atributo=input("\n⚠️ Por favor debe ingresar la caracteristica del regisgro que desea modificar: ").lower().strip()
                    if atributo!="nombre" and atributo!="categoria" and atributo!="codigo" and atributo!="precio" and atributo!="cantidad" and atributo!="caducidad":
                        atributo=input("\n❌ No se encontro la caracteristica del producto en el registro ").lower().strip()
                        return
                    valor_atributo=input("➡️  Ingrese el valor de la caracteristica modificado: ").upper().strip()
                    Inventario[id].update({atributo:valor_atributo})
                    print("\n\t\t::: ✅¡LA OPERACION SE REALIZO CON EXITO! :::")
                    print(f"\n 🔢 La cantidad de registros encontrados fue {num}")
                    return      
                else:
                    print("⚠️ No existe el registro o debe ingresar solo el nombre o categoria del producto")
                    op=input("👉 Desea volver a intentarlo? si/no").upper().strip()
                    while op!="SI" and op!="NO":
                        op=input("⚠️ Intente de nuevo Desea volver a intentarlo? debe responder si/no").upper().strip()
    else:
        print(" ❌ No hay productos en el inventario")
    print(f"La cantidad de registros encontrados fue {num} ")
    EspereTecla()

def BuscarRegistros(Inventario):
    if len(Inventario)>0:
        num=0
        print("\n\t..:: 🔍 Buscar registros de inventario ::..\n")
        producto=input("➡️ Ingrese el nombre o categoria del producto que desea buscar: ").upper().strip()
        for id,datos in Inventario.items():
            id2=str(id)
            if (datos["nombre"]==producto) or (datos["categoria"==producto]):
                num=num+1
                print(f"\n👇Los registros que coinciden con el nombre o categoria {producto} del producto son: \n")
                print(f"{'Nombre':^20}{'Categoria':^14}{'Codigo':^15}{'Precio':^12}{'Cantidad':^12}{'Caducidad':^12}")
                print("-"*90)
                print(f"{datos.get('nombre','N/E'):^20}{datos.get('categoria','N/E'):^14}{datos.get('codigo','N/E'):^15}{datos.get('precio','N/E'):^12}{datos.get('cantidad','N/E'):^12}{datos.get('caducidad','N/E'):^12}")
                print("-"*90)
                print(f"\n 🔢 La cantidad de registros encontrados fue {num}")
            else:
                print("⚠️ No existe el registro o debe ingresar solo el nombre o categoria del producto")
                op=input("👉 Desea volver a intentarlo? si/no").upper().strip()
                while op!="SI" and op!="NO":
                    op=input("⚠️ Intente de nuevo Desea volver a intentarlo? debe responder si/no").upper().strip()
    else:
        print(" ❌ No hay productos en el inventario")
    EspereTecla()

def BorrarRegistros(Inventario):
    print("\n\t\t\t..:: 📛 Opciones de borrar registros de inventario ::..\n\t 1️⃣ ->🗑️ Borrar el registro completo de un prodicto \n\t 2️⃣ ->✂️ Borrar la caracteristica de un registro \n\t 3️⃣ ->🚪 SALIR")
    op=input("👉 Ingrese una opcion de 1-3: ").strip()
    while op!="1" and op!="2" and op!="3":
        op=input("⚠️ Intente de nuevo por favor ingresa una opcion de 1-3: ").strip()
    if len(Inventario)>0:
        if op=="1":
            op2="SI"
            while op2=="SI":
                BorrarPantalla()
                id_in_Inventario=None
                continua=True
                while continua:
                    try:
                        id=float(input("➡️ Ingrese el id del producto que desea borrar: "))
                        continua=False
                    except ValueError:
                            print("⚠️ Por favor intente de nuevo de ingresar un valor numerico en id del producto") 
                for id2,datos in Inventario.items():
                    if id2==id:
                        id_in_Inventario=True
                        print(f"{'ID':<5}{'Nombre':^20}{'Categoria':^14}{'Codigo':^15}{'Precio':^12}{'Cantidad':^12}{'Caducidad':^15}")
                        print("-"*90)
                        print(f"{datos.get('nombre','N/E'):^20}{datos.get('categoria','N/E'):^14}{datos.get('codigo','N/E'):^15}{datos.get('precio','N/E'):^12}{datos.get('cantidad','N/E'):^12}{datos.get('caducidad','N/E'):^12}")
                if id_in_Inventario==True:
                    confirmacion=input("🛑 Estas seguro de borrar el registro del producto con todas sus caracteristicas? ").upper().strip()
                    while confirmacion!="SI" and confirmacion!="NO":
                        confirmacion=input("⚠️ Por favor intenta de nuevo estas seguro de borrar el registro? ").upper().strip()
                    if confirmacion=="SI":
                        Inventario.pop(id)
                        print("\n\t\t::: ✅¡SE HA BORRADO EL REGISTRO CON EXITO! :::")
                    elif confirmacion=="NO":
                        return
                    op2="NO"
                elif id_in_Inventario==None:
                    print("❌ No existe el registro o debe ingresar id del producto")
                    op2=input("➡️ Desea volver a intentarlo? si/no").upper().strip()
                    while op2!="SI" and op2!="NO":
                        op2=input("⚠️ Intente de nuevo Desea volver a intentarlo? debe responder si/no").upper().strip()

        elif op=="2":
            BorrarPantalla()
            id_in_Inventario=None
            continua=True
            while continua:
                try:
                    id=float(input("➡️ Ingrese el id del producto que desea borrar: "))
                    continua=False
                except ValueError:
                        print("⚠️ Por favor intente de nuevo de ingresar un valor numerico en id del producto")
                for id2,datos in Inventario.items():
                    if id2==id:
                        id_in_Inventario=True
                        print(f"{'ID':<5}{'Nombre':^20}{'Categoria':^14}{'Codigo':^15}{'Precio':^12}{'Cantidad':^12}{'Caducidad':^15}")
                        print("-"*90)
                        print(f"{datos.get('nombre','N/E'):^20}{datos.get('categoria','N/E'):^14}{datos.get('codigo','N/E'):^15}{datos.get('precio','N/E'):^12}{datos.get('cantidad','N/E'):^12}{datos.get('caducidad','N/E'):^12}")
                        print("-"*90)
                if id_in_Inventario==True:
                    atributo=input("➡️ Ingrese la caracteristica que desea borrar del registro: ").lower().strip()
                    confirmacion=input("🛑 Estas seguro de borrar la caracteristica del registro? ").upper().strip()
                    while confirmacion!="SI" and confirmacion!="NO":
                        confirmacion=input("⚠️ Por favor intenta de nuevo estas seguro de borrar el registro? ").upper().strip()
                    if confirmacion=="SI":
                        del Inventario[id][atributo]
                        print("\n\t\t::: ✅¡SE HA BORRADO LA CARACTERISTICA DEL REGISTRO CON EXITO! :::")
                    elif confirmacion=="NO":
                        return
                    op2="NO"
                elif id_in_Inventario== None:
                    print("❌ No existe el registro o debe ingresar id del producto")
                    op2=input("➡️ Desea volver a intentarlo? si/no").upper().strip()
                    while op2!="SI" and op2!="NO":
                        op2=input("⚠️ Intente de nuevo Desea volver a intentarlo? debe responder si/no").upper().strip()

        elif op=="3":
            return
    else:
        print(" ❌ No hay productos en el inventario")
    EspereTecla()



