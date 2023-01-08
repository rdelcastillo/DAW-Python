"""
Definición de la clase Libro con los atributos isbn, autor, título y número de páginas.

Ejemplo sacado del libro "Aprende Java con Ejercicios" de Luis José Sánchez:
https://github.com/LuisJoseSanchez/aprende-java-con-ejercicios

Adaptado a Python por Rafael del Castillo Gomariz.

Fecha: 7/01/2023.
"""

class Book:

    def __init__(self):
        """
        Método constructor que es llamado cada que se instancie un objeto de esta clase.
        En este ejemplo solo crearemos los atributos (públicos). Anteponer 'self' es necesario para indicar que estos
        pertenecen al objeto instanciado.
        """
        self.isbn = ''
        self.title = ''
        self.author = ''
        self.number_pages = 0
