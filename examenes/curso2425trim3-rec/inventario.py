
import csv

class Producto:
    def __init__(self, codigo, nombre, precio, stock_actual, stock_minimo):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = float(precio)
        self.stock_actual = int(stock_actual)
        self.stock_minimo = int(stock_minimo)

    def hay_que_reponer(self):
        return self.stock_actual < self.stock_minimo

    def __str__(self):
        return f"{self.codigo} - {self.nombre}: {self.stock_actual} uds (mínimo: {self.stock_minimo})"

class Inventario:
    def __init__(self):
        self.__productos = []

    def cargar_desde_csv(self, nombre_fichero):
        with open(nombre_fichero, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                producto = Producto(row['código'], row['nombre'], row['precio'], row['stock_actual'], row['stock_mínimo'])
                self.__productos.append(producto)

    def productos(self):
        return [str(p) for p in self.__productos]

    def buscar_producto_por_codigo(self, codigo):
        for p in self.__productos:
            if p.codigo == codigo:
                return p
        return None

    def entrada_producto(self, codigo, cantidad):
        prod = self.buscar_producto_por_codigo(codigo)
        if prod:
            prod.stock_actual += cantidad
            return f"Entrada registrada: {cantidad} uds a {prod.nombre}"
        else:
            return "Producto no encontrado."

    def salida_producto(self, codigo, cantidad):
        prod = self.buscar_producto_por_codigo(codigo)
        if prod:
            if prod.stock_actual >= cantidad:
                prod.stock_actual -= cantidad
                return f"Salida registrada: {cantidad} uds de {prod.nombre}"
            else:
                return "No hay suficiente stock."
        else:
            return "Producto no encontrado."

    def generar_pedido(self):
        return [p for p in self.__productos if p.hay_que_reponer()]

    def guardar_informe(self, nombre_archivo):
        with open(nombre_archivo, "w") as f:
            f.write("Productos que necesitan reposición:\n")
            for p in self.generar_pedido():
                f.write(str(p) + "\n")

    def guardar_csv(self, nombre_fichero):
        with open(nombre_fichero, "w", newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['código', 'nombre', 'precio', 'stock_actual', 'stock_mínimo'])
            for p in self.__productos:
                writer.writerow([p.codigo, p.nombre, p.precio, p.stock_actual, p.stock_minimo])

def menu():
    inventario = Inventario()
    inventario.cargar_desde_csv("productos.csv")

    while True:
        print("\n--- MENU ---")
        print("1. Mostrar inventario completo")
        print("2. Realizar entrada de producto")
        print("3. Realizar salida de producto")
        print("4. Mostrar productos que necesitan reposición")
        print("5. Exportar pedido automático")
        print("6. Guardar inventario actualizado")
        print("7. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            for linea in inventario.productos():
                print(linea)
        elif opcion == "2":
            codigo = input("Código del producto: ")
            cantidad = int(input("Cantidad a ingresar: "))
            print(inventario.entrada_producto(codigo, cantidad))
        elif opcion == "3":
            codigo = input("Código del producto: ")
            cantidad = int(input("Cantidad a retirar: "))
            print(inventario.salida_producto(codigo, cantidad))
        elif opcion == "4":
            productos = inventario.generar_pedido()
            if productos:
                for p in productos:
                    print(p)
            else:
                print("No hay productos que necesiten reposición.")
        elif opcion == "5":
            inventario.guardar_informe("pedido.txt")
            print("Pedido guardado en pedido.txt")
        elif opcion == "6":
            inventario.guardar_csv("productos.csv")
            print("Inventario guardado.")
        elif opcion == "7":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu()
