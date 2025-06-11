import sqlite3

# Crear y conectar a la base de datos
conn = sqlite3.connect('electrodomesticos.db')
cursor = conn.cursor()

# Crear tabla de productos si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    categoria TEXT NOT NULL,
    precio REAL NOT NULL,
    stock INTEGER NOT NULL
)
''')
conn.commit()

# Función para insertar productos (ejecuta una sola vez o controla con lógica)
def insertar_productos():
    productos = [
        ("Refrigerador LG", "Línea Blanca", 800.00, 10),
        ("Lavadora Samsung", "Línea Blanca", 650.00, 8),
        ("Televisor Sony 55\"", "TV y Video", 1200.00, 5),
        ("Microondas Panasonic", "Cocina", 220.00, 15),
        ("Aire Acondicionado Mabe", "Climatización", 1500.00, 4)
    ]
    cursor.executemany('''
    INSERT INTO productos (nombre, categoria, precio, stock)
    VALUES (?, ?, ?, ?)''', productos)
    conn.commit()
    print("Productos insertados con éxito.")

# Mostrar el stock de todos los productos
def mostrar_stock():
    print("📦 Stock de Productos:\n")
    cursor.execute('SELECT nombre, categoria, precio, stock FROM productos')
    productos = cursor.fetchall()
    
    if productos:
        for nombre, categoria, precio, stock in productos:
            print(f"- {nombre} | Categoría: {categoria} | Precio: ${precio:.2f} | Stock: {stock} unidades")
    else:
        print("No hay productos en stock.")

# ------- Ejecución del programa -------

# Descomenta esta línea solo la primera vez para insertar datos iniciales
# insertar_productos()

mostrar_stock()

# Cerrar conexión
conn.close()
