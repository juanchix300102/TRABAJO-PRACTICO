import sqlite3

# Conectar o crear la base de datos
conn = sqlite3.connect("tienda_electrodomesticos.db")
cursor = conn.cursor()

# Crear la tabla de productos si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS productos (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    categoria TEXT,
    precio REAL
)
''')

# Insertar productos de ejemplo (solo si la tabla está vacía)
cursor.execute("SELECT COUNT(*) FROM productos")
if cursor.fetchone()[0] == 0:
    productos = [
        ("Heladera Samsung", "Refrigeración", 250000),
        ("Lavarropas LG", "Lavado", 180000),
        ("Microondas BGH", "Cocina", 75000),
        ("Aire acondicionado Philco", "Climatización", 300000),
        ("Televisor Samsung 55''", "TV", 450000)
    ]
    cursor.executemany("INSERT INTO productos (nombre, categoria, precio) VALUES (?, ?, ?)", productos)
    conn.commit()

# Función para buscar productos por nombre o categoría
def buscar_productos(termino_busqueda):
    cursor.execute("SELECT * FROM productos WHERE nombre LIKE ? OR categoria LIKE ?", 
                   (f"%{termino_busqueda}%", f"%{termino_busqueda}%"))
    resultados = cursor.fetchall()
    if resultados:
        print("Resultados encontrados:")
        for producto in resultados:
            print(f"ID: {producto[0]}, Nombre: {producto[1]}, Categoría: {producto[2]}, Precio: ${producto[3]:,.2f}")
    else:
        print("No se encontraron productos con ese término.")

# Interfaz simple
while True:
    print("\n--- BUSCADOR DE PRODUCTOS ---")
    busqueda = input("Ingrese nombre o categoría del producto (o 'salir' para terminar): ")
    if busqueda.lower() == "salir":
        break
    buscar_productos(busqueda)

# Cerrar conexión al final
conn.close()
