import sqlite3
import pandas as pd

# Conexión a la base de datos
conn = sqlite3.connect("tienda_electrodomesticos.db")
cursor = conn.cursor()

# Función para mostrar todos los productos
def reporte_todos_los_productos():
    cursor.execute("SELECT * FROM productos")
    productos = cursor.fetchall()
    print("\n📋 Todos los productos:")
    for p in productos:
        print(f"ID: {p[0]}, Nombre: {p[1]}, Categoría: {p[2]}, Precio: ${p[3]}, Stock: {p[4]}")

# Función para productos sin stock
def reporte_sin_stock():
    cursor.execute("SELECT * FROM productos WHERE stock = 0")
    productos = cursor.fetchall()
    print("\n❌ Productos SIN stock:")
    if productos:
        for p in productos:
            print(f"{p[1]} (Categoría: {p[2]})")
    else:
        print("Todos los productos tienen stock.")

# Función para productos con poco stock
def reporte_stock_bajo(umbral=5):
    cursor.execute("SELECT * FROM productos WHERE stock <= ?", (umbral,))
    productos = cursor.fetchall()
    print(f"\n⚠️ Productos con stock igual o menor a {umbral}:")
    if productos:
        for p in productos:
            print(f"{p[1]} - Stock: {p[4]}")
    else:
        print("Ningún producto tiene stock bajo.")

# Función para el producto más caro y más barato
def reporte_extremos():
    cursor.execute("SELECT * FROM productos ORDER BY precio DESC LIMIT 1")
    caro = cursor.fetchone()
    cursor.execute("SELECT * FROM productos ORDER BY precio ASC LIMIT 1")
    barato = cursor.fetchone()

    print("\n💰 Producto más caro:")
    print(f"{caro[1]} - ${caro[3]}")

    print("\n🪙 Producto más barato:")
    print(f"{barato[1]} - ${barato[3]}")

# Función para exportar todos los productos a CSV
def exportar_a_csv(nombre_archivo="reporte_productos.csv"):
    df = pd.read_sql_query("SELECT * FROM productos", conn)
    df.to_csv(nombre_archivo, index=False)
    print(f"\n✅ Reporte exportado a {nombre_archivo}")

# Menú de reportes
def menu_reportes():
    while True:
        print("\n=== Menú de Reportes ===")
        print("1. Ver todos los productos")
        print("2. Productos sin stock")
        print("3. Productos con stock bajo")
        print("4. Producto más caro y más barato")
        print("5. Exportar productos a CSV")
        print("6. Salir")

        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            reporte_todos_los_productos()
        elif opcion == "2":
            reporte_sin_stock()
        elif opcion == "3":
            umbral = int(input("Ingresa el umbral de stock bajo: "))
            reporte_stock_bajo(umbral)
        elif opcion == "4":
            reporte_extremos()
        elif opcion == "5":
            exportar_a_csv()
        elif opcion == "6":
            break
        else:
            print("Opción inválida.")

# Ejecutar menú
menu_reportes()

# Cerrar conexión
conn.close()
