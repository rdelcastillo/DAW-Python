"""
Imagina que estás creando un programa para administrar una biblioteca. Tienes una clase llamada `Libro` que representa
un libro con propiedades como título, autor y año de publicación.

El patrón DAO (Data Access Object) es una forma de organizar tu código para separar la lógica de cómo se accede y se
guarda la información de los libros de la lógica de negocio de tu programa.

En lugar de acceder directamente a la base de datos o a algún almacenamiento de datos, utilizas una clase llamada
`LibroDAO` que actúa como intermediario entre tu programa y la fuente de datos. Esta clase DAO tiene métodos para
realizar operaciones como agregar un libro, obtener un libro por su título o eliminar un libro.

El beneficio principal del patrón DAO es que permite mantener tu lógica de negocio separada de cómo se almacenan los
datos. Si en el futuro cambias la forma en que se almacenan los libros (por ejemplo, de una base de datos a un archivo
de texto), solo necesitas modificar la implementación del DAO, sin tener que cambiar todo tu programa.

Aquí hay un ejemplo simplificado en Python.

En este ejemplo, creamos la clase `Libro` que representa un libro y la clase `LibroDAO` que actúa como el DAO para
interactuar con los libros. El DAO mantiene una lista de libros en la memoria, pero en una aplicación real podría estar
conectado a una base de datos.

Utilizamos métodos como `agregar_libro`, `obtener_libro_por_titulo` y `eliminar_libro` en el DAO para realizar
operaciones relacionadas con los libros.
"""

from abc import ABC, abstractmethod
import xml.etree.ElementTree as ET
import json
import mysql.connector


class Book:
    def __init__(self, title, author, year_publication):
        self.title = title
        self.author = author
        self.year_publication = year_publication


class BookDAO(ABC):
    @abstractmethod
    def add_book(self, book):
        pass

    @abstractmethod
    def get_book(self, title):
        pass

    @abstractmethod
    def get_books(self):
        pass

    @abstractmethod
    def remove_book(self, book):
        pass


class XmlBookDAO(BookDAO):
    def __init__(self):
        self.tree = ET.parse("libros.xml")
        self.root = self.tree.getroot()
        self.books = []  # TODO meter los libros en la lista

    def add_book(self, book):
        self.books.append(book)
        book_element = ET.Element("book")
        title_element = ET.SubElement(book_element, "title")
        title_element.text = book.title
        author_element = ET.SubElement(book_element, "author")
        author_element.text = book.author
        year_element = ET.SubElement(book_element, "year")
        year_element.text = str(book.year_publication)
        self.root.append(book_element)
        self.tree.write("libros.xml")

    def get_book(self, title):
        for book in self.books:
            if book.title == title:
                return book
        return None

    def get_books(self):
        return self.books.copy()

    def remove_book(self, book):
        if book in self.books:
            self.books.remove(book)
            for book_element in self.root.findall("book"):
                if book_element.find("title").text == book.title:
                    self.root.remove(book_element)
                    self.tree.write("libros.xml")


class JsonBookDAO(BookDAO):
    def __init__(self):
        try:
            with open("libros.json", "r") as file:
                self.books = json.load(file)
        except FileNotFoundError:
            pass
        self.books = []  # TODO meter los libros en la lista

    def add_book(self, book):
        self.books.append({
            "title": book.title,
            "author": book.author,
            "year_publication": book.year_publication
        })
        with open("libros.json", "w") as file:
            json.dump(self.books, file)

    def get_book(self, title):
        for libro in self.books:
            if libro["title"] == title:
                return Book(libro["title"], libro["author"], libro["year_publication"])
        return None

    def get_books(self):
        return self.books

    def remove_book(self, book):
        for libro_json in self.books:
            if libro_json["title"] == book.title:
                self.books.remove_book(libro_json)
                with open("libros.json", "w") as file:
                    json.dump(self.books, file)
                break


class MySqlBookDAO(BookDAO):
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="tu_usuario",
            password="tu_contraseña",
            database="nombre_de_la_base_de_datos"
        )

    def add_book(self, book):
        query = "INSERT INTO libros (titulo, autor, anio_publicacion) VALUES (%s, %s, %s)"
        values = (book.title, book.author, book.year_publication)
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        self.connection.commit()
        cursor.close()

    def get_book(self, title):
        query = "SELECT * FROM libros WHERE titulo = %s"
        values = (title,)
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        result = cursor.fetchone()
        cursor.close()

        if result:
            libro = Book(result[0], result[1], result[2])
            return libro
        else:
            return None

    def remove_book(self, book):
        query = "DELETE FROM libros WHERE titulo = %s"
        values = (book.title,)
        cursor = self.connection.cursor()
        cursor.execute(query, values)
        self.connection.commit()
        cursor.close()
