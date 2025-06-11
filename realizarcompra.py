class Producto:
    """
    Representa un producto en la tienda de electrodomésticos.
    """
    def __init__(self, id_producto, nombre, precio, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def __str__(self):
        return f"ID: {self.id_producto} - {self.nombre} - Precio: ${self.precio:.2f} - Stock: {self.stock}"

class TiendaElectrodomesticos:
    """
    Gestiona los productos disponibles y las operaciones de compra.
    """
    def __init__(self):
        self.productos = {}  # Diccionario: {id_producto: objeto_Producto}
        self._inicializar_productos_base()

    def _inicializar_productos_base(self):
        """
        Carga algunos productos de ejemplo en la tienda.
        """
        self.agregar_producto(Producto("TV001", "Smart TV 55 Pulgadas", 650.00, 10))
        self.agregar_producto(Producto("REF002", "Refrigerador No Frost", 800.00, 5))
        self.agregar_producto(Producto("LAV003", "Lavadora Carga Frontal", 450.00, 8))
        self.agregar_producto(Producto("COC004", "Cocina a Gas 4 Hornallas", 300.00, 12))
        self.agregar_producto(Producto("MIC005", "Microondas Digital", 120.00, 15))

    def agregar_producto(self, producto):
        """
        Añade un producto a la tienda.
        """
        self.productos[producto.id_producto] = producto

    def listar_productos(self):
        """
        Muestra todos los productos disponibles en la tienda.
        """
        if not self.productos:
            print("No hay productos disponibles en la tienda.")
            return

        print("\n--- Productos Disponibles ---")
        for producto in self.productos.values():
            print(producto)
        print("-----------------------------\n")

    def obtener_producto(self, id_producto):
        """
        Retorna un objeto Producto dado su ID.
        """
        return self.productos.get(id_producto)

class CarritoDeCompras:
    """
    Gestiona los productos que un cliente ha añadido a su carrito.
    """
    def __init__(self):
        self.items = {}  # Diccionario: {id_producto: cantidad}

    def agregar_item(self, producto, cantidad):
        """
        Añade un producto al carrito o actualiza su cantidad.
        """
        if cantidad <= 0:
            print("La cantidad debe ser mayor a cero.")
            return False

        if producto.stock < cantidad:
            print(f"No hay suficiente stock de '{producto.nombre}'. Stock disponible: {producto.stock}")
            return False

        self.items[producto.id_producto] = self.items.get(producto.id_producto, 0) + cantidad
        print(f"Se añadieron {cantidad} unidades de '{producto.nombre}' al carrito.")
        return True

    def eliminar_item(self, id_producto):
        """
        Elimina un producto del carrito.
        """
        if id_producto in self.items:
            del self.items[id_producto]
            print(f"Producto con ID '{id_producto}' eliminado del carrito.")
            return True
        else:
            print(f"El producto con ID '{id_producto}' no está en el carrito.")
            return False

    def ver_carrito(self, tienda):
        """
        Muestra los contenidos actuales del carrito.
        """
        if not self.items:
            print("\nEl carrito de compras está vacío.")
            return 0.0

        print("\n--- Contenido del Carrito ---")
        total = 0
        for id_producto, cantidad in self.items.items():
            producto = tienda.obtener_producto(id_producto)
            if producto:
                subtotal = producto.precio * cantidad
                print(f"- {producto.nombre} (x{cantidad}) - Subtotal: ${subtotal:.2f}")
                total += subtotal
            else:
                print(f"- Producto con ID '{id_producto}' no encontrado (posiblemente eliminado de la tienda).")
        print(f"-----------------------------\nTotal del Carrito: ${total:.2f}")
        return total

    def vaciar_carrito(self):
        """
        Vacía completamente el carrito de compras.
        """
        self.items = {}
        print("El carrito ha sido vaciado.")

class ProcesoDeCompra:
    """
    Coordina la interacción entre la tienda, el carrito y el cliente.
    """
    def __init__(self, tienda):
        self.tienda = tienda
        self.carrito = CarritoDeCompras()

    def menu_compra(self):
        """
        Muestra el menú de opciones de compra al cliente.
        """
        while True:
            print("\n--- Menú de Compra ---")
            print("1. Ver productos disponibles")
            print("2. Añadir producto al carrito")
            print("3. Ver carrito")
            print("4. Eliminar producto del carrito")
            print("5. Vaciar carrito")
            print("6. Finalizar compra")
            print("7. Salir")
            print("------------------------")

            opcion = input("Seleccione una opción: ")

            if opcion == '1':
                self.tienda.listar_productos()
            elif opcion == '2':
                id_producto = input("Ingrese el ID del producto a añadir: ").upper()
                cantidad_str = input("Ingrese la cantidad: ")
                try:
                    cantidad = int(cantidad_str)
                    producto = self.tienda.obtener_producto(id_producto)
                    if producto:
                        self.carrito.agregar_item(producto, cantidad)
                    else:
                        print(f"Error: Producto con ID '{id_producto}' no encontrado.")
                except ValueError:
                    print("Cantidad inválida. Por favor, ingrese un número entero.")
            elif opcion == '3':
                self.carrito.ver_carrito(self.tienda)
            elif opcion == '4':
                id_producto = input("Ingrese el ID del producto a eliminar del carrito: ").upper()
                self.carrito.eliminar_item(id_producto)
            elif opcion == '5':
                self.carrito.vaciar_carrito()
            elif opcion == '6':
                self.finalizar_compra()
                break # Salir del menú de compra después de finalizar
            elif opcion == '7':
                print("Saliendo del proceso de compra. ¡Hasta pronto!")
                break
            else:
                print("Opción no válida. Por favor, intente de nuevo.")

    def finalizar_compra(self):
        """
        Procesa la compra, actualiza el stock y simula el pago.
        """
        total = self.carrito.ver_carrito(self.tienda)
        if total == 0:
            print("El carrito está vacío. No se puede finalizar la compra.")
            return

        confirmacion = input(f"El total de su compra es: ${total:.2f}. ¿Desea confirmar la compra? (s/n): ").lower()

        if confirmacion == 's':
            print("\n--- Procesando Compra ---")
            for id_producto, cantidad in self.carrito.items.items():
                producto = self.tienda.obtener_producto(id_producto)
                if producto:
                    if producto.stock >= cantidad:
                        producto.stock -= cantidad
                        print(f"Stock actualizado para '{producto.nombre}'. Nuevo stock: {producto.stock}")
                    else:
                        # Esto no debería ocurrir si se valida al añadir al carrito, pero es una buena práctica.
                        print(f"Error: No hay suficiente stock de '{producto.nombre}' para la compra. (ID: {id_producto})")
                        # Podrías implementar una reversión o manejo de errores aquí.
            print("¡Compra realizada con éxito! Gracias por su preferencia.")
            self.carrito.vaciar_carrito() # Vacía el carrito después de la compra exitosa
        else:
            print("Compra cancelada.")

# --- Ejecución del Programa ---
if __name__ == "__main__":
    tienda = TiendaElectrodomesticos()
    proceso_compra = ProcesoDeCompra(tienda)
    proceso_compra.menu_compra()