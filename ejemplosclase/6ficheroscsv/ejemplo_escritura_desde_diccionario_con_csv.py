"""
Ejemplo de escritura en un fichero csv usando el módulo csv y un diccionario.

Autor: Rafael del Castillo.
"""

import csv

FILE = "palabras.csv"
KEYS = ['castellano', 'inglés']

def main():
    with open(FILE, 'wt') as csv_file:
        csv_writer = csv.DictWriter(csv_file, fieldnames=KEYS)

        csv_writer.writeheader()
        csv_writer.writerow(dict_translation('leche', 'milk'))
        csv_writer.writerow(dict_translation('manzana', 'apple'))


def dict_translation(spain_word, english_word):
    return {KEYS[0]: spain_word, KEYS[1]: english_word}


if __name__ == '__main__':
    main()
