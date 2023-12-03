"""
Programa que genera 20 números enteros entre 100 y 999 y los introduce en un array de 4 filas por 5 columnas.
El programa muestra las sumas parciales de filas y columnas igual que si de una hoja de cálculo se tratara.
La suma total aparece en la esquina inferior derecha.

Ejercicio del libro "Aprende Java con Ejercicios edición 2018" (https://leanpub.com/aprendejava).

@author Rafael del Castillo
"""
from random import randint

ROWS = 3
COLUMNS = 2
LOWEST_NUM = 100
BIGGEST_NUM = 999
WIDTH_NUMBER = 5  # no voy a tener números de más de 5 cifras

array = [[randint(LOWEST_NUM, BIGGEST_NUM) for _ in range(COLUMNS)] for _ in range(ROWS)]  # generamos los datos

# Imprimir filas y sumatorio de cada fila
for row in array:
    sum_row = 0
    for n in row:
        sum_row += n
        print(f"{n:{WIDTH_NUMBER}} ", end="")
    print(f"| {sum_row:{WIDTH_NUMBER}}")

# Imprimir sumatorio de las columnas y sumatorio total
len_sep = ((WIDTH_NUMBER + 1) * (COLUMNS + 1) + 1)
print("-" * len_sep)  # separador
sum_total = 0
for column in range(COLUMNS):
    sum_column = 0
    for row in range(ROWS):
        sum_column += array[row][column]
    print(f"{sum_column:{WIDTH_NUMBER}} ", end="")
    sum_total += sum_column
print(f"| {sum_total:{WIDTH_NUMBER}}")
