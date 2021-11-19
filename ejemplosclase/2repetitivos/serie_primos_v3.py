"""
Este programa pedirá una cantidad de números primos para mostrar.

Versión 3.

En esta versión nos vamos a saltar los números pares, salvo el 2, porque sabemos
que no son primos.

Cuando comprobemos los posibles divisores, nos vamos a saltar los pares, porque
sabemos que un número impar no puede ser divisible por uno par.

El ciclo de comprobación de los divisores, lo vamos a simplificar usando un break.

Autoría: Clase 1ºDAW-A
Fecha: 19/11/2021
"""
import math
import sys

print("Relación de números primos")
print("--------------------------")

# Petición de datos
num_primes_to_show = int(input("¿Cuántos números primos mostramos? "))
if num_primes_to_show < 1:
    print("No puedo imprimir esa cantidad de primos", file=sys.stderr)
    exit(1)

# Proceso
print("2")  # es el primer primo y único par, a partir de aquí todos impares
num_primes_displayed = 1
prime_candidate = 3

while num_primes_displayed < num_primes_to_show:
    # ¿el candidato a primo lo es?
    # vamos a comprobar si es divisible por algún número entre dos y su raíz cuadrada
    is_prime = True
    divider = 3
    while divider <= math.sqrt(prime_candidate):
        if prime_candidate % divider == 0:
            is_prime = False
            break
        divider += 2

    if is_prime:
        print(prime_candidate)
        num_primes_displayed += 1

    # pasar al siguiente candidato
    prime_candidate += 2
