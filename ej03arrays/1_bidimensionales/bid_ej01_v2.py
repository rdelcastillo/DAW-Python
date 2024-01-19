"""
Programa que pide 20 números enteros.

Estos números se introducen en un array de 4 filas por 5 columnas.
El programa muestra las sumas parciales de filas y columnas igual que si de una hoja de cálculo se tratara.
La suma total aparece en la esquina inferior derecha.

Ejercicio del libro "Aprende Java con Ejercicios edición 2018" (https://leanpub.com/aprendejava).

En esta versión mejoramos los siguientes aspectos:

- El ancho de visualización de cada número lo calculamos automáticamente (no es 3 como antes).
- A la hora de imprimir las casillas y calcular el sumatorio de las filas, contemplamos que un array bidimensional es
  un array de arrays de una dimensión y usamos la función sum().

@author Rafael del Castillo
"""

ROWS = 4
COLUMNS = 5
array = [[0] * COLUMNS for _ in range(ROWS)]  # inicializamos array (lista) a 0

# Petición de datos
sum_total = 0
for row in range(ROWS):
    for column in range(COLUMNS):
        n = int(input(f"Dame el valor del array de la posición {row},{column}: "))
        array[row][column] = n
        sum_total += n

width_number = len(str(sum_total))  # ancho de visualización del número

# Imprimir filas y sumatorio de cada fila
for vector in array:  # array tiene en cada fila un vector de enteros
    for n in vector:
        print(f"{n:{width_number}d} ", end="")
    print(f"| {sum(vector):{width_number}d}")

# Imprimir sumatorio de las columnas y sumatorio total
print("-" * ((width_number+1)*(COLUMNS+1) + 1))  # separador
sum_total = 0
for column in range(COLUMNS):
    sum_column = 0
    for row in range(ROWS):
        sum_column += array[row][column]
    print(f"{sum_column:{width_number}d} ", end="")
    sum_total += sum_column
print(f"| {sum_total:{width_number}d}")
