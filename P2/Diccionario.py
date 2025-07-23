inventario={1:{
    "nombre":"Panditas",
    "categoria":"gomitas",},
    2:{
    "nombre":"Bubulubu",
    "categoria":"Chocolate",}
}
Inventario2={}
n=0
while op=="SI":
    n=n+1
    nombre=input("🍬 Ingrese el nombre del producto: ").upper().strip()
    categoria=input("🔖 Ingrese la categoria del producto: ").upper().strip()
    op=input("Deseas agregar otro producto?").upper().strip()
    Inventario2[n]={"nombre": nombre,"categoria": categoria}

print("\n\t\t\t..:: 📄 Mostrar Inventario ::..\n")
print(f"{'ID':^5}{'Nombre':^20}{'Categoria':^14}{'Codigo':^15}{'Precio':^12}{'Cantidad':^12}{'Caducidad':^12}")
print("-"*90)
for id,datos in Inventario2.items():
    print(f"{id:^5}:{datos.get('nombre','N/E'):^20}{datos.get('categoria','N/E'):^14}{datos.get('codigo','N/E'):^15}{datos.get('precio','N/E'):^12}{datos.get('cantidad','N/E'):^12}{datos.get('caducidad','N/E'):^12}")
    print("-"*90)
    
#Eliminar caracteristicas
atributo=input("➡️ Ingrese la caracteristica que desea borrar del registro: ").lower().strip()
del Inventario2[id][atributo]
#Eliminar el registro
id=float(input("➡️ Ingrese el id del producto que desea borrar: "))
Inventario2.pop(id)