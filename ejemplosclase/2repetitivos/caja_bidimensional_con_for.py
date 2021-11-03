"""
Este programa pedirá al usuario el número de filas y columnas de una caja y la mostrará
por pantalla numerando cada celda de la caja con sus dos coordenadas.

El máximo tamaño de la caja será de 9x9.

Autor: Rafael del Castillo
Fecha: 27/10/2021
"""
import sys

print("Dibujo de una caja bidimensional")
print("--------------------------------")

DIMENSION_MAXIMA = 9
EXIT_ERROR_COLUMNAS = 2
EXIT_ERROR_FILAS = 1

print("Dibujo de una caja bidimensional")
print("--------------------------------")

# Pedimos las dimensiones de la caja

# Controlamos que las dimensiones están entre 1 y DIMENSION_MAXIMA.
# En caso de no estarlo acabaremos el programa con un código de salida distinto de 0.
# En caso de error no escribimos en la salida estándar, lo hacemos en la de error.

filas = int(input("Número de filas de la caja: "))
if filas < 1 or filas > DIMENSION_MAXIMA:
    print(f"Dimensión de las filas incorrecta (entre 1 y {DIMENSION_MAXIMA}).", file=sys.stderr)
    exit(EXIT_ERROR_FILAS)

columnas = int(input("Número de columnas de la caja: "))
if columnas < 1 or columnas > DIMENSION_MAXIMA:
    print(f"Dimensión de las columnas incorrecta (entre 1 y {DIMENSION_MAXIMA}).", file=sys.stderr)
    exit(EXIT_ERROR_COLUMNAS)

# Impresión de la caja

for f in range(1, filas+1):
    for c in range(1, columnas+1):
        print(f"{f}{c}\t", end="")
    print()
