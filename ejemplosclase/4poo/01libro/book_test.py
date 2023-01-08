"""
Prueba de la clase Book.

Ejemplo sacado del libro "Aprende Java con Ejercicios" de Luis José Sánchez:
https://github.com/LuisJoseSanchez/aprende-java-con-ejercicios

Adaptado a Python por Rafael del Castillo Gomariz.

Fecha: 7/01/2023.
"""
from book import Book

book1 = Book()  # instanciamos un objeto de la clase Book
book1.isbn = '9788467016901'
book1.title = 'El ingenioso hidalgo don Quijote de la Mancha (1ª parte de El Quijote)'
book1.author = 'Miguel de Cervantes Saavedra'
book1.number_pages = 920

print('Creado objeto "Book" con datos:')
print('ISBN:', book1.isbn)
print('Título:', book1.title)
print('Autor:', book1.author)
print('Número de páginas:', book1.number_pages, '\n')

book2 = Book()  # instanciamos otro objeto de la clase Book
book2.isbn = '9788415973621'
book2.title = 'El ingenioso caballero don Quijote de la Mancha (2ª parte de El Quijote)'
book2.author = 'Miguel de Cervantes Saavedra'
book2.number_pages = 736

print('Creado objeto "Book" con datos:')
print('ISBN:', book2.isbn)
print('Título:', book2.title)
print('Autor:', book2.author)
print('Número de páginas:', book2.number_pages)
