"""
Ejemplo de lectura de un fichero json.

Autor: Rafael del Castillo.
"""
import csv
import json
import os.path
import sys

FILE_JSON = "agenda.json"
FILE_CSV = "agenda_desde_json.csv"

if not os.path.exists(FILE_JSON):  # comprobamos que el fichero existe
    print(f"El fichero {FILE_JSON} no existe. Terminamos...", file=sys.stderr)
    exit(1)

with open(FILE_JSON, "rt") as json_file:
    address_book = json.load(json_file)

with open(FILE_CSV, 'wt') as csv_file:
    fieldnames = address_book[0].keys()
    csv_writer = csv.writer(csv_file)
    csv_writer.writerow(fieldnames)  # cabecera csv

    for person in address_book:
        csv_writer.writerow(person.values())

print(f"Exportado {FILE_JSON} a {FILE_CSV}")
