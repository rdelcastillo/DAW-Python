"""
Programa que escoge al azar 5 palabras en español del mini-diccionario del ejercicio anterior. Se pedirá que el usuario
teclee la traducción al inglés de cada una de las palabras y se comprobará si son correctas. Al final, se mostrará
cuántas respuestas son válidas y cuántas erróneas.

Ejercicio del libro "Aprende Java con Ejercicios", edición 2019.

Autor: Rafael del Castillo Gomariz.
"""
import random

from ej03_dictionary import SPANISH_ENGLISH_DICT

NUM_QUESTIONS = 5

print("Test de inglés")
print("--------------")

# Escogemos las palabras a preguntar en español
spanish_words = tuple(SPANISH_ENGLISH_DICT.keys())
test_words = set()
while len(test_words) < NUM_QUESTIONS:
    word = random.choice(spanish_words)
    test_words.add(word)

# Hacemos el test
num_answer_ok = 0
for word in test_words:
    answer = input(f"Traducción de {word}: ").lower()
    if answer == SPANISH_ENGLISH_DICT[word]:
        num_answer_ok += 1

# Resultados
print(f"Ha acertado {num_answer_ok} palabras.")
print(f"Ha fallado {NUM_QUESTIONS - num_answer_ok} palabras.")
