"""
Ejemplo de lectura de un fichero csv usando el módulo csv y un objeto lector.

Autor: Rafael del Castillo.
"""
import csv
import os.path
import sys

FILE = "datos.csv"

if not os.path.exists(FILE):  # comprobamos que el fichero existe
    print(f"El fichero {FILE} no existe. Terminamos...", file=sys.stderr)
    exit(1)

with open(FILE, "rt") as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=',')  # objeto lector, tendrá toda la carga del trabajo
    next(csv_reader)  # saltamos la primera fila (cabecera)
    for row in csv_reader:
        print(f"{row[0]} trabaja como {row[1]} y nació en el mes de {row[2]}.")
