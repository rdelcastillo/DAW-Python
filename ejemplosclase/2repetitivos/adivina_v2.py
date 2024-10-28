"""
Este programa pedirá repetidamente al usuario un número entre 1 y 100 hasta que lo adivine.

En esta versión el número se generará de forma aleatoria y contabilizaremos la cantidad de intentos
que se han realizado.

Fecha: 28/10/2024.
"""
import random

print("Adivina un número entre 1 y 100")
print("-------------------------------")

num_to_guess = random.randint(1, 100)
tries = 1

n = int(input("Dame un número entre 1 y 100: "))
while n != num_to_guess:
    print("No acertaste :-(")
    tries += 1
    n = int(input("Dame un número entre 1 y 100: "))

print(f"Acertaste en {tries} intentos!!!")