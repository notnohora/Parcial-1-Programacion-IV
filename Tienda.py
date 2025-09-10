import xml.etree.ElementTree as ET

class Producto:

    def __init__(self, nombre, id, precio, cantidadInventario):
        self.nombre = nombre
        self.id = int(id)
        self.precio = float(precio)
        self.cantidadInventario= int(cantidadInventario)

    def DisminuirInventario(self, disminucion):
        self.cantidadInventario -= disminucion

    def AumentarInventario(self, aumento):
        self.cantidadInventario += aumento

    def MostrarInformacion(self):
        return f"Producto: {self.nombre}, ID: {self.id}, Precio: ${self.precio}, Cantidad en Inventario: {self.cantidadInventario}"

class Cliente:

    def __init__(self, nombre, id, saldo):
        self.nombre = nombre
        self.id = int(id)
        self.saldo = float(saldo)

    def RealizarCompra(self, producto, cantidad):
        total = producto.precio * cantidad
        if (self.saldo >= total and producto.cantidadInventario >= cantidad):
            self.saldo -= total
            producto.DisminuirInventario(cantidad)
            return True
        else:
            return False

    def MostrarInformacion(self):
        return f"Cliente: {self.nombre}, ID: {self.id}, Saldo: ${self.saldo}"

class Tienda:

    def __init__(self):
        self.listaProductos = []
        self.listaClientesRegistrados = []

    def AgregarProducto(self, producto):
        self.listaProductos.append(producto)

    def AgregarCliente(self, cliente):
        self.listaClientesRegistrados.append(cliente)

    def RealizarVenta(self, id_cliente, id_producto, cantidad):
        cliente = None
        producto = None

        for c in self.listaClientesRegistrados:
            if c.id == id_cliente:
                cliente = c
                break

        for p in self.listaProductos:
            if p.id == id_producto:
            producto = p
            break

        if cliente is not None and producto is not None:
            if cliente.RealizarCompra(producto, cantidad):
                print("Venta realizada con éxito.")
            else:
                print("No se pudo realizar la venta (saldo o stock insuficiente).")
        else:
            print("Cliente o producto no encontrado.")

    def MostrarProductos(self):
        for producto in self.listaProductos:
            print(producto.MostrarInformacion())

    def MostrarClientes(self):
        for cliente in self.listaClientesRegistrados:
            print(cliente.MostrarInformacion())

    def GuardarDatos(self, archivo):
        root = ET.Element("Tienda")

        productos_elem = ET.SubElement(root, "Productos")
        for producto in self.listaProductos:
            prod_elem = ET.SubElement(productos_elem, "Producto")
            ET.SubElement(prod_elem, "Nombre").text = producto.nombre
            ET.SubElement(prod_elem, "ID").text = str(producto.id)
            ET.SubElement(prod_elem, "Precio").text = str(producto.precio)
            ET.SubElement(prod_elem, "Cantidad").text = str(producto.cantidadInventario)

        clientes_elem = ET.SubElement(root, "Clientes")
        for cliente in self.listaClientesRegistrados:
            cli_elem = ET.SubElement(clientes_elem, "Cliente")
            ET.SubElement(cli_elem, "Nombre").text = cliente.nombre
            ET.SubElement(cli_elem, "ID").text = str(cliente.id)
            ET.SubElement(cli_elem, "Saldo").text = str(cliente.saldo)

        tree = ET.ElementTree(root)
        tree.write(archivo, encoding="utf-8", xml_declaration=True)

    def CargarDatos(self, archivo):
        tree = ET.parse(archivo)
        root = tree.getroot()
        self.listaProductos = []
        self.listaClientesRegistrados = []

        for prod_elem in root.find("Productos"):
            nombre = prod_elem.find("Nombre").text
            id = int(prod_elem.find("ID").text)
            precio = float(prod_elem.find("Precio").text)
            cantidad = int(prod_elem.find("Cantidad").text)
            self.listaProductos.append(Producto(nombre, id, precio, cantidad))

        for cli_elem in root.find("Clientes"):
            nombre = cli_elem.find("Nombre").text
            id = int(cli_elem.find("ID").text)
            saldo = float(cli_elem.find("Saldo").text)
            self.listaClientesRegistrados.append(Cliente(nombre, id, saldo))


def main():
    tienda = Tienda()

    tienda.AgregarProducto(Producto("Laptop", 1, 1500.0, 5))
    tienda.AgregarProducto(Producto("Mouse", 2, 20.0, 50))

    tienda.AgregarCliente(Cliente("Nohora", 100, 2000.0))
    tienda.AgregarCliente(Cliente("Pablo", 101, 30.0))

    tienda.MostrarProductos()
    tienda.MostrarClientes()

    tienda.RealizarVenta(100, 1, 1)
    tienda.RealizarVenta(101, 1, 1)

    tienda.GuardarDatos("tienda.xml")

    nueva_tienda = Tienda()
    nueva_tienda.CargarDatos("tienda.xml")
    nueva_tienda.MostrarProductos()
    nueva_tienda.MostrarClientes()

if __name__ == "__main__":
    main()