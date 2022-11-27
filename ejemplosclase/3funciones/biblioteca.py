"""
Ejemplo de lo que podría ser una biblioteca de funciones.
"""


def f1():
    print("Soy f1")


def f2(param):
    print("Soy f2 y me has pasado como parámetro", param)


def f3(param1, param2):
    print(f"Soy f3 y me has pasado como parámetros {param1} y {param2}")


def espacio_de_nombres_biblioteca():
    print(__name__)


# Probamos las funciones (imprescindible el if)
if __name__ == "__main__":
    f1()
    f2("Parámetro de prueba")
    f3("Parámetro 1", "Parámetro 2")
    espacio_de_nombres_biblioteca()
