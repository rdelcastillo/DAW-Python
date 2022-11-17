"""
Programa que lea 10 números por teclado y que luego los muestre en orden inverso, es decir, el primero que se introduce
es el último en mostrarse y viceversa.
"""

AMOUNT_NUMBERS_TO_READ = 10
numbers = [0] * AMOUNT_NUMBERS_TO_READ  # creamos array inicializando a 0 sus elementos

# Petición de datos
for i in range(AMOUNT_NUMBERS_TO_READ):
    numbers[i] = int(input(f"Dame el número que estará en la posición {i + 1}: "))

# Mostramos el contenido del array en orden inverso
for i in range(AMOUNT_NUMBERS_TO_READ - 1, -1, -1):
    print(numbers[i])
