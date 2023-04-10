"""
Ejemplo de escribir en un fichero. Crearemos un diccionario castellano - inglés en formato CSV.

Programa anterior refactorizado (se puede hacer aún más).

Autor: Rafael del Castillo Gomariz.
"""
import sys


def main():
    print("Creación de un diccionario castellano - inglés")
    print("----------------------------------------------")

    filename = input("Nombre del fichero para guardar el diccionario: ")
    if file_exists(filename) and not agree_with("El fichero ya existe ¿sobreescribimos?"):
       print("Programa abortado...", file=sys.stderr)
       exit(1)

    dictionary = create_dictionary(filename)
    while True:
        write_spanish_english_words(dictionary)
        if not agree_with("¿Quiere continuar añadiendo palabras al diccionario?"):
            break

    dictionary.close()
    print("Diccionario guardado.")


def file_exists(filename):
    try:
        f = open(filename, "rt")
        f.close()
        return True
    except FileNotFoundError:
        return False


def agree_with(prompt):
    while True:
        resp = input(f"{prompt} (S/N) ").upper()
        if resp == "N":
            return False
        elif resp == "S":
            return True
        else:
            print("Debe responder S o N")


def create_dictionary(filename):
    try:
        f = open(filename, "wt")
        print("Palabra,Traducción", file=f)  # Creo la cabecera del CSV
        return f
    except PermissionError | FileNotFoundError | ValueError:
        print(f"No se puede escribir en {filename}", file=sys.stderr)
        exit(2)


def write_spanish_english_words(dictionary):
    spanish_word = input("Dame una palabra en castellano: ")
    english_word = input("Dame la traducción en inglés: ")
    dictionary.write(f"{spanish_word},{english_word}\n")


if __name__ == '__main__':
    main()
