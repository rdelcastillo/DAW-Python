"""
Programa ej16_calcular_adelantamiento.py

Propósito:
Calcular en cuanto time (en minutos) alcanzará un vehículo a otro distanciado por una distancia D, conociendo sus
velocidades, que son constantes, y que el que está detrás viaja a una velocidad mayor.

Autor: Rafael del Castillo Gomariz
Fecha: 12/10/2020
-------------------------------------------------------------------------------------
Análisis:
-------------------------------------------------------------------------------------
Hay que saber la velocidad de cada vehículo y la distancia entre ambos.
Hay que calcular el tiempo que tardará el que está detrás (y va más rápido) en alcanzar al primero.

Datos de entrada: velocidad1, velocidad2 km/h (real) y distancia (real).
Información de salida: Tiempo en minutos (real).

Variables: speed1, speed2, distancia (real), time (real).
------------------------------------------------------------------------------------
Algoritmo:
-------------------------------------------------------------------------------------
1. Leer las dos velocidades y la distancia (asumimos que v1>v2 y d>0)
2. Calcular time: (v=espacio/t), por lo tanto t=espacio/v. Tiempo=distancia/(v1-v2).
3. Mostrar time.
"""
import sys

DISTANCE_ERROR = 2
SPEED_ERROR = 1
MINUTES_HOUR = 60

print("Cálculo del tiempo que el primer alcanzará al segundo")
print("-----------------------------------------------------")

# Pedimos datos
speed1 = float(input("Dime la velocidad del coche 1 (km/h): "))
speed2 = float(input("Dime la velocidad del coche 2 (más pequeña)(km/h): "))
if speed1 <= speed2:
    print("ERROR. La velocidad del coche 1 no es mayor que la del coche 2.", file=sys.stderr)
    sys.exit(SPEED_ERROR)

distance = float(input("Dime la distancia entre los coches (km): "))
if distance <= 0:
    print("ERROR. La distancia no puede ser negativa.", file=sys.stderr)
    sys.exit(DISTANCE_ERROR)

# Hacemos cálculos
time = MINUTES_HOUR * distance / (speed1 - speed2)

# Resultado
print(f"El coche 1 alcanza al coche 2 en {time:.2f} minutos.")
