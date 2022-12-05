"""
Define tres arrays de 20 números enteros cada uno, con nombres numbers, squares y cubes.
Carga el array numbers con valores aleatorios entre 0 y 100.
En el array squares se deben almacenar los cuadrados de los valores que hay en el array numbers.
En el array cubes se deben almacenar los cubos de los valores que hay en numbers.
A continuación, muestra el contenido de los tres arrays dispuesto en tres columnas.
"""
import random

LEN_ARRAY = 20
MIN_NUMBER = 0
MAX_NUMBER = 100

numbers = [random.randint(MIN_NUMBER, MAX_NUMBER) for _ in range(LEN_ARRAY)]
squares = [n ** 2 for n in numbers]
cubes = [n ** 3 for n in numbers]

for i in range(LEN_ARRAY):
    print(f"{numbers[i]:3} {squares[i]:5} {cubes[i]:7}")