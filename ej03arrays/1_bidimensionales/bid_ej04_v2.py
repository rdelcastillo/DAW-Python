"""
Rellena un array de 6 filas por 10 columnas con números enteros positivos comprendidos entre 0 y 1000 (ambos incluidos).
A continuación, el programa deberá dar la posición tanto del máximo como del mínimo.

En esta versión usaremos una tupla para guardar la posición del máximo y del mínimo, calcularemos el máximo y
mínimo asignándoles inicialmente el primer elemento del array, y usaremos append() para añadir al array.
"""

import random

ROWS = 6
COLUMNS = 10
LOWEST_NUM = 0
BIGGEST_NUM = 1000

# Rellenamos el array
array = []
for row in range(ROWS):
    array.append([])
    for _ in range(COLUMNS):
        array[row].append(random.randint(LOWEST_NUM, BIGGEST_NUM))
print("Array generado:", array)

# Buscamos la posición del máximo y del mínimo (podía haberlo hecho en el ciclo anterior).

# En este caso, asignamos el máximo temporal y el mínimo temporal a al valor del primer elemento.
max_num = min_num = array[0][0]
position_max = position_min = (0, 0)  # Posiciones del máximo y del mínimo

for row in range(ROWS):
    for column in range(COLUMNS):
        if array[row][column] > max_num:  # nuevo máximo
            max_num = array[row][column]
            position_max = (row, column)
        elif array[row][column] < min_num:  # nuevo mínimo
            min_num = array[row][column]
            position_min = (row, column)

# Mostramos resultado
print(f"El máximo de los números del array es {max_num} y está en las posiciones {position_max}")
print(f"El mínimo de los números del array es {min_num} y está en las posiciones {position_min}")
