"""
Iterador para la serie de Fibonacci.

Creamos el iterador como una clase derivada de collections.abc.Iterator.

Autor: Rafael del Castillo Gomariz
"""
from typeguard import typechecked
from collections.abc import Iterator


@typechecked
class FibonacciIterator(Iterator):

    def __init__(self, stop: int = 10):
        if stop < 1:
            raise ValueError("El máximo de elementos de la serie no puede ser negativo")
        self.__index = 0
        self.__current = 0
        self.__next = 1
        self.__stop = stop

    def __next__(self):
        if self.__index == self.__stop:
            raise StopIteration
        self.__index += 1
        fib_num = self.__current
        self.__current, self.__next = self.__next, self.__current + self.__next
        return fib_num

if __name__ == '__main__':
    print("Serie de Fibonacci")
    print("------------------")

    n = int(input("¿Cuántos números quiere mostrar? "))
    for i, fib_n in enumerate(FibonacciIterator(n)):
        print(f"{i+1}: {fib_n}")
