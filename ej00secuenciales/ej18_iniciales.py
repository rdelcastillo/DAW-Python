"""
Programa ej18_iniciales.py

Propósito: Pedir el nombre y los dos apellidos de una persona y mostrar las iniciales.

Autor: Rafael del Castillo Gomariz
Fecha: 12/10/2020
-------------------------------------------------------------------------------------
Análisis:
-------------------------------------------------------------------------------------
Hay que pedir el nombre y los apellidos, y mostrar las iniciales, o sea, el primer carácter de cada cadena.

Datos de entrada: nombre y apellidos (cadena)
Información de salida: Iniciales (cadena)

Variables: name, surname1, surname2, initials (cadena).
------------------------------------------------------------------------------------
Algoritmo:
-------------------------------------------------------------------------------------
1. Leer nombre y apellidos
2. Obtener primer carácter de cada cadena
3. Concatenar los caracteres
4. Mostrar iniciales
"""
print("Cálculo de las iniciales del nombre y los apellidos de una persona")
print("------------------------------------------------------------------")

# Pedimos datos
name = input("Dime tu nombre: ")
surname1 = input("Dime tu primer apellido: ")
surname2 = input("Dime tu segundo apellido: ")

# Cálculos
initials = (name[0] + surname1[0] + surname2[0]).upper()

# Salida
print("Las iniciales son: ", initials)
