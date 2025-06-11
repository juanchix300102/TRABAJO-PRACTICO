import sqlite3

# Conexión a la base de datos
conn = sqlite3.connect("tienda_electrodomesticos.db")
cursor = conn.cursor()

# Crear tabla de proveedores si no existe
cursor.execute("""
CREATE TABLE IF NOT EXISTS proveedores (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    contacto TEXT,
    direccion TEXT
)
""")
conn.commit()

# Función para registrar proveedor
def registrar_proveedor():
    nombre = input("Nombre del proveedor: ")
    contacto = input("Contacto (teléfono o correo): ")
    direccion = input("Dirección: ")

    cursor.execute("""
    INSERT INTO proveedores (nombre, contacto, direccion)
    VALUES (?, ?, ?)
    """, (nombre, contacto, direccion))
    conn.commit()
    print("✅ Proveedor registrado exitosamente.")

# Función para listar proveedores
def listar_proveedores():
    cursor.execute("SELECT * FROM proveedores")
    proveedores = cursor.fetchall()

    print("\n📦 Lista de Proveedores:")
    if proveedores:
        for p in proveedores:
            print(f"ID: {p[0]}, Nombre: {p[1]}, Contacto: {p[2]}, Dirección: {p[3]}")
    else:
        print("No hay proveedores registrados.")

# Función para buscar proveedor por nombre
def buscar_proveedor():
    nombre = input("Ingrese el nombre del proveedor a buscar: ")
    cursor.execute("SELECT * FROM proveedores WHERE nombre LIKE ?", ('%' + nombre + '%',))
    resultados = cursor.fetchall()

    if resultados:
        for p in resultados:
            print(f"ID: {p[0]}, Nombre: {p[1]}, Contacto: {p[2]}, Dirección: {p[3]}")
    else:
        print("Proveedor no encontrado.")

# Función para eliminar proveedor
def eliminar_proveedor():
    id_prov = input("Ingrese el ID del proveedor a eliminar: ")
    cursor.execute("DELETE FROM proveedores WHERE id = ?", (id_prov,))
    conn.commit()
    print("🗑️ Proveedor eliminado (si existía).")

# Función para actualizar proveedor
def actualizar_proveedor():
    id_prov = input("Ingrese el ID del proveedor a actualizar: ")
    nuevo_nombre = input("Nuevo nombre: ")
    nuevo_contacto = input("Nuevo contacto: ")
    nueva_direccion = input("Nueva dirección: ")

    cursor.execute("""
    UPDATE proveedores
    SET nombre = ?, contacto = ?, direccion = ?
    WHERE id = ?
    """, (nuevo_nombre, nuevo_contacto, nueva_direccion, id_prov))
    conn.commit()
    print("🔄 Proveedor
