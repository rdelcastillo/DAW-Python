# ################################################################################
# Pide al usuario dos pares de números x1,y2 y x2,y2, que representen dos puntos
# en el plano. Calcula y muestra la distancia entre ellos.
# ################################################################################
# Análisis
# Se piden dos puntos y se calcula la distancia entre ellos.
# Datos de entrada: dos puntos; cuatro coordenadas (x1,y1) (x2,y2) (entero).
# Información de salida: distancia (real).
# Variables: x1,y1,x2,y2(entero), distancia(real).
# ################################################################################
# Diseño
# 1. Leer las cuatro coordenadas.
# 2. Calcular distancia: raíz cuadrada de (x2-x1)^2 + (y2-y1)^2
# 3. Mostrar distancia
# ################################################################################

import math

# Pedimos datos
x1 = int(input("Dime las coordenadas del punto 1:\n"))
y1 = int(input())
x2 = int(input("Dime las coordenadas del punto 2:\n"))
y2 = int(input())

# Cálculos
distancia = math.sqrt(math.pow((x2-x1),2)+math.pow((y2-y1),2))

# Salida
print(f"Distancia: {distancia}")



