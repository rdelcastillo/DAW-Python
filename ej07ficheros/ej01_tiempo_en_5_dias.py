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

Versión 2.0. Modularizar el programa.
"""

import requests
import sys
import os


def mostrar_ayuda():
    """
    Muestra la sintaxis de este programa y su funcionalidad.
    """
    print("Este programa nos da el pronóstico del tiempo de los próximos cinco días para una ciudad.\n")
    print("Sintaxis: python3 ej01_tiempo_en_5_dias.py {CIUDAD} [{DIRECTORIO}]\n")
    print("Si {DIRECTORIO} no se especifica la información se muestra por la pantalla, si se hace se genera un fichero "
          "html en DIRECTORIO con nombre {CIUDAD}_{FECHA-INICIO}_{FECHA_FIN}.\n")
    print("Si {DIRECTORIO} se especifica hay que añadir al final del nombre / (Unix/Linux) ó \\ (Windows).")


def tiempo_en_5dias(ciudad):
    """
    Consulta en la API de Open Weather el pronóstico del tiempo para los próximos cinco días.
    :param ciudad: Localidad para que la hacemos la consulta.
    :return: JSON con las mediciones del tiempo (40)
    """
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {"q": ciudad, "appid": os.environ["OPEN_WEATHER_KEY"], "units": "metric", "lang": "es"}
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("Error al hacer la petición o", ciudad, "no existe:", response.status_code, file=sys.stderr)
        exit(2)
    return response.json()


def calculos_temperatura(dias, totales, datos):
    """
    Calcula las temperaturas media, máxima y mínima diarias, y la global.
    :param dias: lista donde guardamos los datos diarios.
    :param totales: diccionario donde guardamos los datos globales.
    :param datos: JSON con los datos devueltos con la API de OpenWeathers
    """
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


def fichero_html(ciudad, datos_mediciones):
    """
    Abre para escritura el fichero donde guardaremos la salida html.
    :param ciudad: Localidad de la que hacemos las mediciones.
    :param datos_mediciones: JSON con las mediciones de OpenWeathers
    :return: manejador del fichero
    """
    # nombre fichero: {CIUDAD}_{FECHA-INICIO}_{FECHA_FIN}
    # ejemplo: "Cordoba_2020-02-27-12.00.00_2020-03-03-09.00.00.html"
    fecha_inicio = datos_mediciones["list"][0]["dt_txt"]  # fecha primera medición
    fecha_fin = datos_mediciones["list"][-1]["dt_txt"]  # fecha última medición
    nombre_fichero = directorio + ciudad + "_" + fecha_inicio + "_" + fecha_fin + ".html"
    # sustituimos en el nombre ":" por "." y " " por "-"
    nombre_fichero = nombre_fichero.replace(":", ".").replace(" ", "-")
    # abrimos fichero para escritura
    try:
        fichero = open(nombre_fichero, "wt")
    except IOError:
        print("No se puede crear el fichero html:", nombre_fichero)
        exit(3)
    return fichero


# Funciones para mostrar las temperaturas
def escribe_valores_dia(dia, temps, fichero):
    """
    Escribirá la temperatura media, mínima y máxima del día que hemos pasado como parámetro y el número de
    mediciones.
    :param fichero: manejador de fichero donde se escribe el html. None si la salida es por pantalla.
    :param dia: día en el que se han tomado los valores de la temperatura.
    :param temps: mediciones del día.
    :param salida_html: si es verdadero la salido es en un fichero
    """

    # cálculos y formateo del día
    dia = f"{dia[8:]}-{dia[5:7]}-{dia[0:4]}"  # formato dd-mm-aaaa
    temp_med = sum(temps['temp']) / len(temps['temp'])
    temp_min = min(temps['temp_min'])
    temp_max = max(temps['temp_max'])

    # muestro la información o en el fichero html o en pantalla
    if fichero:
        fichero.write(fila_html(dia, temp_med, temp_min, temp_max, len(temps['temp'])))
    else:
        print(f"Día {dia}:\t"
              f"Temperatura media: {temp_med:.2f}º, "
              f"mínima: {temp_min}º y máxima: {temp_max}º. "
              f"Mediciones: {len(temps['temp'])}")


def escribe_valores_totales(totales, fichero, mediciones):
    """
    Escribirá la temperatura media, mínima y máxima global que hemos pasado como parámetro y el número de
    mediciones.
    :param mediciones: número total de mediciones realizadas,
    :param totales: diccionario con los datos globales de las mediciones
    :param fichero: manejador de fichero donde se escribe el html. None si la salida es por pantalla.
    """

    # cálculos
    temp_med = sum(totales['temp']) / len(totales['temp'])
    temp_min = min(totales['temp_min'])
    temp_max = max(totales['temp_max'])
    if fichero:
        fichero.write(fin_html(temp_med, temp_min, temp_max, mediciones))
        fichero.close()
        print("Generado fichero", fichero.name, "con los datos.")
    else:
        print(f"\nTOTALES:\t\tTemperatura media: {temp_med:.2f}º, "
              f"mínima: {temp_min}º y máxima: {temp_max}º")


# Funciones para manejar el html
def inicio_html(ciudad):
    """
    :param ciudad:
    :return: inicio del html del resumen del pronóstico del tiempo.
    """
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lectura de temperaturas en {ciudad}</title>
</head>
<body>
    <center><p>Este programa nos muestra los resultados de las mediciones para los próximos 5 días en {ciudad}</p>
        <table border="1">
            <tr>
                <th>Día</th>
                <th>Temperatura Media</th>
                <th>Temperatura Mínima</th>
                <th>Temperatura Máxima</th>
                <th>Nº Mediciones</th>
            </tr>"""


def fila_html(dia, temp_med, temp_min, temp_max, mediciones):
    return f"""
            <tr>
                <td><center>{dia}</center></td>
                <td><center>{temp_med:.2f}º</center></td>
                <td><center>{temp_min}º</center></td>
                <td><center>{temp_max}º</center></td>
                <td><center>{mediciones}</center></td>
            </tr>"""


def fin_html(temp_med, temp_min, temp_max, mediciones):
    return f"""
            <tr>
                <th><center>TOTALES</center></th>
                <th><center>{temp_med:.2f}º</center></th>
                <th><center>{temp_min}º</center></th>
                <th><center>{temp_max}º</center></th>
                <th><center>{mediciones}</center></th>
            </tr>
        </table>
    </center>
</body>
</html>
"""


#
# PROGRAMA PRINCIPAL
#
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
    mostrar_ayuda()
    exit(0)
else:
    salida_html = False

ciudad = sys.argv[1]    # localidad de la que vamos a hacer el pronóstico

# petición GET a OpenWeather
datos_mediciones = tiempo_en_5dias(ciudad)

# cálculos
dias = dict()  # diccionario con clave el día y valor la lista de mediciones del día
totales = {"temp": [], "temp_min": [], "temp_max": []}  # lista de mediciones de todos los días
calculos_temperatura(dias, totales, datos_mediciones)

# Resultados
# crear fichero html si es necesario
if salida_html:
    fichero = fichero_html(ciudad, datos_mediciones)
    fichero.write(inicio_html(ciudad))  # escribimos inicio html
else:
    fichero = None

# procesamos cada medición
for dia, temps in dias.items():
    escribe_valores_dia(dia, temps, fichero)    # diario

# global
escribe_valores_totales(totales, fichero, len(datos_mediciones["list"]))

