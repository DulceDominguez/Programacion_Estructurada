inventario={1:{
    "nombre":"Panditas",
    "categoria":"gomitas",},
    2:{
    "nombre":"Bubulubu",
    "categoria":"Chocolate",}
}

datos = {
    "persona": {
        "nombre": "Dulce",
        "edad": 18,
        "contacto": {
            "email": "dulce@example.com",
            "teléfono": "123-456-7890"
        }
    },
    "lenguajes": ["Python", "R", "Bash"]
}

def recorrer_diccionario(dic, nivel=0):
    for clave, valor in dic.items():
        sangría = "  " * nivel
        if isinstance(valor, dict):
            print(f"{sangría}{clave}:")
            recorrer_diccionario(valor, nivel + 1)
        else:
            print(f"{sangría}{clave}: {valor}")
recorrer_diccionario(datos)