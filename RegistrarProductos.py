import sqlite3

# Conexión a la base de datos (se crea si no existe)
conn = sqlite3.connect("tienda_electrodomesticos.db")
cursor = conn.cursor()

# Crear tabla si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    categoria TEXT NOT NULL,
    precio REAL NOT NULL,
    stock INTEGER NOT NULL
)
""")
conn.commit()

# Función para registrar un nuevo producto
def registrar_producto():
    nombre = input("Nombre del producto: ")
    categoria = input("Categoría (ej. Refrigerador, Televisor, Lavadora): ")
    try:
        precio = float(input("Precio: "))
        stock = int(input("Cantidad en stock: "))
    except ValueError:
        print("Precio y stock deben ser números.")
        return

    cursor.execute("""
    INSERT INTO productos (nombre, categoria, precio, stock)
    VALUES (?, ?, ?, ?)
    """, (nombre, categoria, precio, stock))
    conn.commit()
    print("✅ Producto registrado exitosamente.")

# Función para listar productos
def listar_productos():
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()

    if productos:
        print("\n📦 Productos registrados:")
        for prod in productos:
            print(f"ID: {prod[0]}, Nombre: {prod[1]}, Categoría: {prod[2]}, Precio: ${prod[3]}, Stock: {prod[4]}")
    else:
        print("❌ No hay productos registrados.")

# Menú simple
def menu():
    while True:
        print("\n=== Tienda de Electrodomésticos ===")
        print("1. Registrar producto")
        print("2. Ver productos")
        print("3. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            registrar_producto()
        elif opcion == "2":
            listar_productos()
        elif opcion == "3":
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# Ejecutar menú
menu()

# Cerrar conexión
conn.close()
