# Lista de productos simulando una base de datos
productos = [
    {"id": 1, "nombre": "Heladera", "marca": "Samsung", "precio": 250000},
    {"id": 2, "nombre": "Lavarropas", "marca": "LG", "precio": 200000},
    {"id": 3, "nombre": "Microondas", "marca": "Philips", "precio": 85000},
    {"id": 4, "nombre": "Aire Acondicionado", "marca": "Whirlpool", "precio": 300000},
    {"id": 5, "nombre": "Televisor", "marca": "Sony", "precio": 270000},
]

# Función para buscar productos por nombre o marca
def buscar_producto(busqueda):
    encontrados = []
    for producto in productos:
        if (busqueda.lower() in producto["nombre"].lower()) or (busqueda.lower() in producto["marca"].lower()):
            encontrados.append(producto)
    return encontrados

# Menú de búsqueda
def menu_busqueda():
    while True:
        print("\n🔎 Buscar productos en la tienda de electrodomésticos")
        termino = input("Ingrese el nombre o marca del producto a buscar (o escriba 'salir' para terminar): ")

        if termino.lower() == "salir":
            print("👋 Gracias por usar la tienda. ¡Hasta luego!")
            break

        resultados = buscar_producto(termino)

        if resultados:
            print("\n✅ Productos encontrados:")
            for p in resultados:
                print(f"ID: {p['id']} | Nombre: {p['nombre']} | Marca: {p['marca']} | Precio: ${p['precio']}")
        else:
            print("❌ No se encontraron productos con ese nombre o marca.")

# Ejecutar el menú
menu_busqueda()
