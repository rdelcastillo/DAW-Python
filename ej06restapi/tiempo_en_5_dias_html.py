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

Autor: Rafael del Castillo Gomariz
"""

import requests
import sys
import os


def show_help():
    """
    Muestra la sintaxis de este programa y su funcionalidad.
    """
    print("Este programa nos da el pronóstico del time de los próximos cinco días para una ciudad.\n")
    print("Sintaxis: python3 tiempo_en_5_dias_html.py {CIUDAD} [{DIRECTORIO}]\n")
    print("Si {DIRECTORIO} no se especifica la información se muestra por la pantalla, si se hace se genera un fichero "
          "html en DIRECTORIO con nombre {CIUDAD}_{FECHA-INICIO}_{FECHA_FIN}.\n")
    print("Si {DIRECTORIO} se especifica hay que añadir al final del nombre / (Unix/Linux) ó \\ (Windows).")


def time5days(city):
    """
    Consulta en la API de Open Weather el pronóstico del time para los próximos cinco días.
    :param city: Localidad para que la hacemos la consulta.
    :return: JSON con las mediciones del time (40)
    """
    url = "https://api.openweathermap.org/data/2.5/forecast"
    params = {"q": city, "appid": os.environ["OPEN_WEATHER_KEY"], "units": "metric", "lang": "es"}
    response = requests.get(url, params=params)
    if response.status_code != 200:
        print("Error al hacer la petición o", city, "no existe:", response.status_code, file=sys.stderr)
        exit(2)
    return response.json()


def temperature_calculations(days, totals, data):
    """
    Calcula las temperaturas media, máxima y mínima diarias, y la global.
    :param days: lista donde guardamos los datos diarios.
    :param totals: diccionario donde guardamos los datos globales.
    :param data: JSON con los datos devueltos con la API de OpenWeathers
    """
    for measurement in data["list"]:
        # fecha y temperatura de la medición
        day = measurement["dt_txt"][:10]
        temp = float(measurement["main"]["temp"])
        temp_min = float(measurement["main"]["temp_min"])
        temp_max = float(measurement["main"]["temp_max"])

        # si no tenemos datos de ese día creamos una nueva entrada en el diccionario
        if not days.get(day):
            days[day] = {"temp": [], "temp_min": [], "temp_max": []}
        # añadimos medición
        days[day]["temp"].append(temp)
        days[day]["temp_min"].append(temp_min)
        days[day]["temp_max"].append(temp_max)
        totals["temp"].append(temp)
        totals["temp_min"].append(temp_min)
        totals["temp_max"].append(temp_max)


def html_file(city, json_data):
    """
    Abre para escritura el fichero donde guardaremos la salida html.
    :param city: Localidad de la que hacemos las mediciones.
    :param json_data: JSON con las mediciones de OpenWeathers
    :return: manejador del fichero
    """
    # nombre fichero: {CIUDAD}_{FECHA-INICIO}_{FECHA_FIN}
    # ejemplo: "Cordoba_2020-02-27-12.00.00_2020-03-03-09.00.00.html"
    start_date = json_data["list"][0]["dt_txt"]  # fecha primera medición
    end_date = json_data["list"][-1]["dt_txt"]  # fecha última medición
    filename = directory + city + "_" + start_date + "_" + end_date + ".html"
    # sustituimos en el nombre ":" por "." y " " por "-"
    filename = filename.replace(":", ".").replace(" ", "-")
    # abrimos fichero para escritura
    try:
        file = open(filename, "wt")
    except IOError:
        print("No se puede crear el fichero html:", filename)
        exit(3)
    return file


# Funciones para mostrar las temperaturas
def write_values_day(day, measurements, file):
    """
    Escribirá la temperatura media, mínima y máxima del día que hemos pasado como parámetro y el número de
    mediciones.
    :param file: manejador de fichero donde se escribe el html. None si la salida es por pantalla.
    :param day: día en el que se han tomado los valores de la temperatura.
    :param measurements: mediciones del día.
    :param salida_html: si es verdadero la salido es en un fichero
    """

    # cálculos y formateo del día
    day = f"{day[8:]}-{day[5:7]}-{day[0:4]}"  # formato dd-mm-aaaa
    temp_med = sum(measurements['temp']) / len(measurements['temp'])
    temp_min = min(measurements['temp_min'])
    temp_max = max(measurements['temp_max'])

    # muestro la información o en el fichero html o en pantalla
    if file:
        file.write(html_row(day, temp_med, temp_min, temp_max, len(measurements['temp'])))
    else:
        print(f"Día {day}:\t"
              f"Temperatura media: {temp_med:.2f}º, "
              f"mínima: {temp_min}º y máxima: {temp_max}º. "
              f"Mediciones: {len(measurements['temp'])}")


def write_totals_values(totals, file, num_measurements):
    """
    Escribirá la temperatura media, mínima y máxima global que hemos pasado como parámetro y el número de
    mediciones.
    :param num_measurements: número total de mediciones realizadas,
    :param totals: diccionario con los datos globales de las mediciones
    :param file: manejador de fichero donde se escribe el html. None si la salida es por pantalla.
    """

    # cálculos
    temp_med = sum(totals['temp']) / len(totals['temp'])
    temp_min = min(totals['temp_min'])
    temp_max = max(totals['temp_max'])
    if file:
        file.write(html_end(temp_med, temp_min, temp_max, num_measurements))
        file.close()
        print("Generado fichero", file.name, "con los datos.")
    else:
        print(f"\nTOTALES:\t\tTemperatura media: {temp_med:.2f}º, "
              f"mínima: {temp_min}º y máxima: {temp_max}º")


# Funciones para manejar el html
def html_init(city):
    """
    :param city:
    :return: inicio del html del resumen del pronóstico del time.
    """
    return f"""<!DOCTYPE html>
<html lang="es">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Lectura de temperaturas en {city}</title>
</head>
<body>
    <center><p>Este programa nos muestra los resultados de las mediciones para los próximos 5 días en {city}</p>
        <table border="1">
            <tr>
                <th>Día</th>
                <th>Temperatura Media</th>
                <th>Temperatura Mínima</th>
                <th>Temperatura Máxima</th>
                <th>Nº Mediciones</th>
            </tr>"""


def html_row(dia, temp_med, temp_min, temp_max, mediciones):
    return f"""
            <tr>
                <td><center>{dia}</center></td>
                <td><center>{temp_med:.2f}º</center></td>
                <td><center>{temp_min}º</center></td>
                <td><center>{temp_max}º</center></td>
                <td><center>{mediciones}</center></td>
            </tr>"""


def html_end(temp_med, temp_min, temp_max, mediciones):
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
    exit_html = True
    directory = sys.argv[2]
    if directory[-1] != "/" and directory[-1] != "\\":
        print("El nombre del directorio tiene que terminar en / ó en \\", file=sys.stderr)
        exit(3)
elif sys.argv[1] == "-h":
    show_help()
    exit(0)
else:
    exit_html = False

city = sys.argv[1]    # localidad de la que vamos a hacer el pronóstico

# petición GET a OpenWeather
measurements_data = time5days(city)

# cálculos
days = dict()  # diccionario con clave el día y valor la lista de mediciones del día
totals = {"temp": [], "temp_min": [], "temp_max": []}  # lista de mediciones de todos los días
temperature_calculations(days, totals, measurements_data)

# Resultados
# crear fichero html si es necesario
if exit_html:
    file = html_file(city, measurements_data)
    file.write(html_init(city))  # escribimos inicio html
else:
    file = None

# procesamos cada medición
for day, temps in days.items():
    write_values_day(day, temps, file)    # diario

# global
write_totals_values(totals, file, len(measurements_data["list"]))

