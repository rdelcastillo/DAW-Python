"""
Este programa pedirá una cantidad de números primos para mostrar.

Versión 1.

Autoría: Clase 1ºDAW-B
Fecha: 17/11/2021
"""
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
    # vamos a comprobar cuantos divisores tiene entre dos y candidato-1
    total_dividers = 0
    for n in range(2, prime_candidate):
        if prime_candidate % n == 0:
            total_dividers += 1

    # si no tiene divisores es primo
    if total_dividers == 0:
        print(prime_candidate)
        num_primes_displayed += 1

    # pasar al siguiente candidato
    prime_candidate += 1