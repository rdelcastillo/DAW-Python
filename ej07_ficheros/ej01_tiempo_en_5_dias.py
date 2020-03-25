"""
Usando la API de OpenWeather obtendremos el pronóstico del tiempo de los próximos cinco días, para una ciudad que se le
pide al usuario, mostraremos:

Temperatura media, mínima y máxima (en grados Celsius) para cada día y global.

El programa admite dos parámetros:

- El primero es la ciudad de la que vamos a sacar el pronóstico de la temperatura, si la ciudad es errónea el programa
  termina con un mensaje de error y código 2.
- El segundo es opcional, y si existe, es el directorio donde vamos a crear un fichero html con la información
  formateada como una tabla del pronóstico de la temperatura, si no existe la información se muestra por pantalla.

Consideraciones:

- Este fichero (si se tiene que crear) tendrá por nombre: {CIUDAD}_{FECHA-INICIO}_{FECHA_FIN}, ejemplo:
  "Cordoba_2020-02-27-12.00.00_2020-03-03-09.00.00.html"
- Si el fichero no se puede crear el programa termina con un mensaje de error y código 3.
- Si el programa no recibe ningún parámetro o recibe más de dos terminará con un mensaje de error (código 1)
  diciendo que la sintaxis es incorrecta.
- Si el programa recibe un solo parámetro y este es "-h" el programa muestra un texto explicando qué hace.

Versión 0.1: probamos escribiendo fichero de exto plano (sin marcas html)
"""

import requests
import sys
import os

# Comprobamos si el número de parámetros es correcto
if len(sys.argv) == 1 or len(sys.argv) > 3:
    print("La sintaxis es incorrecta.", file=sys.stderr)
    exit(1)

# Comprobamos si la salida es por pantalla o a un archivo html o hay que mostrar la ayuda
if len(sys.argv) == 3:
    salida_html = True
    directorio = sys.argv[2]
    if directorio[-1] != "/" and directorio[-1] != "\\":
        print("El nombre del directorio tiene que terminar en / ó en \\", file=sys.stderr)
        exit(3)
elif sys.argv[1] == "-h":
    print("Este programa nos da el pronóstico del tiempo de los próximos cinco días para una ciudad.\n")
    print("Sintaxis: python3 ej01_tiempo_en_5_dias.py {CIUDAD} [{DIRECTORIO}]\n")
    print("Si {DIRECTORIO} no se especifica la información se muestra por la pantalla, si se hace se genera un fichero "
          "html en DIRECTORIO con nombre {CIUDAD}_{FECHA-INICIO}_{FECHA_FIN}.\n")
    print("Si {DIRECTORIO} se especifica hay que añadir al final del nombre / (Unix/Linux) ó \\ (Windows).")
    exit(0)
else:
    salida_html = False

ciudad = sys.argv[1]

# petición GET a la API de OpenWeather
url = "https://api.openweathermap.org/data/2.5/forecast"
params = {"q": ciudad, "appid": os.environ["OPEN_WEATHER_KEY"], "units": "metric", "lang": "es"}
response = requests.get(url, params=params)
if response.status_code != 200:
    print("Error al hacer la petición o", ciudad, "no existe:", response.status_code)
    exit(2)
datos = response.json()

# cálculos
dias = dict()  # diccionario con clave el día y valor la lista de mediciones del día
totales = {"temp": [], "temp_min": [], "temp_max": []}  # lista de mediciones de todos los días

for medicion in datos["list"]:
    # fecha y temperatura de la medición
    dia = medicion["dt_txt"][:10]
    temp = float(medicion["main"]["temp"])
    temp_min = float(medicion["main"]["temp_min"])
    temp_max = float(medicion["main"]["temp_max"])

    # si no tenemos datos de ese día creamos una nueva entrada en el diccionario
    if not dias.get(dia):
        dias[dia] = {"temp": [], "temp_min": [], "temp_max": []}
    # añadimos medición
    dias[dia]["temp"].append(temp)
    dias[dia]["temp_min"].append(temp_min)
    dias[dia]["temp_max"].append(temp_max)
    totales["temp"].append(temp)
    totales["temp_min"].append(temp_min)
    totales["temp_max"].append(temp_max)

# resultados
if salida_html:
    # nombre fichero
    fecha_inicio = datos["list"][0]["dt_txt"]  # fecha primera medición
    fecha_fin = datos["list"][-1]["dt_txt"]  # fecha última medición
    nombre_fichero = directorio + ciudad + "_" + fecha_inicio + "_" + fecha_fin
    # sustituimos en el mombre ":" por "." y " " por "-"
    nombre_fichero = nombre_fichero.replace(":", ".").replace(" ", "-")
    # abrimos fichero para escritura
    try:
        fichero = open(nombre_fichero, "wt")
    except IOError:
        print("No se puede crear el fichero html:", nombre_fichero)
        exit(3)
else:
    print()
    fichero = sys.stdout

for dia, temps in dias.items():
    # diario
    temp_med = sum(temps['temp']) / len(temps['temp'])
    temp_min = min(temps['temp_min'])
    temp_max = max(temps['temp_max'])
    print(f"Día {dia[8:]}-{dia[5:7]}-{dia[0:4]}:\t"
          f"Temperatura media: {temp_med:.2f}º, "
          f"mínima: {temp_min}º y máxima: {temp_max}º. "
          f"Mediciones: {len(temps['temp'])}", file=fichero)
print()

# global
temp_med = sum(totales['temp']) / len(totales['temp'])
temp_min = min(totales['temp_min'])
temp_max = max(totales['temp_max'])
print(f"TOTALES:\t\tTemperatura media: {temp_med:.2f}º, "
      f"mínima: {temp_min}º y máxima: {temp_max}º", file=fichero)

# fin
if salida_html:
    fichero.close()
    print("Generado fichero", nombre_fichero, "con los datos.")
