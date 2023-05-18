"""
Iterador PrimeIterator que permite iterar sobre la lista de números primos, desde 2 hasta uno dado como máximo.

Ejemplo: "primes = list(PrimeIterator(15)) devolverá [2, 3, 5, 7, 11, 13]

Autor: Rafael del Castillo Gomariz
"""
import math
from typeguard import typechecked
from collections.abc import Iterator

@typechecked
class PrimeIterator(Iterator):

    def __init__(self, stop: int):
        if stop < 2:
            raise ValueError("El máximo debe ser mayor o igual a 2")
        self.__stop = stop
        self.__current_prime = 2

    def __next__(self):
        if self.__current_prime > self.__stop:
            raise StopIteration
        prime, self.__current_prime = self.__current_prime, self.__next_prime()
        return prime

    def __next_prime(self):
        if self.__current_prime == 2:
            return 3
        candidate_prime = self.__current_prime + 2
        while not self.__is_prime(candidate_prime):
            candidate_prime += 2
        return candidate_prime

    @staticmethod
    def __is_prime(num):
        for i in range(3, int(math.sqrt(num) + 1), 2):
            if num % i == 0:
                return False
        return True


if __name__ == '__main__':
    n = int(input("¿Hasta qué valor quieres sacar la lista de números primos? "))
    for p in PrimeIterator(n):
        print(p, end=" ")
    print()