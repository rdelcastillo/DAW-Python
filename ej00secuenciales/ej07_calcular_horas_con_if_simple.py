"""
Programa ej07_calcular_horas.py
Propósito: Pide una cantidad de minutos y muestra por pantalla a cuantas horas y minutos corresponde.
Autor: Rafael del Castillo Gomariz
Fecha: 12/10/2020
-------------------------------------------------------------------------------------
Análisis:
-------------------------------------------------------------------------------------
Tenemos que leer una cantidad de minutos, y calcular cuantas horas y minutos son.

Datos de entrada: minutos (entero)

Información de salida: horas y minutos (entero)

Variables: total_minutes, hours, minutes (entero).

-------------------------------------------------------------------------------------
Algoritmo:
-------------------------------------------------------------------------------------
1. Leer los minutos
2. Calcular a cuantas horas corresponde, división entera entre 60.
3. calcular los minutos restantes: resto de la división entre 60.
4. Mostrar horas y minutos
"""

# Pedimos datos
total_minutes = int(input("Dime la cantidad de minutos: "))

# Cálculos
hours = total_minutes // 60
minutes = total_minutes % 60

# Resultado
# Distinguiremos el caso de cuando horas y minutos vayan en singular

# primero: escribo el valor de la variable "horas"
print(hours, "hora", end="")

# segundo: compruebo si es más hora, en ese caso añado una "s"
if hours != 1:
    print("s", end="")

# tercero: hago lo mismo con los minutos
print(" y", minutes, "minuto", end="")
if minutes != 1:
    print("s")
