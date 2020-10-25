"""
Programa Ej15IntercambiarVariables.py

Propósito: Dadas dos variables numéricas A y B, que el usuario debe teclear, se pide intercambiar los valores de ambas.

Autor: Rafael del Castillo Gomariz
Fecha: 12/10/2020
-------------------------------------------------------------------------------------
Análisis:
-------------------------------------------------------------------------------------
Se piden el valor de dos variables (el tipo puede ser el que queramos), hay que intercambiar sus valores.

Datos de entrada: dos números en dos variables (entero).
Información de salida: Las dos variables pero con los datos cambiados (entero)

Variables: a,b.
------------------------------------------------------------------------------------
Algoritmo:
-------------------------------------------------------------------------------------
1. Leer los dos valores.
2. Intercambio los valores. Necesito una variable auxiliar (aux). Asigno "a" en "aux", "b" en "a" y "aux" en "b"
3. Mostrar los valores de "a" y "b".
"""

print("Intercambio de los valores de dos variables")
print("-------------------------------------------")

# Pedimos datos
a = int(input("Introduce valor de la variable A: "))
b = int(input("Introduce valor de la variable B: "))

# Intercambiamos las variables usando una variable auxiliar
aux = a
a = b
b = aux

# Mostramos resultados
print("Nuevo valor de A: ", a)
print("Nuevo valor de B: ", b)

# Python permite hacer esto de forma más simple usando "tuplas".
# Para probarlo volvemos a intercambiar los valores

# Intercambiamos variables SIN usar variable auxiliar
a, b = b, a

# Mostramos resultados
print("\nNuevo intercambio para recuperar los valores originales:")
print("Nuevo valor de A: ", a)
print("Nuevo valor de B: ", b)
