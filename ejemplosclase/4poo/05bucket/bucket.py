"""
Implementación de la clase 'Cubo'. Para saber qué atributos deben definirse, nos preguntamos qué características tienen
los cubos (igual que hicimos con la clase GatoSimple). Todos los cubos tienen una determinada capacidad, un color, están
hechos de un determinado material (plástico, latón, etc.) y puede que tengan asa o puede que no. Un cubo se fabrica con
el propósito de contener líquido, por tanto, otra característica es la cantidad de litros de líquido que contiene en un
momento determinado.

Por ahora, solo nos interesa saber la capacidad máxima (que no podrá cambiar) y los litros que contiene el cubo en cada
momento, así que esos serán los atributos que tendremos en cuenta.

En este ejemplo usamos el método mágico __str__() para pintar el cubo y __repr__() para la representación canónica del
objeto.

Ejemplo sacado del libro "Aprende Java con Ejercicios" de Luis José Sánchez:
https://github.com/LuisJoseSanchez/aprende-java-con-ejercicios

Adaptado a Python por Rafael del Castillo Gomariz.

Fecha: 15/01/2023.
"""

class Bucket:

    def __init__(self, capacity, content=0):
        if not isinstance(capacity, int) or capacity <= 0:
            raise ValueError(f"La capacidad del cubo tiene que ser un valor entero positivo, recibido {capacity}")
        self.__capacity = capacity
        self.content = content

    @property
    def capacity(self):
        return self.__capacity

    @property
    def content(self):
        return self.__content

    @content.setter
    def content(self, value):
        if not isinstance(value, int) or value < 0 or value > self.capacity:
            raise ValueError(f"El contenido del cubo tiene que ser un valor entero positivo y menor o igual a su "
                             f"capacidad, recibido {value}")
        self.__content = value

    def empty(self):
        self.content = 0

    def fill(self):
        self.content = self.capacity

    def dump_in(self, destination):
        """
        Vuelca el contenido de un cubo sobre otro. Antes de echar el agua se comprueba cuánto le cabe al cubo destino.
        """
        if not isinstance(destination, Bucket):
            raise ValueError(f"Un cubo solo se puede volcar en otro cubo, recibido {destination}")
        free_capacity_at_destination = destination.capacity - destination.content
        if self.content <= free_capacity_at_destination:
            destination.content += self.content
            self.empty()
        else:
            self.content -= free_capacity_at_destination
            destination.fill()

    def __str__(self):
        """
        Devuelve una cadena con el cubo dibujado. Se muestran los bordes del cubo con el carácter # y el agua que
        contiene con el carácter ~
        """
        bucket_str = ""
        for _ in range(self.capacity, self.content, -1):
            bucket_str += "#          #\n"
        for _ in range(self.content, 0, -1):
            bucket_str += "#~~~~~~~~~~#\n"
        bucket_str += "############"
        return bucket_str

    def __repr__(self):
        """
        Devuelve la representación canónica del objeto, con este valor deberíamos poder construir el objeto.
        """
        return f"Bucket({self.capacity}, {self.content})"