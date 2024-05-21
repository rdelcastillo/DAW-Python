"""
Ejemplo de pila sobre la que podemos iterar y acceder a sus elementos.
"""
class Stack:
    def __init__(self):
        self.__items = []

    def push(self, item):
        self.__items.append(item)

    def pop(self):
        try:
            return self.__items.pop()
        except IndexError:
            raise IndexError("pop from an empty stack") from None

    def __iter__(self):
        return iter(self.__items)

    def __getitem__(self, index):
        return self.__items[index]

    def __len__(self):
        return len(self.__items)
