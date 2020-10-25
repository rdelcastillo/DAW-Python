"""
Ejemplo de librería de funciones dentro de un paquete.
"""


def funcion1():
    print("Soy la función 1")


def funcion2(param):
    print("Soy la función 2 y me has llamado con", param)


def funcion3(*param):
    print(f"Soy la función 3 y me has llamado con {len(param)} parámetros:")
    for p in range(len(param)):
        print(f"\t* Soy el parámetro {p}")
