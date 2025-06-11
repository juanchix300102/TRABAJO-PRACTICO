import hashlib

class Usuario:
    """
    Representa un usuario en la tienda de electrodomésticos.
    """
    def __init__(self, nombre_usuario, contrasena, rol="cliente"):
        self.nombre_usuario = nombre_usuario
        self.contrasena_hash = self._hashear_contrasena(contrasena)
        self.rol = rol  # Puede ser "cliente", "empleado", "administrador"

    def _hashear_contrasena(self, contrasena):
        """
        Hashea la contraseña usando SHA256 para seguridad.
        """
        return hashlib.sha256(contrasena.encode()).hexdigest()

    def verificar_contrasena(self, contrasena):
        """
        Verifica si la contraseña proporcionada coincide con la almacenada.
        """
        return self._hashear_contrasena(contrasena) == self.contrasena_hash

    def __str__(self):
        return f"Usuario: {self.nombre_usuario}, Rol: {self.rol}"

class SistemaGestionUsuarios:
    """
    Gestiona la creación, eliminación, búsqueda y autenticación de usuarios.
    """
    def __init__(self):
        self.usuarios = {}  # Diccionario para almacenar usuarios: {nombre_usuario: objeto_Usuario}
        self._inicializar_usuarios_base()

    def _inicializar_usuarios_base(self):
        """
        Crea algunos usuarios por defecto para pruebas.
        """
        self.crear_usuario("admin", "admin123", "administrador")
        self.crear_usuario("empleado1", "empleado123", "empleado")
        self.crear_usuario("cliente1", "cliente123", "cliente")

    def crear_usuario(self, nombre_usuario, contrasena, rol="cliente"):
        """
        Crea un nuevo usuario y lo añade al sistema.
        Retorna True si el usuario se creó exitosamente, False si ya existe.
        """
        if nombre_usuario in self.usuarios:
            print(f"Error: El usuario '{nombre_usuario}' ya existe.")
            return False
        nuevo_usuario = Usuario(nombre_usuario, contrasena, rol)
        self.usuarios[nombre_usuario] = nuevo_usuario
        print(f"Usuario '{nombre_usuario}' creado con rol '{rol}'.")
        return True

    def eliminar_usuario(self, nombre_usuario):
        """
        Elimina un usuario del sistema.
        Retorna True si el usuario se eliminó exitosamente, False si no existe.
        """
        if nombre_usuario in self.usuarios:
            del self.usuarios[nombre_usuario]
            print(f"Usuario '{nombre_usuario}' eliminado.")
            return True
        else:
            print(f"Error: El usuario '{nombre_usuario}' no existe.")
            return False

    def buscar_usuario(self, nombre_usuario):
        """
        Busca y retorna un objeto Usuario por su nombre de usuario.
        Retorna None si el usuario no se encuentra.
        """
        return self.usuarios.get(nombre_usuario)

    def autenticar_usuario(self, nombre_usuario, contrasena):
        """
        Autentica un usuario.
        Retorna el objeto Usuario si la autenticación es exitosa, None en caso contrario.
        """
        usuario = self.buscar_usuario(nombre_usuario)
        if usuario and usuario.verificar_contrasena(contrasena):
            print(f"Autenticación exitosa para el usuario '{nombre_usuario}'.")
            return usuario
        else:
            print("Nombre de usuario o contraseña incorrectos.")
            return None

    def listar_usuarios(self):
        """
        Lista todos los usuarios registrados en el sistema.
        """
        if not self.usuarios:
            print("No hay usuarios registrados en el sistema.")
            return
        print("\n--- Lista de Usuarios ---")
        for usuario in self.usuarios.values():
            print(usuario)
        print("-------------------------\n")

def mostrar_menu():
    """
    Muestra el menú principal de opciones.
    """
    print("\n--- Sistema de Gestión de Usuarios ---")
    print("1. Crear nuevo usuario")
    print("2. Eliminar usuario")
    print("3. Buscar usuario")
    print("4. Listar todos los usuarios")
    print("5. Autenticar usuario")
    print("6. Salir")
    print("--------------------------------------")

def main():
    """
    Función principal para ejecutar el sistema.
    """
    sistema = SistemaGestionUsuarios()

    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción: ")

        if opcion == '1':
            nombre = input("Ingrese nombre de usuario: ")
            contrasena = input("Ingrese contraseña: ")
            rol = input("Ingrese rol (cliente/empleado/administrador, por defecto 'cliente'): ").lower()
            if rol not in ["cliente", "empleado", "administrador", ""]:
                print("Rol inválido. Se asignará 'cliente'.")
                rol = "cliente"
            sistema.crear_usuario(nombre, contrasena, rol if rol else "cliente")
        elif opcion == '2':
            nombre = input("Ingrese el nombre de usuario a eliminar: ")
            sistema.eliminar_usuario(nombre)
        elif opcion == '3':
            nombre = input("Ingrese el nombre de usuario a buscar: ")
            usuario_encontrado = sistema.buscar_usuario(nombre)
            if usuario_encontrado:
                print(f"Usuario encontrado: {usuario_encontrado}")
            else:
                print(f"El usuario '{nombre}' no se encontró.")
        elif opcion == '4':
            sistema.listar_usuarios()
        elif opcion == '5':
            nombre = input("Ingrese nombre de usuario para autenticar: ")
            contrasena = input("Ingrese contraseña para autenticar: ")
            usuario_autenticado = sistema.autenticar_usuario(nombre, contrasena)
            if usuario_autenticado:
                print(f"Bienvenido, {usuario_autenticado.nombre_usuario}!")
                # Aquí podrías implementar lógica adicional basada en el rol del usuario autenticado
        elif opcion == '6':
            print("Saliendo del sistema. ¡Hasta luego!")
            break
        else:
            print("Opción no válida. Por favor, intente de nuevo.")

if __name__ == "__main__":
    main()