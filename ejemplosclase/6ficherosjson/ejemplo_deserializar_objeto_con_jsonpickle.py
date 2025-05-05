"""
Otra alternativa para serializar y deserializar objetos Python complejos a JSON es usar librerías que extienden JSON
como jsonpickle.

En este ejemplo deserializamos la clase Persona que ya usamos para mostrar el uso de JSONEncoder.

Autor: Rafael del Castillo Gomariz.
"""
import jsonpickle
import os
import sys

FILE_JSON = "agenda.json"

if __name__ == '__main__':
    if not os.path.exists(FILE_JSON):
        print(f"El fichero {FILE_JSON} no existe. Terminamos...", file=sys.stderr)
        exit(1)

    with open(FILE_JSON) as json_file:
        address_book = jsonpickle.decode(json_file.read())

    print(address_book)
