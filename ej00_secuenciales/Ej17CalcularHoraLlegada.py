"""
Programa Ej17CalcularHoraLlegada.py

Propósito: Un ciclista parte de una ciudad A a las HH horas, MM minutos y SS segundos.
El tiempo de viaje hasta llegar a otra ciudad B es de T segundos.
Se pide determinar la hora de llegada a la ciudad B.

Autor: Rafael del Castillo Gomariz
Fecha: 12/10/2020
-------------------------------------------------------------------------------------
Análisis:
-------------------------------------------------------------------------------------
Tenemos que pedir la hora de salida (hora, minutos y segundos).
Tenemos que saber también el tiempo en segundos que ha tardado en llegar.
Tenemos que calcular la hora de llegada.

Datos de entrada: hora, minutos y segundos de salida (enteros), segundos que tarda (entero).
Información de salida: hora, minutos y segundos de llegada (enteros).

Variables:  departure_hour, departure_minute, departure_second, travel_seconds,
            arrival_hour, arrival_minute, arrival_second (enteros)

------------------------------------------------------------------------------------
Algoritmo:
-------------------------------------------------------------------------------------
1. Leer hora de salida
2. Leer segundos que tarda
3. Convierto la hora de salida a segundos (necesito una variable departure_time_in_seconds)
4. Le sumo los segundos que he tardado (necesito una variable arrival_time_in_seconds)
5. Convierto los segundos totales a hora, minuto y segundos
6. Muestro la hora de llegada
"""

print("Cálculo de la hora de llegada de un ciclista de A a B")
print("-----------------------------------------------------")

# Pedimos datos
departure_hour = int(input("Hora de salida: "))
departure_minute = int(input("Minutos de salida: "))
departure_second = int(input("Segundos de salida: "))
travel_seconds = int(input("Tiempo que has tardado en segundos: "))

# Hacemos los cálculos

# convierto la hora de salida a segundos
departure_time_in_seconds = departure_hour * 3600 + departure_minute * 60 + departure_second

# le sumo los segundos que he tardado
arrival_time_in_seconds = departure_time_in_seconds + travel_seconds

# convierto los segundos totales a hora, minuto y segundos
arrival_hour = arrival_time_in_seconds // 3600
arrival_minute = (arrival_time_in_seconds % 3600) // 60
arrival_second = (arrival_time_in_seconds % 3600) % 60

# Muestro la hora de llegada
print(f"Hora de llegada {arrival_hour}:{arrival_minute}:{arrival_second}")
