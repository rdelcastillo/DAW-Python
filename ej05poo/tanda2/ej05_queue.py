"""
Clase que represente una estructura de datos tipo cola (queue).

Permitirá estas operaciones:

- Crear la cola con o sin valores iniciales o a partir de otra cola.
- Obtener el número de elementos almacenados (tamaño).
- Saber si la cola está vacía.
- Vaciar completamente la cola.
- Encolar (enqueue): se añade un elemento a la cola. Se añade al final de esta.
- Desencolar (dequeue): se saca (debe devolverse) y se elimina el elemento frontal de la cola (el primero que entró)
- Leer el elemento frontal de la cola, es decir, el primer elemento que entró, sin retirarlo (front).

Autor: Rafael del Castillo Gomariz.
"""
from typeguard import typechecked

@typechecked
class Queue:

    def __init__(self, *values):
        if len(values) == 1 and isinstance(values[0], Queue):
            other = values[0]
            self.__values = list(other.__values)
        else:
            self.__values = list(values)

    def __repr__(self):
        return f"{self.__class__.__name__}(values={self.__values})"

    @property
    def size(self):
        return len(self.__values)

    def is_empty(self):
        return self.size == 0

    def clear(self):
        self.__values.clear()

    def enqueue(self, value):
        self.__values.append(value)

    def dequeue(self):
        return self.__values.pop(0)

    def top(self):
        return self.__values[0]

if __name__ == '__main__':
    queue1 = Queue(1, 2, 3, 4, 5)
    queue2 = Queue(queue1)
    print(f"Creadas {queue1} y {queue2}")

    print(f"Añado A y B a {queue1}")
    queue1.enqueue('A')
    queue1.enqueue('B')
    print("Resultado:", queue1)

    print(f"Quito dos elementos de {queue2}")
    print(f"Quito {queue2.dequeue()}, {queue2.dequeue()}")
    print("Resultado:", queue2)