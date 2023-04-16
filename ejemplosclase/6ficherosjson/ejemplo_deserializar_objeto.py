"""
Para deserializar un json que tiene objetos de clases específicas podemos usar el parámetro "object_hook" que permite
especificar una función de decodificación personalizada que se utilizará para convertir los objetos JSON en objetos
Python.

Esta función se invoca para cada objeto JSON que se decodifica y recibe un diccionario como argumento. La función debe
devolver un objeto Python que reemplace al diccionario original en la salida. Si no encuentra el objeto Python
correspondiente, debe devolver el diccionario original sin cambios.

Más información: https://pynative.com/python-convert-json-data-into-custom-python-object/

Autor: Rafael del Castillo Gomariz.
"""
import json
import os
import sys

from ejemplo_serializar_objeto import Person

FILE_JSON = "agenda.json"

def main():
    if not os.path.exists(FILE_JSON):
        print(f"El fichero {FILE_JSON} no existe. Terminamos...", file=sys.stderr)
        exit(1)

    with open(FILE_JSON) as json_file:
        address_book = json.load(json_file, object_hook=person_decoder)

    print(address_book)

def person_decoder(p):
    """
    Función de decodificación personalizada que debe devolver el objeto Python correspondiente como resultado.
    Si no encuentra el objeto Python correspondiente, debe devolver el diccionario original sin cambios.
    """
    if 'name' in p and 'address' in p and 'email' in p and 'phone' in p:
        return Person(p['name'], p['address'], p['email'], p['phone'])
        # otra opción: return namedtuple('X', p.keys())(*p.values())
    return p

if __name__ == '__main__':
    main()
