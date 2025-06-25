# Proveedores
proveedores = [
    {"id": 1, "nombre": "ElectroDistribuidora S.A."},
    {"id": 2, "nombre": "Mayorista Tech"},
    {"id": 3, "nombre": "Proveedores del Sur"},
]

# Inventario de productos
inventario = [
    {"id": 1, "nombre": "Heladera", "stock": 5},
    {"id": 2, "nombre": "Lavarropas", "stock": 3},
    {"id": 3, "nombre": "Microondas", "stock": 8},
]

# Función para mostrar proveedores
def mostrar_proveedores():
    print("\n📋 Lista de Proveedores:")
    for p in proveedores:
        print(f"{p['id']}: {p['nombre']}")

# Función para mostrar inventario
def mostrar_inventario():
    print("\n📦 Inventario actual:")
    for item in inventario:
        print(f"{item['id']}: {item['nombre']} - Stock: {item['stock']}")

# Función para registrar una compra
def registrar_compra():
    mostrar_proveedores()
    proveedor_id = int(input("Ingrese el ID del proveedor al que va a comprar: "))
    proveedor = next((p for p in proveedores if p["id"] == proveedor_id), None)

    if not proveedor:
        print("❌ Proveedor no encontrado.")
        return

    mostrar_inventario()
    producto_id = int(input("Ingrese el ID del producto que desea comprar: "))
    producto = next((p for p in inventario if p["id"] == producto_id), None)

    if not producto:
        print("❌ Producto no encontrado.")
        return

    cantidad = int(input(f"Ingrese la cantidad de '{producto['nombre']}' a comprar: "))
    producto["stock"] += cantidad

    print(f"\n✅ Compra registrada exitosamente:")
    print
