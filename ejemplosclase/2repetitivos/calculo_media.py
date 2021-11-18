"""
Este programa calcula la media de 5 notas introducidas por el usuario.

Autor: Rafael del Castillo
Fecha: 28/10/2021
"""

NUM_GRADES = 5
sum_grades = 0  # esta variable es un "acumulador"

print(f"Cálculo de la media de {NUM_GRADES} notas")
print("-------------------------------")

# Pedimos las notas
for i in range(NUM_GRADES):
    grade = int(input(f"Dame la nota número {i + 1}: "))
    sum_grades += grade

# Mostrar resultado
mean_grades = sum_grades / NUM_GRADES
print(f"La media de las {NUM_GRADES} notas es {mean_grades:.2f}")