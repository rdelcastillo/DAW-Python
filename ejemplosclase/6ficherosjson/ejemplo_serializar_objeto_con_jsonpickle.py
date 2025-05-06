"""
Otra alternativa para serializar y deserializar objetos Python complejos a JSON es usar librerías que extienden JSON
como jsonpickle.

En este ejemplo serializamos la clase Persona que ya usamos para mostrar el uso de JSONEncoder.

Autor: Rafael del Castillo Gomariz.
"""
import jsonpickle
from ejemplo_serializar_objeto import Person

FILE_JSON = "agenda.json"

# Configurar jsonpickle para usar una versión de json que no escape ASCII
jsonpickle.set_preferred_backend('json')
jsonpickle.set_encoder_options('json', ensure_ascii=False)

address_book = [
    Person("Juan", "Calle Falsa 123, 14001 Córdoba", "juan@example.com", "555 - 1234"),
    Person("María", "Avenida Principal 456, 14002 Córdoba", "maria@example.com", "555 - 5678"),
    Person("Pedro", "Calle Secundaria 789, 14003 Córdoba", "pedro@example.com", "555 - 9012"),
    Person("Ana", "Plaza Central 321, 14001 Córdoba", "ana@example.com", "555 - 3456"),
    Person("Luis", "Calle Principal 654, 14001 Córdoba", "luis@example.com", "555 - 7890")
]

with open(FILE_JSON, "wt") as json_file:
    json_file.write(jsonpickle.encode(address_book, indent=4))

print(f"Creado {FILE_JSON}")
