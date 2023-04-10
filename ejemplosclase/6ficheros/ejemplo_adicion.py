"""
Ejemplo de como añadir a un fichero. Lo haremos con el diccionario castellano - inglés en formato CSV.

Autor: Rafael del Castillo Gomariz.
"""
import sys

from ejemplo_escribir_v1_refactorizado import file_exists, agree_with, write_spanish_english_words


def main():
    print("Adición de palabras a un diccionario castellano - inglés")
    print("--------------------------------------------------------")

    filename = input("Nombre del fichero del diccionario: ")
    if not file_exists(filename):
        print("Para añadir palabras al diccionario este debe existir, no es el caso.", file=sys.stderr)
        exit(1)

    dictionary = open_dictionary(filename)
    while True:
        write_spanish_english_words(dictionary)
        if not agree_with("¿Quiere continuar añadiendo palabras al diccionario?"):
            break

    dictionary.close()
    print("Diccionario guardado.")


def open_dictionary(filename):
    try:
        f = open(filename, "at")
        return f
    except PermissionError | FileNotFoundError | ValueError:
        print(f"No se puede abrir {filename}", file=sys.stderr)
        exit(2)



if __name__ == '__main__':
    main()
