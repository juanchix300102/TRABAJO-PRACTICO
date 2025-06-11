# Lista de productos (cada uno representa un electrodoméstico)
electrodomesticos = [
    {"id": 1, "nombre": "Refrigerador", "marca": "Samsung", "precio": 1200},
    {"id": 2, "nombre": "Lavadora", "marca": "LG", "precio": 850},
    {"id": 3, "nombre": "Microondas", "marca": "Panasonic", "precio": 300},
    {"id": 4, "nombre": "Aspiradora", "marca": "Philips", "precio": 200}
]

def mostrar_productos():
    print("\nInventario actual:")
    for producto in electrodomesticos:
        print(f"ID: {producto['id']} | {producto['nombre']} - {producto['marca']} | ${producto['precio']}")

def eliminar_producto_por_id(id_producto):
    global electrodomesticos
    original = len(electrodomesticos)
    electrodomesticos = [p for p in electrodomesticos if p["id"] != id_producto]
    if len(electrodomesticos) < original:
        print(f"\n✅ Producto con ID {id_producto} eliminado.")
    else:
        print(f"\n⚠️ No se encontró un producto con ID {id_producto}.")

def eliminar_producto_por_nombre(nombre_producto):
    global electrodomesticos
    original = len(electrodomesticos)
    electrodomesticos = [p for p in electrodomesticos if p["nombre"].lower() != nombre_producto.lower()]
    if len(electrodomesticos) < original:
        print(f"\n✅ Producto '{nombre_producto}' eliminado.")
    else:
        print(f"\n⚠️ No se encontró un producto llamado '{nombre_producto}'.")

# Ejemplo de uso
mostrar_productos()

# Eliminar por ID
eliminar_producto_por_id(2)

# Eliminar por nombre
eliminar_producto_por_nombre("Aspiradora")

# Mostrar productos restantes
mostrar_productos()