"""
Vamos a crear una lista de 100 números enteros aleatorios entre -5000 y 5000 y vamos a averiguar:

Usando map:
    - Una lista con los números elevados al cuadrado.
    - Una lista con los números como cadena de texto.

Usando filter:
    - Los números múltiplos de 3.
    - El total de números negativos.
    - Los números primos.
    - El máximo número primo.

Usando reduce:
    - La suma de todos los números.
    - La suma de todos los números pares.
    - La multiplicación de todos los números primos.
"""
import random
from functools import reduce

TOTAL_NUMBERS = 10
MIN_VALUE, MAX_VALUE = -5000, 5000


def main():
    my_list = [random.randint(MIN_VALUE, MAX_VALUE) for _ in range(TOTAL_NUMBERS)]

    squared_list = list(map(lambda n: n ** 2, my_list))
    text_list = list(map(lambda n: str(n), my_list))

    multiples_of_3_list = list(filter(lambda n: n % 3 == 0, my_list))
    negatives_list = list(filter(lambda n: n < 0, my_list))
    primes_list = list(filter(lambda n: is_prime(n), my_list))

    total_sum = reduce(lambda total, n: total + n, my_list, 0)
    pairs_sum = reduce(lambda total, n: total + (n if n%2==0 else 0), my_list, 0)
    primes_multiplication = reduce(lambda total, n: total * n, primes_list, 1)

    print("Lista de números generada:", my_list)
    print("Lista elevada al cuadrado:", squared_list)
    print("Lista como texto:", text_list)
    print("Lista de números múltiplos de 3:", multiples_of_3_list)
    print("Lista de números negativos:", negatives_list)
    print("Lista de números primos:", primes_list)
    print("Máximo número primo:", max(primes_list) if len(primes_list) > 0 else None)
    print("Suma de todos los números de la lista:", total_sum)
    print("Suma de los números pares de la lista:", pairs_sum)
    print("Multiplicación de los números primos de la lista:", primes_multiplication if len(primes_list) > 0 else None)


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    max_divisor = int(n**0.5) + 1
    for divisor in range(3, max_divisor, 2):
        if n % divisor == 0:
            return False
    return True


if __name__ == '__main__':
    main()
