"""
Este programa pedirá repetidamente al usuario un número entre 1 y 100 hasta que lo adivine.

En esta versión me dirá si el número que hay que adivinar es mayor o menor y usaremos constantes para
los límites.

Fecha: 28/10/2024.
"""
import random

NUM_MIN_TO_GUESS = 1
NUM_MAX_TO_GUESS = 100

print(f"Adivina un número entre {NUM_MIN_TO_GUESS} y {NUM_MAX_TO_GUESS}")
print("-------------------------------")

num_to_guess = random.randint(NUM_MIN_TO_GUESS, NUM_MAX_TO_GUESS)
tries = 1

n = int(input(f"Dame un número entre {NUM_MIN_TO_GUESS} y {NUM_MAX_TO_GUESS}: "))
while n != num_to_guess:
    print("No acertaste :-(")
    if n > num_to_guess:
        print("El número que tienes que adivinar es MENOR.")
    else:
        print("El número que tienes que adivinar es MAYOR.")
    tries += 1
    n = int(input(f"Dame un número entre {NUM_MIN_TO_GUESS} y {NUM_MAX_TO_GUESS}: "))

print(f"Acertaste en {tries} intentos!!!")