"""
Queremos obtener las 5 películas "trending topic" semanal o del día en función del género de la misma.
Al usuario le preguntamos si quiere un género concreto o si los quiere todos.

Usaremos la API de themoviedb.org
Para los géneros de las películas: https://developers.themoviedb.org/3/genres/get-movie-list
Para el "trending topic": https://developers.themoviedb.org/3/trending/get-trending

Versión 1.0.
"""

import requests
import os

# Constantes
URL_BASE = "https://api.themoviedb.org/3"  # url a partir de la cual hacemos las peticiones
SEMANAL = "/week"  # parte del endpoint para el trending topic semanal
DIARIO = "/day"  # parte del endpoint para el trending topic diario
PETICION_TRENDING = "/trending/movie"
PETICION_GENEROS = "/genre/movie/list"
TOP = 5  # número de películas a mostrar
API_KEY = os.environ["API_KEY_MOVIEDB"]


# ---------
# Funciones
# ---------
def pedir_temporalizacion():
    while True:
        temp = input("¿Trending Topic semanal o diario? (S/D): ").upper()
        if temp in ["S", "D"]:
            break
    return temp


def generos_peliculas():
    """
    Hace una petición a la API de MOVIEDB para obtener los géneros de las películas
    :return: diccionario de pares: código, descripción
    """
    # construimos endpoint y hacemos petición API REST
    url = URL_BASE + PETICION_GENEROS
    params = {"api_key": API_KEY, "language": "es"}
    response = requests.get(url, params=params)

    # si hay error terminamos
    if response.status_code != 200:
        print("Error al hacer la petición:", response.url, "status:", response.status_code)
        exit(1)

    # construimos diccionario con la respuesta
    lista_generos = response.json()
    generos = dict()
    for g in lista_generos["genres"]:
        generos[g["id"]] = g["name"]

    return generos


def mostrar_generos(generos):
    """
    Muestra por pantalla los géneros de las películas.
    :param generos: diccionario con los géneros.
    """
    print("\nGÉNEROS")
    print("-------")
    for codigo, nombre in generos.items():
        print(f"{codigo}: {nombre}")
    print()


def pedir_genero():
    g = 0  # 0 implica que no filtramos por género

    # ¿filtramos por género?
    while True:
        resp = input("¿Quiere filtrar por algún género de película? (S/N): ").upper()
        if resp in ["S", "N"]:
            break

    # si filtramos por género pedimos el código
    if resp == "S":
        generos = generos_peliculas()  # diccionario géneros, la clave es el código y el valor la descripción
        # mostramos los géneros y pedimos uno de ellos
        while True:
            mostrar_generos(generos)
            try:
                g = int(input("Género: "))
            except ValueError:  # si pone algo que no es entero
                g = 0
            if g in generos.keys():
                break
            print("Código de género erróneo.")

    return g


def trending_topic_pelis(pagina, temporalizacion):
    # construimos endpoint
    url = URL_BASE + PETICION_TRENDING
    if temporalizacion == "S":
        url += SEMANAL
    else:
        url += DIARIO

    # parámetros petición
    params = {"api_key": API_KEY,
              "language": "es",
              "page": str(pagina)}

    # petición API REST
    response = requests.get(url, params=params)
    if response.status_code == 200:  # todo ok
        return response.json()

    # si llegamos aquí hay un error
    print("Error al hacer la petición:", response.url, "status:", response.status_code)
    exit(1)


# ---------
# PRINCIPAL
# ---------

# Pedimos datos

# ¿trending topic semanal o diario?
temporalizacion = pedir_temporalizacion()  # S: semanal, D: diario
# ¿todos los géneros o alguno en particular?
genero = pedir_genero()  # 0: todos los géneros, otro valor: el código del género

# Proceso

print("\nTRENDING TOPIC")
print("--------------")

# inicializamos variables
num_pelis = 0
pagina = 1  # en la primera petición, si hay un género concreto, puede que no obtengamos todas las películas

# ciclo REPETIR hasta que tengamos TOP películas
while True:
    pelis = trending_topic_pelis(pagina, temporalizacion)
    for peli in pelis["results"]:
        if (genero == 0) or (genero in peli['genre_ids']):
            num_pelis += 1
            print(f"{num_pelis}: {peli['title']}")
            if num_pelis == TOP:  # hemos llegado al TOP, no seguimos
                break
    pagina += 1
    if num_pelis == TOP:  # condición de terminación del ciclo (HASTA)
        break
