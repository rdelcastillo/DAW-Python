"""
Un alumno desea saber cuál será su calificación final en la materia de Algoritmos. Dicha calificación se compone de los
siguientes porcentajes:

- 55% del promedio de sus tres calificaciones parciales.
- 30% de la calificación del examen final.
- 15% de la calificación de un trabajo final.

Autor: Rafael del Castillo Gomariz
Fecha: 19/10/2022
"""

WEIGHT_PARTIAL_EXAMS = 0.55
WEIGHT_FINAL_EXAM = 0.30
WEIGHT_FINAL_JOB = 1 - WEIGHT_FINAL_EXAM - WEIGHT_PARTIAL_EXAMS

print("Cálculo de la calificación final")
print("--------------------------------")

partial_exam1_score = float(input("Dame la calificación del primer examen parcial: "))
partial_exam2_score = float(input("Dame la calificación del segundo examen parcial: "))
partial_exam3_score = float(input("Dame la calificación del tercer examen parcial: "))
final_exam_score = float(input("Dame la calificación del examen final: "))
final_job_score = float(input("Dame la calificación del trabajo final: "))

partial_exams_score = (partial_exam1_score + partial_exam2_score + partial_exam3_score) / 3
final_score = WEIGHT_PARTIAL_EXAMS * partial_exams_score + WEIGHT_FINAL_EXAM * final_exam_score \
              + WEIGHT_FINAL_JOB * final_job_score

print("La calificación final es", final_score)
