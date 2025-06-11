import sqlite3

# Conexión a la base de datos (se crea si no existe)
conn = sqlite3.connect('clientes.db')
cursor = conn.cursor()

# Crear tabla de clientes si no existe
cursor.execute('''
CREATE TABLE IF NOT EXISTS clientes (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    nombre TEXT NOT NULL,
    telefono TEXT,
    email TEXT,
    direccion TEXT
)
''')
conn.commit()

# Funciones
def agregar_cliente():
    print("\n📋 Agregar Nuevo Cliente")
    nombre = input("Nombre completo: ").strip()
    telefono = input("Teléfono: ").strip()
    email = input("Email: ").strip()
    direccion = input("Dirección: ").strip()

    cursor.execute('''
    INSERT INTO clientes (nombre, telefono, email, direccion)
    VALUES (?, ?, ?, ?)''', (nombre, telefono, email, direccion))
    conn.commit()
    print("✅ Cliente agregado exitosamente.")

def ver_clientes():
    print("\n📋 Lista de Clientes:")
    cursor.execute('SELECT id, nombre, telefono, email, direccion FROM clientes')
    clientes = cursor.fetchall()
    
    if clientes:
        for c in clientes:
            print(f"\nID: {c[0]}")
            print(f"Nombre: {c[1]}")
            print(f"Teléfono: {c[2]}")
            print(f"Email: {c[3]}")
            print(f"Dirección: {c[4]}")
    else:
        print("No hay clientes registrados.")

def buscar_cliente():
    nombre = input("\n🔍 Buscar cliente por nombre: ").strip()
    cursor.execute('SELECT * FROM clientes WHERE nombre LIKE ?', ('%' + nombre + '%',))
    resultados = cursor.fetchall()
    if resultados:
        for c in resultados:
            print(f"\nID: {c[0]} | Nombre: {c[1]} | Teléfono: {c[2]} | Email: {c[3]} | Dirección: {c[4]}")
    else:
        print("❌ Cliente no encontrado.")

def eliminar_cliente():
    try:
        id_cliente = int(input("\n🗑 Ingrese el ID del cliente a eliminar: "))
        cursor.execute('DELETE FROM clientes WHERE id = ?', (id_cliente,))
        conn.commit()
        if cursor.rowcount > 0:
            print("✅ Cliente eliminado correctamente.")
        else:
            print("❌ Cliente no encontrado.")
    except ValueError:
        print("⚠️ ID inválido.")

# Menú principal
def menu():
    while True:
        print("\n===== GESTIÓN DE CLIENTES =====")
        print("1. Agregar cliente")
        print("2. Ver clientes")
        print("3. Buscar cliente por nombre")
        print("4. Eliminar cliente")
        print("5. Salir")

        opcion = input("Seleccione una opción (1-5): ")

        if opcion == "1":
            agregar_cliente()
        elif opcion == "2":
            ver_clientes()
        elif opcion == "3":
            buscar_cliente()
        elif opcion == "4":
            eliminar_cliente()
        elif opcion == "5":
            print("👋 Saliendo del sistema...")
            break
        else:
            print("❌ Opción no válida. Intente de nuevo.")

# Ejecutar menú
if __name__ == "__main__":
    menu()
    conn.close()
