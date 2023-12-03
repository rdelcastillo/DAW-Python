"""
Iterador sobre los números pares.

Autor: Rafael del Castillo
"""
from collections.abc import Iterator
from typeguard import typechecked

@typechecked
class PairIterator(Iterator):

    def __init__(self, stop: int):
        if stop < 0:
            raise ValueError("El número de parada no puede ser negativo")
        self.__stop = stop
        self.__current = 2

    def __next__(self):
        if self.__current > self.__stop:
            raise StopIteration
        pair = self.__current
        self.__current += 2
        return pair

if __name__ == '__main__':
    pair_iterator = PairIterator(10)
    for n in pair_iterator:
        print(n)
