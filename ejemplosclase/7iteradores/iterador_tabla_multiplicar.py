"""
Iterador para la tabla de multiplicación.

Autor: Rafael del Castillo Gomariz
"""
from typeguard import typechecked

@typechecked
class MultiplicationIterator:

    def __init__(self, num: int):
        self.__n = num
        self.__i = 0

    @property
    def n(self):
        return self.__n

    @property
    def i(self):
        return self.__i

    def __iter__(self):
        return self

    def __next__(self):
        if self.__i == 10:
            raise StopIteration
        self.__i += 1
        return self.__i * self.__n

if __name__ == "__main__":
    NUM = 7
    print("Tabla de multiplicar del número", NUM)
    print("----------------------------------")

    iterator = MultiplicationIterator(NUM)
    for n in iterator:
        print(f"{iterator.n} x {iterator.i} = {n}")
