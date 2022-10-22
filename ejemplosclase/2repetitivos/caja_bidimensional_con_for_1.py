"""
Este programa pedirá al usuario el número de filas y columnas de una caja y la mostrará
por pantalla numerando cada celda de la caja con sus dos coordenadas.

El máximo tamaño de la caja será de 9x9.

Autor: Rafael del Castillo
Fecha: 27/10/2021
"""
import sys

MAXIMUM_SIZE = 9
EXIT_ERROR_COLUMNS = 2
EXIT_ERROR_ROWS = 1

print("Dibujo de una caja bidimensional")
print("--------------------------------")

# Pedimos las dimensiones de la caja

# Controlamos que las dimensiones están entre 1 y MAXIMUM_SIZE.
# En caso de no estarlo acabaremos el programa con un código de salida distinto de 0.
# En caso de error no escribimos en la salida estándar, lo hacemos en la de error.

rows = int(input("Número de filas de la caja: "))
if rows < 1 or rows > MAXIMUM_SIZE:
    print(f"Dimensión de las filas incorrecta (entre 1 y {MAXIMUM_SIZE}).", file=sys.stderr)
    exit(EXIT_ERROR_ROWS)

columns = int(input("Número de columnas de la caja: "))
if columns < 1 or columns > MAXIMUM_SIZE:
    print(f"Dimensión de las columnas incorrecta (entre 1 y {MAXIMUM_SIZE}).", file=sys.stderr)
    exit(EXIT_ERROR_COLUMNS)

# Impresión de la caja

for f in range(1, rows + 1):
    for c in range(1, columns + 1):
        print(f"{f}{c}\t", end="")
    print()
