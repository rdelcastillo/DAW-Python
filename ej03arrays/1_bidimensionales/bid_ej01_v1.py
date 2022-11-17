"""
Programa que pide 20 números enteros.

Estos números se introducen en un array de 4 filas por 5 columnas.
El programa muestra las sumas parciales de filas y columnas igual que si de una hoja de cálculo se tratara.
La suma total aparece en la esquina inferior derecha.

Ejercicio del libro "Aprende Java con Ejercicios edición 2018" (https://leanpub.com/aprendejava).

@author Rafael del Castillo
"""

ROWS = 2
COLUMNS = 3
array = [[0] * COLUMNS for _ in range(ROWS)]  # inicializamos array (lista) a 0

# Petición de datos
for row in range(ROWS):
    for column in range(COLUMNS):
        array[row][column] = int(input(f"Dame el valor del array de la posición {row},{column}: "))

# Imprimir filas y sumatorio de cada fila
for row in range(ROWS):
    sum_row = 0
    for column in range(COLUMNS):
        sum_row += array[row][column]
        print(f"{array[row][column]:3d} ", end="")
    print(f"| {sum_row:3d}")

# Imprimir sumatorio de las columnas y sumatorio total
print("-" * (4*(COLUMNS+1) + 1))  # separador
sum_total = 0
for column in range(COLUMNS):
    sum_column = 0
    for row in range(ROWS):
        sum_column += array[row][column]
    print(f"{sum_column:3d} ", end="")
    sum_total += sum_column
print(f"| {sum_total:3d}")
