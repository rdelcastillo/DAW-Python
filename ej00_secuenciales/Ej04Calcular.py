"""
Programa Ej04Calcular.py
Propósito: Dados dos números, mostrar la suma, resta, división y multiplicación de ambos.
Autor: Rafael del Castillo Gomariz
Fecha: 12/10/2020
-------------------------------------------------------------------------------------
Análisis:
-------------------------------------------------------------------------------------
Tenemos que leer dos números, calcular la suma, resta, multiplicación y división.

Datos de entrada: Los dos números (reales).

Información de salida: suma, resta, multiplicación, división (reales)

Variables: num1, num2 (reales). Esta vez las salidas no las guardamos en variables.
-------------------------------------------------------------------------------------
Algoritmo:
-------------------------------------------------------------------------------------
1. Leer los números.
2. Mostrar suma, resta, multiplicación y división.
"""

print("Cálculo de la suma, resta, división y multiplicación de dos números.")
print("--------------------------------------------------------------------")

# Pedimos datos
num1 = float(input("Introduce el número 1: "))
num2 = float(input("Introduce el número 2: "))

# Mostramos resultados usando "cadenas f"
# Más información de las cadenas f: https://www.mclibre.org/consultar/python/lecciones/python-cadenas.html#cadenas-f
print(f"La suma es {num1+num2}")
print(f"La resta es {num1-num2}")
print(f"La multiplicación es {num1*num2}")
print(f"La división es {num1/num2}")

