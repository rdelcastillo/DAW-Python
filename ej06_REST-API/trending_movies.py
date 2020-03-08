"""
Queremos obtener las 5 películas "trending topic" semanal o del día en función del género de la misma.
Al usuario le preguntamos si quiere un género concreto o si los quiere todos.

Usaremos la API de themoviedb.org
Para los géneros de las películas: https://developers.themoviedb.org/3/genres/get-movie-list
Para el "trending topic": https://developers.themoviedb.org/3/trending/get-trending

Versión 0.1: construimos esqueleto.
"""

# Constantes
URL_BASE = "https://developers.themoviedb.org/3"    # url a partir de la cual hacemos las peticiones
SEMANAL = "/week"   # parte del endpoint para el trending topic semanal
DIARIO = "/day"     # parte del endpoint para el trending topic diario
PETICION_TRENDING = "/trending/movie"
PETICION_GENEROS = "/genres/get-movie-list"
TOP = 5             # número de películas a mostrar

# Pedimos datos

# ¿trending topic semanal o diario?
temporalizacion = pedir_temporalizacion()   # S: semanal, D: diario

# ¿todos los géneros o alguno en particular?
genero = pedir_genero()                     # 0: todos los géneros, otro valor: el código del género

# Proceso

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
            if num_pelis == TOP:    # hemos llegado al TOP, no seguimos
                break
    pagina += 1
    if num_pelis == 5:  # condición de terminación del ciclo (HASTA)
        break

