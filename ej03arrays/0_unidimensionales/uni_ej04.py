"""
Programa que pide 10 números por teclado y los muestre junto con las palabras “máximo” y “mínimo” al lado
del máximo y del mínimo respectivamente.

@author Rafael del Castillo Gomariz

Ejercicio del libro "Aprende Java con Ejercicios edición 2018" (https://leanpub.com/aprendejava).

"""
TOTAL_NUMBERS = 10

# Creamos lista que hará de vector de 10 elementos
numbers = [None] * TOTAL_NUMBERS

# Pedimos datos
print(f"Introduzca {TOTAL_NUMBERS} números enteros y pulse INTRO:")
for i in range(TOTAL_NUMBERS):
    numbers[i] = int(input())

# Calculamos máximo y mínimo, observa que no es necesario hacerlo en el ciclo anterior
max_number = max(numbers)
min_number = min(numbers)

# Mostramos resultado
print()
for i in range(TOTAL_NUMBERS):
    print(numbers[i], end=" ")
    if numbers[i] == max_number:
        print("máximo ", end=" ")
    if numbers[i] == min_number:
        print("mínimo ", end=" ")
