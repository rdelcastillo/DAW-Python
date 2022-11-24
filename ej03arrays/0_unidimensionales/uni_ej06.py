"""
Programa que genera 20 números enteros aleatorios entre 0 y 100 y los almacene en un array. Después pasa todos los
números pares a las primeras posiciones del array (del 0 en adelante) y todos los impares a las celdas restantes.
"""
import random

TOTAL_NUMBERS = 20
MIN_NUMBER = 0
MAX_NUMBER = 100

# Almacenamos los números aleatorios en una lista
numbers = []
for _ in range(TOTAL_NUMBERS):
    numbers.append(random.randint(MIN_NUMBER, MAX_NUMBER))
print("Lista original: ", numbers)

# Guardamos los números pares en una lista y los impares en otra
pair_numbers = []
odd_numbers = []
for n in numbers:
    if n % 2 == 0:
        pair_numbers.append(n)
    else:
        odd_numbers.append(n)

# Concatenamos las listas y mostramos resultado
numbers = pair_numbers + odd_numbers
print("Lista procesada:", numbers)

