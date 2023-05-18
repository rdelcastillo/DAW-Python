"""
Iterador PrimeIterator que permite iterar sobre la lista de números primos, desde 2 hasta uno dado como máximo.

Creamos una lista interna y usamos la criba de Eratóstenes.

Ejemplo: "primes = list(PrimeIterator(15)) devolverá [2, 3, 5, 7, 11, 13]

Autor: Rafael del Castillo Gomariz
"""
from collections.abc import Iterator
from typeguard import typechecked

@typechecked
class PrimeIterator(Iterator):

    def __init__(self, stop: int):
        if stop < 2:
            raise ValueError("El máximo debe ser mayor o igual a 2")
        primes = self.__create_primes_with_sieve_of_eratosthenes(stop)
        self.__primes_iterator = iter(primes)

    @staticmethod
    def __create_primes_with_sieve_of_eratosthenes(stop: int):
        numbers = list(range(2, stop + 1))
        i = 0
        while numbers[i] ** 2 < stop:
            for num in numbers[i+1:]:
                if num % numbers[i] == 0:
                    numbers.remove(num)
            i += 1
        return numbers

    def __next__(self):
        return next(self.__primes_iterator)


if __name__ == '__main__':
    n = int(input("¿Hasta qué valor quieres sacar la lista de números primos? "))
    for p in PrimeIterator(n):
        print(p, end=" ")
    print()
