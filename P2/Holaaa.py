def Datos():
    Lista=[]
    sum=0
    continua="SI"
    while continua=="SI":
        continua2=True
        while continua2:
            try:
                num=float(input("Ingresa un numero: "))
                continua2=False
            except ValueError:
                print("Debe ingresar un valor numerico")
        Lista.append(num)
        sum=sum+num
        continua=input("Desea ingresar otro numero?").upper()
        while continua!="SI" and continua!="NO":
            continua=input("Desea ingresar otro numero?").upper()
    print("Los numero ingresados fueron: ")
    for fila in Lista:
        print(fila)
    print(f"La sumatoria fue: {sum}")
Datos()