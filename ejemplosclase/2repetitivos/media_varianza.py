"""
Este programa pide una serie de calificaciones al usuario y dos indica su media, su mediana y su varianza.

Ejemplo de la necesidad de usar arrays (en este caso listas de Python).
"""

print("Programa para calcular la media, mediana y varianza de calificaciones")
print("---------------------------------------------------------------------")

# cálculo de la media
sum_grades = 0
num_grades = 0

while True:
    # pedimos una nota entre 0 y 10
    while True:
        grade = float(input("Introduzca una calificación: "))
        if 0 <= grade <= 10:
            break
        print("Le recuerdo que la nota debe estar entre 0 y 10.\n")

    # acumulo la nota introducida
    sum_grades += grade
    num_grades += 1

    # ¿seguimos?
    while True:
        resp = input("¿Continuamos introduciendo notas (S/N) ").upper()
        if resp == "S" or resp == "N":
            break
        print("Le recuerdo que debe responder con S o N\n")

    if resp == "N":
        break

mean = sum_grades / num_grades
print(f"\nLa media de las notas introducidas es {mean:.2f}")
