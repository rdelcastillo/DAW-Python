"""
Programa que calcule la estatura media, mínima y máxima en centímetros de personas de diferentes países.

El array que contiene los nombres de los países es el siguiente: [“España”, “Rusia”, “Japón”, “Australia”]

Los datos sobre las estaturas se deben simular mediante un array de 4 filas por 10 columnas con números aleatorios
generados al azar entre 140 y 210. Los decimales de la media se pueden despreciar.

Los nombres de los países se deben mostrar utilizando el array de países (no se pueden escribir directamente).
"""
import random
from statistics import mean

COLUMNS = 10
MIN_HEIGHT = 140
MAX_HEIGHT = 210
LEN_COUNTRY_NAME = 10
LEN_HEIGHT = 3

countries = ["España", "Rusia", "Japón", "Australia"]
heights_by_country = [[0] * COLUMNS for _ in range(len(countries))]

# Generación de datos aleatorios
for country in heights_by_country:
    for i in range(len(country)):
        country[i] = random.randint(MIN_HEIGHT, MAX_HEIGHT)

# Salida de datos
print(" "*(LEN_COUNTRY_NAME+3) + " "*COLUMNS*(LEN_HEIGHT+1) + "MED MIN MAX")    # cabecera
for row in range(len(countries)):
    print(f"{countries[row]+':':{LEN_COUNTRY_NAME}} ", end="")
    country_heights = heights_by_country[row]
    for height in country_heights:
        print(f"{height:{LEN_HEIGHT}} ", end="")
    print(f"| {round(mean(country_heights)):{LEN_HEIGHT}} " # altura media, máxima y mínima
          f"{max(country_heights):{LEN_HEIGHT}} {min(country_heights):{LEN_HEIGHT}}")