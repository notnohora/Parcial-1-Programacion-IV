class Empleado():
    def __init__(self, nombre, id, salario_base, anios_experiencia):
        self.nombre = nombre
        self.id = id
        self.salario_base = salario_base
        self.anios_experiencia = anios_experiencia
        
    def __str__(self):
        return f"Empleado: {self.nombre}, ID: {self.id}, Salario Base: {self.salario_base}, Años de Experiencia: {self.anios_experiencia}"
        
    def calcular_salario(self):
        if 0 <= self.anios_experiencia < 3:
            bono = self.salario_base * (5 / 100)
        elif 3 <= self.anios_experiencia <= 5:
            bono = self.salario_base * (10 / 100)
        else:
            bono = self.salario_base * (15 / 100)
            
        return bono + self.salario_base
    
class GestorEmpleados():
    def __init__(self):
        self.empleados = []
        self.siguiente_id = 1 #con este atributo los ID seran incrementales

    def agregar_empleado(self, empleado):
        empleado.id = self.siguiente_id
        self.empleados.append(empleado)
        print(f"Empleado agregado con ID {empleado.id}.")
        self.siguiente_id += 1 #incrementa el ID para el proximo empleado

    def eliminar_empleado(self, id):
        empleado = self.buscar_empleado(id)
        if empleado:
            self.empleados.remove(empleado)
            print(f"Empleado con ID {id} eliminado.")
        else:
            print(f"No se encontró empleado con ID {id}.")
        
    def buscar_empleado(self, id):
        for empleado in self.empleados:
            if empleado.id == id:
                return empleado
        return None
    
    def editar_empleado(self, id):
        empleado = self.buscar_empleado(id)
        if empleado:
            cambios = False
            nuevo_nombre = input("Ingrese el nuevo nombre (ENTER para no cambiar): ").strip()
            if nuevo_nombre:
                empleado.nombre = nuevo_nombre
                cambios = True

            nuevo_salario = input("Ingrese el nuevo salario base (ENTER para no cambiar): ").strip()
            if nuevo_salario:
                if not nuevo_salario.replace(".", "", 1).isdigit(): #permite un unico punto decimal
                    print("El salario debe ser un número válido.")
                else:
                    nuevo_salario = float(nuevo_salario)
                    if nuevo_salario < 0:
                        print("El salario no puede ser negativo.")
                    else:
                        empleado.salario_base = nuevo_salario
                        cambios = True

            nueva_experiencia = input("Ingrese los nuevos años de experiencia (ENTER para no cambiar): ").strip()
            if nueva_experiencia:
                if not nueva_experiencia.isdigit():
                    print("Los años de experiencia deben ser un número entero válido.")
                else:
                    nueva_experiencia = int(nueva_experiencia)
                    if nueva_experiencia < 0:
                        print("Los años de experiencia no pueden ser negativos.")
                    else:
                        empleado.anios_experiencia = nueva_experiencia
                        cambios = True
                        
            nuevo_id = input("Ingrese el nuevo ID (ENTER para no cambiar): ").strip()
            if nuevo_id:
                if not nuevo_id.isdigit():
                    print("El ID debe ser un número entero válido.")
                else:
                    nuevo_id = int(nuevo_id)
                    if nuevo_id <= 0:
                        print("El ID debe ser un número entero positivo.")
                    elif self.buscar_empleado(nuevo_id):
                        print("El ID ya está en uso. No se puede cambiar.")
                    else:
                        empleado.id = nuevo_id
                        if empleado.id >= self.siguiente_id:
                            self.siguiente_id = empleado.id + 1  #asegura que los ID sigan siendo incrementales
                        cambios = True

            if cambios:
                self.guardar_empleados("empleados.txt")
                print("Empleado actualizado.")
            else:
                print("No se realizaron cambios.")
        else:
            print(f"No se encontró empleado con ID {id}.")
            
    def mostrar_empleados(self):
        print("\nListado de Empleados:")
        print("-" * 80)
        for empleado in self.empleados:
            print(empleado)
            print(f"Salario con bono: {empleado.calcular_salario()}")
            print("-" * 80)

    def guardar_empleados(self, nombre_archivo):
        with open(nombre_archivo, "w") as archivo:
            for empleado in self.empleados:
                archivo.write(f"{empleado.nombre},{empleado.id},{empleado.salario_base},{empleado.anios_experiencia}\n")
                #NO SÉ SI GUARDAR EL SALARIO TOTAL, DEJO EL BASE POR EL MOMENTO

    def cargar_empleados(self, nombre_archivo):
        self.empleados = []  #limpia la lista actual antes de cargar
        self.siguiente_id = 1 #reinicia el ID incremental
        with open(nombre_archivo, "r") as archivo:
            for linea in archivo:
                registro = linea.strip().split(",")
                nombre = registro[0]
                id = registro[1]
                salario_base = registro[2]
                anios_experiencia = registro[3]
                
                empleado = Empleado(nombre, int(id), float(salario_base), int(anios_experiencia))
                self.agregar_empleado(empleado)
        
gestor = GestorEmpleados()
while True:
    print("\n--- Gestión de Empleados ---")
    print("1. Agregar empleado")
    print("2. Eliminar empleado")
    print("3. Buscar empleado")
    print("4. Editar empleado")
    print("5. Mostrar empleados")
    print("6. Guardar empleados en archivo")
    print("7. Cargar empleados desde archivo")
    print("8. Salir")
    
    opcion = input("Seleccione una opción: ")
    
    
    if opcion == "1":
        nombre = input("Ingrese el nombre del empleado: ")
        salario_base = float(input("Ingrese el salario base: "))
        anios_experiencia = int(input("Ingrese los años de experiencia: "))
        empleado = Empleado(nombre, None, salario_base, anios_experiencia)
        gestor.agregar_empleado(empleado)
        
    elif opcion == "2":
        if gestor.empleados:
            id = int(input("Ingrese el ID del empleado a eliminar: "))
            gestor.eliminar_empleado(id)
        else:
            print("No hay empleados registrados.")
        
    elif opcion == "3":
        if gestor.empleados:
            id = int(input("Ingrese el ID del empleado a buscar: "))
            empleado = gestor.buscar_empleado(id)
            if empleado:
                print(empleado)
            else:
                print(f"No se encontró empleado con ID {id}.")
        else:
            print("No hay empleados registrados.")
            
    elif opcion == "4":
        if gestor.empleados:
            id = int(input("Ingrese el ID del empleado a editar: "))
            gestor.editar_empleado(id)
        else:
            print("No hay empleados registrados.")
            
    elif opcion == "5":
        if gestor.empleados:
            gestor.mostrar_empleados()
        else:
            print("No hay empleados registrados.")
        
    elif opcion == "6":
        if gestor.empleados:
            nombre_archivo = input("Ingrese el nombre del archivo para guardar (por ejemplo, empleados.txt): ")
            gestor.guardar_empleados(nombre_archivo)
            print(f"Empleados guardados en {nombre_archivo}.")
        else:
            print("No hay empleados para guardar.")
        
    elif opcion == "7":
        nombre_archivo = input("Ingrese el nombre del archivo para cargar (por ejemplo, empleados.txt): ")
        try:
            gestor.cargar_empleados(nombre_archivo)
            print(f"Empleados cargados desde {nombre_archivo}.")
        except FileNotFoundError: #obligatorio el manejo de error para no frenar el programa
            print("Archivo no encontrado.")
        
    elif opcion == "8":
        print("Saliendo del programa.")
        break
        
    else:
        print("Opción no válida. Intente nuevamente.")