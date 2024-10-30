
class Producto:
    def __init__(self, nombre, precio):
        self._nombre = nombre
        self._precio = precio

    def mostrar_info(self):
        return f"{self._nombre} - Precio: ${self._precio}"

    def obtener_precio(self):
        return self._precio

class Ropa(Producto):
    def __init__(self, nombre, precio, talla, tipo_tela):
        super().__init__(nombre, precio)
        self._talla = talla
        self._tipo_tela = tipo_tela

    def mostrar_info(self):
        return f"{self._nombre} - Talla: {self._talla} - Tipo de tela: {self._tipo_tela} - Precio: ${self._precio}"

class Camisa(Ropa):
    def __init__(self, precio, talla, tipo_tela):
        super().__init__("Camisa", precio, talla, tipo_tela)

class Pantalon(Ropa):
    def __init__(self, precio, talla, tipo_tela):
        super().__init__("Pantalon", precio, talla, tipo_tela)

class Zapato(Producto):
    def __init__(self, nombre, precio, talla):
        super().__init__(nombre, precio)
        self._talla = talla

    def mostrar_info(self):
        return f"{self._nombre} - Talla: {self._talla} - Precio: ${self._precio}"

class Carrito:
    def __init__(self):
        self._productos = []

    def agregar_producto(self, producto):
        self._productos.append(producto)

    def mostrar_resumen(self):
        total = 0
        print("Resumen de Compra:")
        for producto in self._productos:
            print(producto.mostrar_info())
            total += producto.obtener_precio()
        print(f"Total a pagar: ${total}")

class Tienda:
    def __init__(self):
        self._inventario = []

    def agregar_producto_inventario(self, producto):
        self._inventario.append(producto)

    def mostrar_inventario(self):
        print("Inventario de Productos:")
        for idx, producto in enumerate(self._inventario, start=1):
            print(f"{idx}. {producto.mostrar_info()}")

    def procesar_compra(self):
        carrito = Carrito()
        while True:
            self.mostrar_inventario()
            opcion = input("Seleccione el número del producto que desea agregar al carrito (o 'q' para finalizar): ")
            if opcion.lower() == 'q':
                break
            if opcion.isdigit() and 1 <= int(opcion) <= len(self._inventario):
                carrito.agregar_producto(self._inventario[int(opcion) - 1])
                print("Producto agregado al carrito.")
            else:
                print("Opción inválida, intente nuevamente.")
        
       
        carrito.mostrar_resumen()

tienda = Tienda()
tienda.agregar_producto_inventario(Camisa(25.00, "m", "algodon"))
tienda.agregar_producto_inventario(Pantalon(90.00, "L", "jean"))
tienda.agregar_producto_inventario(Zapato("zapato para hombre", 80.00, "40"))
tienda.procesar_compra()
