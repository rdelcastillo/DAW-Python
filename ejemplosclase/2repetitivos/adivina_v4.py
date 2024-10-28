"""
Este programa pedirá repetidamente al usuario un número entre 1 y 100 hasta que lo adivine.

En esta versión habrá un límite de intentos.

Fecha: 28/10/2024.
"""
import random

MIN_TO_GUESS = 1
MAX_TO_GUESS = 100
MAX_TRIES = 10

print(f"Adivina un número entre {MIN_TO_GUESS} y {MAX_TO_GUESS}")
print("-------------------------------")

num_to_guess = random.randint(MIN_TO_GUESS, MAX_TO_GUESS)
tries = 1

n = int(input(f"Dame un número entre {MIN_TO_GUESS} y {MAX_TO_GUESS}: "))
while n != num_to_guess and tries < MAX_TRIES:
    print("No acertaste :-(")
    if n > num_to_guess:
        print("El número que tienes que adivinar es MENOR.")
    else:
        print("El número que tienes que adivinar es MAYOR.")
    tries += 1
    n = int(input(f"Dame un número entre {MIN_TO_GUESS} y {MAX_TO_GUESS}: "))

if n == num_to_guess:
    print(f"Acertaste en {tries} intentos!!!")
else:
    print(f"Has agotado los {MAX_TRIES} intentos. El número a adivinar era {num_to_guess}")