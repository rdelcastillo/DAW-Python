"""
Ejemplo de función generadora para crear tablas de multiplicar.

Autor: Rafael del Castillo Gomariz
"""
from typeguard import typechecked

@typechecked
def multiplication_generator(n: int):
    for i in range(1, 11):
        yield i * n

if __name__ == '__main__':
    num = int(input("¿Qué tabla de multiplicar quiere mostrar? "))
    for i, p in enumerate(multiplication_generator(num)):
        print(f"{num} x {i+1} = {p}")
