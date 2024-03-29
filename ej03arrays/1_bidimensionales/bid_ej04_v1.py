"""
Rellena un array de 6 filas por 10 columnas con números enteros positivos comprendidos entre 0 y 1000 (ambos incluidos).
A continuación, el programa deberá dar la posición tanto del máximo como del mínimo.
"""

import random

ROWS = 6
COLUMNS = 10
LOWEST_NUM = 0
BIGGEST_NUM = 1000

# Rellenamos el array
array = [[0] * COLUMNS for _ in range(ROWS)]
for row in range(ROWS):
    for column in range(COLUMNS):
        array[row][column] = random.randint(LOWEST_NUM, BIGGEST_NUM)
print("Array generado:", array)

# Buscamos la posición del máximo y del mínimo (podía haberlo hecho en el ciclo anterior).

# En este caso, como conocemos el rango de los números, podemos asignar el máximo temporal a
# LOWEST_NUM y el mínimo temporal a BIGGEST_NUM, en caso de no conocerlo deberíamos darles el
# valor del primer elemento.
max_num = LOWEST_NUM
min_num = BIGGEST_NUM

# Posiciones del máximo y del mínimo (podría haberlo hecho con una tupla para ser más 'pythonico')
row_max = 0
column_max = 0
row_min = 0
column_min = 0

for row in range(ROWS):
    for column in range(COLUMNS):
        if array[row][column] > max_num:  # nuevo máximo
            max_num = array[row][column]
            row_max = row
            column_max = column
        if array[row][column] < min_num:  # nuevo mínimo (ojo, elif aquí no sirve)
            min_num = array[row][column]
            row_min = row
            column_min = column

# Mostramos resultado
print(f"El máximo de los números del array es {max_num} y está en las posiciones ({row_max},{column_max})")
print(f"El mínimo de los números del array es {min_num} y está en las posiciones ({row_min},{column_min})")
