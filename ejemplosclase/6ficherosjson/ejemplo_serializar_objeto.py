"""
En determinadas ocasiones queremos convertir a JSON un objeto de una clase creada por nosotros, si llamamos a la función
json.dump() para hacerlo obtendremos un error porque el módulo json solo puede manejar tipos primitivos de Python que
tienen un equivalente JSON directo (diccionarios, listas, cadenas, números, etc.).

Para resolver esto, necesitamos crear un codificador personalizado para que nuestra clase JSON sea serializable. Hay
varias formas de hacer que una clase de Python JSON sea serializable, en este ejemplo vamos a ver una forma simple de
hacerlo a través de una agenda cuyos elementos son objetos de la clase Persona.

El módulo json tiene una clase JSONEncoder de la que podemos crear una subclase para implementar una serialización JSON
personalizada. A los métodos json.dump() y json.dumps() podemos pasarle esta clase.

Más información: https://pynative.com/make-python-class-json-serializable/

Autor: Rafael del Castillo Gomariz.
"""
import json
from dataclasses import dataclass
from json import JSONEncoder
from typeguard import typechecked

@typechecked
@dataclass(frozen=True)
class Person:
    name: str
    address: str = ""
    email: str = ""
    phone: str = ""

class PersonEncoder(JSONEncoder):
    def default(self, o):
        return o.__dict__

if __name__ == '__main__':
    FILE_JSON = "agenda.json"
    address_book = [
        Person("Juan", "Calle Falsa 123, 14001 Córdoba", "juan@example.com", "555 - 1234"),
        Person("María", "Avenida Principal 456, 14002 Córdoba", "maria@example.com", "555 - 5678"),
        Person("Pedro", "Calle Secundaria 789, 14003 Córdoba", "pedro@example.com", "555 - 9012"),
        Person("Ana", "Plaza Central 321, 14001 Córdoba", "ana@example.com", "555 - 3456"),
        Person("Luis", "Calle Principal 654, 14001 Córdoba", "luis@example.com", "555 - 7890")
    ]

    with open(FILE_JSON, "wt") as json_file:
        json.dump(address_book, json_file, ensure_ascii=False, indent=4, cls=PersonEncoder)
    print(f"Creado {FILE_JSON}")