"""
Usando la API de OpenWeather obtendremos el pronóstico del tiempo para una ciudad que se le pide al usuario de los
próximos cinco días, mostraremos:

Temperatura media, mínima y máxima (en grados Celsius) para cada día y global.
"""
import requests
import os

# Pedimos la ciudad
ciudad = input("Ciudad de la que quiere conocer el pronóstico del tiempo en los próximos 5 días: ")

# datos para hacer la petición
url = "https://api.openweathermap.org/data/2.5/forecast"
params = {"q":ciudad, "appid":os.environ["OPEN_WEATHER_KEY"], "units":"metric", "lang":"es"}

# petición
response = requests.get(url, params=params)
if response.status_code != 200:
    print("Error al hacer la petición:", response.status_code)
    exit(1)
datos = response.json()

# cálculos
dias = dict()       # diccionario con clave el día y valor la lista de mediciones del día
totales = list()    # lista de mediciones de todos los días
for medicion in datos["list"]:
    # fecha y temperatura de la medición
    dia = medicion["dt_txt"][:10]
    temp = float(medicion["main"]["temp"])
    # si no tenemos datos de ese día creamos una nueva entrada en el diccionario
    if not dias.get(dia):
        dias[dia] = list()
    # añadimos medición
    dias[dia].append(temp)
    totales.append(temp)

# resultados
print()
for dia,temps in dias.items():
    print(f"Día {dia[8:]}-{dia[5:7]}-{dia[0:4]}:\tTemperatura media: {(sum(temps)/len(temps)):.2f}º, "
          f"mínima: {min(temps)}º y máxima: {max(temps)}º")
print()
print(f"TOTALES:\t\tTemperatura media: {(sum(totales)/len(totales)):.2f}º, "
      f"mínima: {min(totales)}º y máxima: {max(totales)}º")