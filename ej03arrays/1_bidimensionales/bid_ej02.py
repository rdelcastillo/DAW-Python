"""
Programa que genera 20 números enteros entre 100 y 999 y los introduce en un array de 4 filas por 5 columnas.
El programa muestra las sumas parciales de filas y columnas igual que si de una hoja de cálculo se tratara.
La suma total aparece en la esquina inferior derecha.

Ejercicio del libro "Aprende Java con Ejercicios edición 2018" (https://leanpub.com/aprendejava).

@author Rafael del Castillo
"""
import random

ROWS = 4
COLUMNS = 5
LOWEST_NUM = 100
BIGGEST_NUM = 999
WIDTH_NUMBER = 5
array = [[0] * COLUMNS for _ in range(ROWS)]  # inicializamos array (lista) a 0

# Generación de datos
for row in range(ROWS):
    for column in range(COLUMNS):
        array[row][column] = random.randint(LOWEST_NUM, BIGGEST_NUM)

# Imprimir filas y sumatorio de cada fila
for row in range(ROWS):
    sum_row = 0
    for column in range(COLUMNS):
        sum_row += array[row][column]
        print(f"{array[row][column]:{WIDTH_NUMBER}} ", end="")
    print(f"| {sum_row:{WIDTH_NUMBER}}")

# Imprimir sumatorio de las columnas y sumatorio total
print("-" * ((WIDTH_NUMBER+1)*(COLUMNS+1) + 1))  # separador
sum_total = 0
for column in range(COLUMNS):
    sum_column = 0
    for row in range(ROWS):
        sum_column += array[row][column]
    print(f"{sum_column:{WIDTH_NUMBER}} ", end="")
    sum_total += sum_column
print(f"| {sum_total:{WIDTH_NUMBER}}")
