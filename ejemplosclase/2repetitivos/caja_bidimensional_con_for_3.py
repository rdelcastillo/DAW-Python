"""
Este programa pedirá al usuario el número de filas y columnas de una caja y la mostrará
por pantalla numerando cada celda de la caja con sus dos coordenadas.

El máximo tamaño de la caja será de 9x9.

En esta versión añadimos caracteres gráficos.

Autor: Rafael del Castillo
Fecha: 08/11/2021
"""
import sys

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

# Creamos las cadenas correspondientes a la cabecera, intersección y pie de la caja
cabecera_caja = "┌" + "────┬" * (columnas - 1) + "────┐"
interseccion_caja = "├" + "────┼" * (columnas - 1) + "────┤"
pie_caja = "└" + "────┴" * (columnas - 1) + "────┘"

# Impresión caja
f = 0
print(cabecera_caja)
while True:
    print("│", end="")
    for c in range(columnas):
        print(f" {f + 1}{c + 1} ", end="│")
    f += 1
    if f == filas:
        break
    print(f"\n{interseccion_caja}")
print(f"\n{pie_caja}")
