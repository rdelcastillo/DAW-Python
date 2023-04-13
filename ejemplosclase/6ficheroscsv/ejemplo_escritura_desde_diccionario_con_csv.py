"""
Ejemplo de escritura en un fichero csv usando el módulo csv y un dicccionario.

Autor: Rafael del Castillo.
"""
import csv

FILE = "palabras.csv"

with open(FILE, 'wt') as csv_file:
    csv_writer = csv.DictWriter(csv_file, fieldnames=['castellano', 'inglés'])

    csv_writer.writeheader()
    csv_writer.writerow({'castellano': 'leche', 'inglés': 'milk'})
    csv_writer.writerow({'inglés': 'apple', 'castellano': 'manzana'})
