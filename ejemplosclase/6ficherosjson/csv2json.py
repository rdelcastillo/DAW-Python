"""
Ejemplo de escritura en un fichero json. Lo creamos importando desde un csv.

Autor: Rafael del Castillo.
"""
import csv
import json
import os
import sys

FILE_JSON = "agenda_desde_csv.json"
FILE_CSV = "agenda.csv"

if not os.path.exists(FILE_CSV):
    print(f"El fichero {FILE_CSV} no existe. Terminamos...", file=sys.stderr)
    exit(1)

with open(FILE_CSV) as csv_file:
    csv_reader = csv.DictReader(csv_file)
    address_book = [person for person in csv_reader]

with open(FILE_JSON, "wt") as json_file:
    json.dump(address_book, json_file, ensure_ascii= False)

print(f"Exportado {FILE_CSV} a {FILE_JSON}")
