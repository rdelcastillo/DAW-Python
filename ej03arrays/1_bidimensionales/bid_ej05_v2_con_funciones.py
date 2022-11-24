"""
Rellena un array de 6 filas por 10 columnas con números enteros positivos comprendidos entre 0 y 1000 (ambos incluidos).
A continuación, el programa deberá dar la posición tanto del máximo como del mínimo.

Ningún número se repite.

Usaremos una función para comprobar si el número está en el array y tuplas para guardar las posiciones del máximo
y del mínimo.
"""

import random

ROWS = 6
COLUMNS = 10
LOWEST_NUM = 0
BIGGEST_NUM = 1000


def is_in_array(n, array):
    for vector in array:
        if n in vector:
            return True  # ya sé que n está en array, acabo la función
    return False  # si llego aquí es que n no está en array


# Rellenamos el array
array = [[None] * COLUMNS for _ in range(ROWS)]
for row in range(ROWS):
    for column in range(COLUMNS):
        # generamos un número que no esté en el array
        while True:
            n = random.randint(LOWEST_NUM, BIGGEST_NUM)
            if not is_in_array(n, array):
                break
        # añado número al array al array
        array[row][column] = n
print("Array generado:", array)

# Buscamos la posición del máximo y del mínimo (podía haberlo hecho en el ciclo anterior).

# En este caso, como conocemos el rango de los números, podemos asignar el máximo temporal a
# LOWEST_NUM y el mínimo temporal a BIGGEST_NUM, en caso de no conocerlo deberíamos darles el
# valor del primer elemento.
max_num = LOWEST_NUM
min_num = BIGGEST_NUM

# Posiciones del máximo y del mínimo
max_position = min_position = (0, 0)
for row in range(ROWS):
    for column in range(COLUMNS):
        if array[row][column] > max_num:  # nuevo máximo
            max_num = array[row][column]
            max_position = (row, column)
        if array[row][column] < min_num:  # nuevo mínimo (ojo, elif aquí no sirve)
            min_num = array[row][column]
            min_position = (row, column)

# Mostramos resultado
print(f"El máximo de los números del array es {max_num} y está en las posiciones ({max_position})")
print(f"El mínimo de los números del array es {min_num} y está en las posiciones ({min_position})")
