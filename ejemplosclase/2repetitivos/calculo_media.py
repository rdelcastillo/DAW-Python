"""
Este programa calcula la media de 5 notas introducidas por el usuario.

Autor: Rafael del Castillo
Fecha: 28/10/2021
"""

NUM_NOTAS = 5
suma_notas = 0  # esta variable es un "acumulador"

print(f"Cálculo de la media de {NUM_NOTAS} notas")
print("-------------------------------")

# Pedimos las notas
for i in range(NUM_NOTAS):
    nota = int(input(f"Dame la nota número {i+1}: "))
    suma_notas += nota

# Mostrar resultado
media_notas = suma_notas / NUM_NOTAS
print(f"La media de las {NUM_NOTAS} notas es {media_notas:.2f}")