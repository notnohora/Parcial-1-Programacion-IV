import xml.etree.ElementTree as ET

class Producto:
    def __init__(self, nombre, id_producto, precio, cantidad_inventario):
        self.nombre = nombre
        self.id_producto = int(id_producto)
        self.precio = float(precio)
        self.cantidad_inventario = int(cantidad_inventario)

    def disminuir_inventario(self, disminucion):
        self.cantidad_inventario -= disminucion

    def aumentar_inventario(self, aumento):
        self.cantidad_inventario += aumento

    def mostrar_informacion(self):
        return f"Producto: {self.nombre}, ID: {self.id_producto}, Precio: ${self.precio}, Cantidad en Inventario: {self.cantidad_inventario}"

class Cliente:
    def __init__(self, nombre, id_cliente, saldo):
        self.nombre = nombre
        self.id_cliente = int(id_cliente)
        self.saldo = float(saldo)

    def realizar_compra(self, producto, cantidad):
        total = producto.precio * cantidad
        if self.saldo >= total and producto.cantidad_inventario >= cantidad:
            self.saldo -= total
            producto.disminuir_inventario(cantidad)
            return True
        else:
            return False

    def mostrar_informacion(self):
        return f"Cliente: {self.nombre}, ID: {self.id_cliente}, Saldo: ${self.saldo}"

class Tienda:
    def __init__(self):
        self.lista_productos = []
        self.lista_clientes_registrados = []

    def agregar_producto(self, producto):
        self.lista_productos.append(producto)

    def agregar_cliente(self, cliente):
        self.lista_clientes_registrados.append(cliente)

    def realizar_venta(self, id_cliente, id_producto, cantidad):
        cliente = None
        producto = None

        for c in self.lista_clientes_registrados:
            if c.id_cliente == id_cliente:
                cliente = c
                break

        for p in self.lista_productos:
            if p.id_producto == id_producto:
                producto = p
                break

        if cliente is not None and producto is not None:
            if cliente.realizar_compra(producto, cantidad):
                print("Venta realizada con éxito.")
            else:
                print("No se pudo realizar la venta (saldo o stock insuficiente).")
        else:
            print("Cliente o producto no encontrado.")

    def mostrar_productos(self):
        for producto in self.lista_productos:
            print(producto.mostrar_informacion())

    def mostrar_clientes(self):
        for cliente in self.lista_clientes_registrados:
            print(cliente.mostrar_informacion())

    def guardar_datos(self, archivo):
        root = ET.Element("Tienda")

        productos_elem = ET.SubElement(root, "Productos")
        for producto in self.lista_productos:
            prod_elem = ET.SubElement(productos_elem, "Producto")
            ET.SubElement(prod_elem, "Nombre").text = producto.nombre
            ET.SubElement(prod_elem, "ID").text = str(producto.id_producto)
            ET.SubElement(prod_elem, "Precio").text = str(producto.precio)
            ET.SubElement(prod_elem, "Cantidad").text = str(producto.cantidad_inventario)

        clientes_elem = ET.SubElement(root, "Clientes")
        for cliente in self.lista_clientes_registrados:
            cli_elem = ET.SubElement(clientes_elem, "Cliente")
            ET.SubElement(cli_elem, "Nombre").text = cliente.nombre
            ET.SubElement(cli_elem, "ID").text = str(cliente.id_cliente)
            ET.SubElement(cli_elem, "Saldo").text = str(cliente.saldo)

        tree = ET.ElementTree(root)
        tree.write(archivo, encoding="utf-8", xml_declaration=True)

    def cargar_datos(self, archivo):
        tree = ET.parse(archivo)
        root = tree.getroot()
        self.lista_productos = []
        self.lista_clientes_registrados = []

        for prod_elem in root.find("Productos"):
            nombre = prod_elem.find("Nombre").text
            id_producto = int(prod_elem.find("ID").text)
            precio = float(prod_elem.find("Precio").text)
            cantidad = int(prod_elem.find("Cantidad").text)
            self.lista_productos.append(Producto(nombre, id_producto, precio, cantidad))

        for cli_elem in root.find("Clientes"):
            nombre = cli_elem.find("Nombre").text
            id_cliente = int(cli_elem.find("ID").text)
            saldo = float(cli_elem.find("Saldo").text)
            self.lista_clientes_registrados.append(Cliente(nombre, id_cliente, saldo))


def main():
    tienda = Tienda()

    tienda.agregar_producto(Producto("Laptop", 1, 1500.0, 5))
    tienda.agregar_producto(Producto("Mouse", 2, 20.0, 50))

    tienda.agregar_cliente(Cliente("Nohora", 100, 2000.0))
    tienda.agregar_cliente(Cliente("Pablo", 101, 30.0))

    print("\nProductos disponibles:")
    print("-" * 80)
    tienda.mostrar_productos()
    print("\nClientes registrados:")
    print("-" * 80)
    tienda.mostrar_clientes()

    print("\nEstado de ventas:")
    print("-" * 80)
    tienda.realizar_venta(100, 1, 1)
    tienda.realizar_venta(101, 1, 1)

    tienda.guardar_datos("tienda.xml")
    print("\nDatos guardados en 'tienda.xml'\n")

    nueva_tienda = Tienda()
    print("\nCargando datos desde 'tienda.xml'")
    print("-" * 80)
    nueva_tienda.cargar_datos("tienda.xml")
    nueva_tienda.mostrar_productos()
    nueva_tienda.mostrar_clientes()

if __name__ == "__main__":
    main()