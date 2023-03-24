"""
Mini-diccionario español-inglés que contiene 20 palabras (con su correspondiente traducción). El programa pedirá una
palabra en español y dará la correspondiente traducción en inglés.

Ejercicio del libro "Aprende Java con Ejercicios", edición 2019.

Autor: Rafael del Castillo Gomariz.
"""

SPANISH_ENGLISH_DICT = {"uno":"one", "dos":"two", "tres":"three", "cuatro":"four", "cinco":"five", "seis":"six",
                        "siete":"seven", "ocho":"eight", "nueve":"nine", "diez":"ten", "once":"eleven", "doce":"twelve",
                        "trece":"thirteen", "catorce":"fourteen", "quince":"fifteen", "dieciséis":"sixteen",
                        "diecisiete":"seventeen", "dieciocho":"eighteen", "diecinueve":"nineteen", "veinte":"twenty"}


def main():
    print("Mini-diccionario español-inglés")
    print("-------------------------------")

    while True:
        # Pedimos la palabra a traducir, si es una cadena vacía terminamos
        spanish_word = input("Palabra a traducir (Intro para terminar): ")
        if spanish_word == "":
            break

        # Buscamos la palabra, si está mostramos la traducción
        english_word = SPANISH_ENGLISH_DICT.get(spanish_word.lower())
        if english_word is not None:
            print(f"Traducción: {english_word}")
        else:
            print(f"{spanish_word} no está en el diccionario")

    print("\n¡Hasta la próxima! :-)")


if __name__ == '__main__':
    main()
