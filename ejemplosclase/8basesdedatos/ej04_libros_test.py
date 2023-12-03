"""
En este programa creamos una instancia de la clase DAO que deseamos utilizar (en este caso, XmlLibroDAO) y luego
ejecutamos un bucle infinito que muestra el menú y espera la entrada del usuario para ejecutar la opción correspondiente.

Puedes cambiar la instancia dao a JsonBookDAO o MySqlBookDAO según tus necesidades, y asegúrate de tener los archivos de
datos libros.xml o libros.json disponibles según la clase DAO que elijas.
"""
import sys
from ej04_libros import XmlBookDAO, JsonBookDAO, MySqlBookDAO, Book


def main():
    while True:
        show_menu()
        opc = input("Ingrese una opción: ")

        if opc == "1":
            add_book()
        elif opc == "2":
            remove_book()
        elif opc == "3":
            list_books()
        elif opc == "4":
            sys.exit()
        else:
            print("Opción inválida. Por favor, ingrese una opción válida.")

def show_menu():
    print("1. Agregar libro")
    print("2. Eliminar libro")
    print("3. Listar libros")
    print("4. Salir")
    print()

def add_book():
    title = input("Ingrese el título del libro: ")
    author = input("Ingrese el autor del libro: ")
    year_publication = int(input("Ingrese el año de publicación del libro: "))
    book = Book(title, author, year_publication)
    dao.add_book(book)
    print("Libro agregado exitosamente.")

def remove_book():
    title = input("Ingrese el título del libro a eliminar: ")
    book = dao.get_book(title)
    if book:
        dao.remove_book(book)
        print("Libro eliminado exitosamente.")
    else:
        print("El libro no existe.")

def list_books():
    books = dao.get_books()
    if books:
        print("Lista de libros:")
        for book in books:
            print(f"Título: {book.title}")
            print(f"Autor: {book.author}")
            print(f"Año de publicación: {book.year_publication}")
            print()
    else:
        print("No hay libros para mostrar.")

if __name__ == "__main__":
    dao = XmlBookDAO()  # Puedes cambiar a JsonBookDAO o MySqlBookDAO según tus necesidades
    main()
