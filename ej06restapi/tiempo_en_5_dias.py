"""
Usando la API de OpenWeather obtendremos el pronóstico del time para una ciudad que se le pide al usuario de los
próximos cinco días, mostraremos:

Temperatura media, mínima y máxima (en grados Celsius) para cada día y global.

Para las temperaturas medias usaremos la clave "temp" del json devuelto por la API.
Para las temperaturas mínimas usaremos la clave "temp_min" del json devuelto por la API.
Para las temperaturas máximas usaremos la clave "temp_max" del json devuelto por la API.
"""
import requests
import os

# Pedimos la ciudad
city = input("Ciudad de la que quiere conocer el pronóstico del time en los próximos 5 días: ")

# datos para hacer la petición
url = "https://api.openweathermap.org/data/2.5/forecast"
params = {"q": city, "appid": os.environ["OPEN_WEATHER_KEY"], "units": "metric", "lang": "es"}

# petición
response = requests.get(url, params=params)
if response.status_code != 200:
    print("Error al hacer la petición:", response.status_code)
    exit(1)
json_data = response.json()

# cálculos
days = dict()  # diccionario con clave el día y valor la lista de mediciones del día
totals = {"temp": [], "temp_min": [], "temp_max": []}  # lista de mediciones de todos los días

for measurement in json_data["list"]:
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

# resultados
print()
for day, temps in days.items():
    # diario
    temp_med = sum(temps['temp']) / len(temps['temp'])
    temp_min = min(temps['temp_min'])
    temp_max = max(temps['temp_max'])
    print(f"Día {day[8:]}-{day[5:7]}-{day[0:4]}:\t"
          f"Temperatura media: {temp_med:.2f}º, "
          f"mínima: {temp_min}º y máxima: {temp_max}º. "
          f"Mediciones: {len(temps['temp'])}")
print()

# global
temp_med = sum(totals['temp']) / len(totals['temp'])
temp_min = min(totals['temp_min'])
temp_max = max(totals['temp_max'])
print(f"TOTALES:\t\tTemperatura media: {temp_med:.2f}º, "
      f"mínima: {temp_min}º y máxima: {temp_max}º")
