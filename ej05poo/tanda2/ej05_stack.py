"""
Clase que representa una estructura de datos tipo pila (stack).

Permitirá estas operaciones:

- Crear la pila con o sin valores iniciales o a partir de otra pila.
- Obtener el número de elementos almacenados (tamaño).
- Saber si está vacía.
- Vaciarla completamente.
- Apilar (push): se añade un elemento a la pila. Se añade al principio de esta.
- Desapilar (pop): se saca (debe devolverse) el elemento superior de la pila y se elimina.
- Leer el elemento superior de la pila sin retirarlo (top).

Autor: Rafael del Castillo Gomariz
"""
from __future__ import annotations
from typeguard import typechecked

@typechecked
class Stack:

    def __init__(self, *values: int):
        self.__values = list(values)

    @classmethod
    def from_stack(cls, other: Stack):
        new_stack = cls()  # o Stack()
        new_stack.__values = other.__values.copy()  # si no es una copia desde la nueva pila podríamos cambiar la 1ª
        return new_stack

    def __repr__(self):
        return f"{self.__class__.__name__}(values={self.__values})"

    def __str__(self):
        str_ = ""
        for n in self.__values:
            str_ += f"{n}\n"
        return str_

    @property
    def size(self):
        return len(self.__values)

    def is_empty(self):
        return self.size == 0

    def clear(self):
        self.__values.clear()

    def push(self, value):
        self.__values.insert(0, value)

    def pop(self):
        return self.__values.pop(0)

    def top(self):
        return self.__values[0]

if __name__ == '__main__':
    stack1 = Stack(1,2,3,4,5)
    stack2 = Stack.from_stack(stack1)
    print(f"Creadas {stack1} y {stack2}")

    print(f"Añado A y B a {stack1}")
    stack1.push('A')
    stack1.push('B')
    print("Resultado:", stack1)

    print(f"Quito dos elementos de {stack2}")
    print(f"Quito {stack2.pop()}, {stack2.pop()}")
    print("Resultado:", stack2)
