"""
Este programa pedirá repetidamente al usuario un número entre 1 y 100 hasta que lo adivine.

Fecha: 28/10/2024.
"""

NUM_TO_GUESS = 60

# Mensaje de bienvenida
print("Adivina un número entre 1 y 100")
print("-------------------------------")

# Proceso
n = int(input("Dame un número entre 1 y 100: "))
while n != NUM_TO_GUESS:
    print("No acertaste :-(")
    n = int(input("Dame un número entre 1 y 100: "))

# Fin
print("Acertaste!!!")