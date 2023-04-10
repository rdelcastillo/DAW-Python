"""
Ejemplo de escritura en un fichero csv usando el módulo csv y un objeto lector.

Autor: Rafael del Castillo.
"""
import csv

FILE = "datos.csv"

with open(FILE, mode='at') as csv_file:
    csv_writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    # delimiter es el carácter utilizado para separar cada campo. El valor predeterminado es la coma (',').
    # quotechar es el carácter utilizado para rodear los campos. El valor predeterminado es una comilla doble ('"').

    csv_writer.writerow(['Pepe López', 'Contable', 'noviembre'])
    csv_writer.writerow(['Lola Flores', 'IT', 'enero'])
