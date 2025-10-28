
import csv

class Producto:
    def __init__(self, codigo, nombre, precio, stock_actual, stock_minimo):
        # TODO: Inicializar atributos
        pass

    def hay_que_reponer(self):
        # TODO: Devolver True si stock_actual < stock_minimo
        pass

    def __str__(self):
        # TODO: Devolver string con datos del producto
        pass

class Inventario:
    def __init__(self):
        self.__productos = []

    def cargar_desde_csv(self, nombre_fichero):
        # TODO: Leer CSV y cargar productos
        pass

    def productos(self):
        # TODO: Devolver lista de strings con los productos
        pass

    def buscar_producto_por_codigo(self, codigo):
        # TODO: Buscar un producto por su código
        pass

    def entrada_producto(self, codigo, cantidad):
        # TODO: Aumentar stock y devolver mensaje
        pass

    def salida_producto(self, codigo, cantidad):
        # TODO: Disminuir stock si es posible y devolver mensaje
        pass

    def generar_pedido(self):
        # TODO: Devolver lista de productos que hay que reponer
        pass

    def guardar_informe(self, nombre_archivo):
        # TODO: Guardar pedido en un fichero
        pass

    def guardar_csv(self, nombre_fichero):
        # TODO: Guardar inventario actualizado en CSV
        pass

def menu():
    inventario = Inventario()
    inventario.cargar_desde_csv("productos.csv")

    while True:
        print("\n--- MENÚ ---")
        print("1. Mostrar inventario completo")
        print("2. Realizar entrada de producto")
        print("3. Realizar salida de producto")
        print("4. Mostrar productos que necesitan reposición")
        print("5. Exportar pedido automático")
        print("6. Guardar inventario actualizado")
        print("7. Salir")
        opcion = input("Selecciona una opción: ")

        # TODO Control de excepciones
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
            # TODO si ha habido cambios en el inventario y no se han guardado debe advertirse
            break
        else:
            print("Opción no valida.")

if __name__ == "__main__":
    menu()
