"""
Ejemplo de lectura de un fichero csv directamente en un diccionario.

Autor: Rafael del Castillo.
"""
import csv
import os.path
import sys

FILE = "datos.csv"

if not os.path.exists(FILE):  # comprobamos que el fichero existe
    print(f"El fichero {FILE} no existe. Terminamos...", file=sys.stderr)
    exit(1)

with open(FILE) as csv_file:  # si a open() no le decimos el modo asume que es de lectura y texto
    csv_reader = csv.DictReader(csv_file)
    for row in csv_reader:
        print(f"{row['nombre']} trabaja como {row['puesto']} y nació en el mes de {row['mes de nacimiento']}.")
