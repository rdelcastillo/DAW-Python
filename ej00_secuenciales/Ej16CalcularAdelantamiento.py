"""
Programa Ej16CalcularAdelantamiento.py

Propósito:
Calcular en cuanto tiempo (en minutos) alcanzará un vehículo a otro distanciados por una distancia D, conociendo sus
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

Variables: speed1, speed2, distancia (real), tiempo (real).
------------------------------------------------------------------------------------
Algoritmo:
-------------------------------------------------------------------------------------
1. Leer las dos velocidades y la distancia (asumimos que v1>v2)
2. Calcular tiempo: (v=espacio/t), por lo tanto t=espacio/v. Tiempo=distancia/(v1-v2).
3. Mostrar tiempo.
"""

print("Cálculo del tiempo que el primer alcanzará al segundo")
print("-----------------------------------------------------")

# Pedimos datos
speed1 = float(input("Dime la velocidad del coche 1 (km/h): "))
speed2 = float(input("Dime la velocidad del coche 2 (más pequeña)(km/h): "))
distancia = float(input("Dime la distancia entre los coches (km): "))

# Hacemos cálculos
tiempo = 60 * distancia / (speed1 - speed2)

# Resultado
print("El primer coche alcanza al primero en", tiempo, "minutos.")
