"""
Ejemplo de escritura en un fichero json. Lo creamos importando desde un csv.

En la función json.dump() usamos los parámetros ensure_ascii y ident para que los caracteres acentuados salgan y para
que haya saltos de línea y tabulaciones en el json (pretty-printed).

Autor: Rafael del Castillo.
"""
import csv
import json
import os
import sys

FILE_CSV = "agenda.csv"
FILE_JSON = "agenda.json"

if not os.path.exists(FILE_CSV):
    print(f"El fichero {FILE_CSV} no existe. Terminamos...", file=sys.stderr)
    exit(1)

with open(FILE_CSV) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    address_book = []
    # Añadimos cada persona del csv a address_book, mejor sería hacerlo con:
    # address_book = [person for person in csv_reader]
    for person in csv_reader:
        address_book.append(person)

with open(FILE_JSON, "wt") as json_file:
    json.dump(address_book, json_file, ensure_ascii=False, indent=4)

print(f"Exportado {FILE_CSV} a {FILE_JSON}")
