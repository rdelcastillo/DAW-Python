"""
Este programa pedirá una cantidad de números primos para mostrar.

Versión 2.

En esta versión para ver si un número es primo, no comprobaremos si
todos los números comprendidos entre 2 y el anterior son divisibles, solo
hasta la raíz cuadrada del número a comprobar.

También, cuando tengamos constancia de que el número a comprobar es divisible
por alguno de los números entre 2 y el anterior, dejaremos de comprobar porque
ya sabremos que es primo.

Autoría: Clase 1ºDAW-B
Fecha: 17/11/2021
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
num_primes_displayed = 0
prime_candidate = 2

while num_primes_displayed < num_primes_to_show:
    # ¿el candidato a primo lo es?
    # vamos a comprobar si es divisible por algún número entre dos y su raíz cuadrada
    is_prime = True
    divider = 2
    while divider <= math.sqrt(prime_candidate) and is_prime:
        if prime_candidate % divider == 0:
            is_prime = False
        divider += 1

    # ¿es primo?
    if is_prime:
        print(prime_candidate)
        num_primes_displayed += 1

    # pasar al siguiente candidato
    prime_candidate += 1
