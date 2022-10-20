"""
Programa que calcula la nota final de un estudiante, considerando que:

- cada respuesta correcta suma 5 puntos
- cada respuesta incorrecta suma -1 puntos
- cada respuesta en blanco suma 0 puntos.

Imprime la puntuación total obtenida por el estudiante y su nota normalizada entre 0 y 10.

Autor: Rafael del Castillo Gomariz
Fecha: 19/10/2022
"""

POINTS_CORRECT_ANSWER = 5
POINTS_INCORRECT_ANSWER = -1
POINTS_BLANK_ANSWER = 0
MAX_SCORE = 10

print("Cálculo de la calificación final")
print("--------------------------------")

number_correct_answers = int(input("Número de respuestas correctas: "))
number_incorrect_answers = int(input("Número de respuestas incorrectas: "))
number_blank_answers = int(input("Número de respuestas en blanco: "))

max_points = (number_correct_answers + number_incorrect_answers + number_blank_answers) * POINTS_CORRECT_ANSWER
points = number_correct_answers * POINTS_CORRECT_ANSWER + number_incorrect_answers * POINTS_INCORRECT_ANSWER \
                 + number_blank_answers * POINTS_BLANK_ANSWER
score = MAX_SCORE * (points / max_points)

print("La calificación final es", score)
