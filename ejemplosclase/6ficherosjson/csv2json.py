"""
Ejemplo de escritura en un fichero json. Lo creamos importando desde un csv que recibimos como parámetro.

En la función json.dump() usamos los parámetros ensure_ascii y ident para que los caracteres acentuados salgan y para
que haya saltos de línea y tabulaciones en el json (pretty-printed).

Autor: Rafael del Castillo.
"""
import csv
import json
import os
import sys

def main():
    file_csv, file_json = get_filenames()

    with open(file_csv) as csv_file:
        csv_reader = csv.DictReader(csv_file)
        record_list = []
        # Añadimos cada persona del csv a address_book, mejor sería hacerlo con:
        # address_book = [record for record in csv_reader]
        for record in csv_reader:
            record_list.append(record)

    with open(file_json, "wt") as json_file:
        json.dump(record_list, json_file, ensure_ascii=False, indent=4)

    print(f"Exportado {file_csv} a {file_json}")

def get_filenames():
    check_errors()
    csv_filename = sys.argv[1]
    json_filename = csv_filename[:-4] + ".json"
    return csv_filename, json_filename


def check_errors():
    if len(sys.argv) != 2:
        print("Este programa debe recibir un fichero CSV como argumento", file=sys.stderr)
        exit(1)
    csv_filename = sys.argv[1]
    if csv_filename[-4:] != ".csv":
        print("El fichero recibido como argumento no tiene extensión csv", file=sys.stderr)
        exit(2)
    if not os.path.exists(csv_filename):
        print(f"El fichero {csv_filename} no existe. Terminamos...", file=sys.stderr)
        exit(3)


if __name__ == '__main__':
    main()
