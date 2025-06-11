# Inventario de productos
productos = [
    {"id": 1, "nombre": "Refrigerador", "marca": "Samsung", "precio": 1200, "stock": 5},
    {"id": 2, "nombre": "Lavadora", "marca": "LG", "precio": 850, "stock": 3},
    {"id": 3, "nombre": "Microondas", "marca": "Panasonic", "precio": 300, "stock": 7},
    {"id": 4, "nombre": "Aspiradora", "marca": "Philips", "precio": 200, "stock": 4}
]

# Lista para registrar ventas
ventas = []

def mostrar_productos():
    print("\n📦 Inventario actual:")
    for p in productos:
        print(f"ID: {p['id']} | {p['nombre']} - {p['marca']} | ${p['precio']} | Stock: {p['stock']}")

def realizar_venta(id_producto, cantidad):
    # Buscar el producto
    for producto in productos:
        if producto["id"] == id_producto:
            if producto["stock"] >= cantidad:
                total = producto["precio"] * cantidad
                producto["stock"] -= cantidad

                venta = {
                    "producto": producto["nombre"],
                    "cantidad": cantidad,
                    "precio_unitario": producto["precio"],
                    "total": total
                }
                ventas.append(venta)
                print(f"\n✅ Venta realizada: {cantidad} x {producto['nombre']} = ${total}")
                return
            else:
                print(f"\n❌ Stock insuficiente. Solo quedan {producto['stock']} unidades.")
                return
    print(f"\n⚠️ Producto con ID {id_producto} no encontrado.")

def mostrar_ventas():
    print("\n🧾 Registro de ventas:")
    if not ventas:
        print("No se han realizado ventas todavía.")
        return
    for idx, venta in enumerate(ventas, start=1):
        print(f"{idx}. {venta['cantidad']} x {venta['producto']} - ${venta['total']}")

# ===============================
# Uso de ejemplo
# ===============================
mostrar_productos()

# Realizar algunas ventas
realizar_venta(1, 2)  # 2 Refrigeradores
realizar_venta(3, 1)  # 1 Microondas
realizar_venta(2, 5)  # Stock insuficiente

mostrar_ventas()
mostrar_productos()