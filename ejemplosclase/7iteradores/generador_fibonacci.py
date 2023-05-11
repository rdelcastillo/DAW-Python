"""
Generador de números de la serie de Fibonacci.

Autor: Rafael del Castillo Gomariz
"""
from time import sleep


def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a+b

if __name__ == '__main__':
    print("Serie de Fibonacci (pulse Ctrl+C para acabar)")
    print("---------------------------------------------")
    for i, n in enumerate(fibonacci_generator()):
        print(f"{i+1}: {n}")
        sleep(1)