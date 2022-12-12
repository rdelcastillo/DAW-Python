"""
Haz un programa que muestre un menú y, usando las funciones anteriores, ejecute las siguientes opciones:

Muestra los números primos que hay entre 1 y 1000.
Muestra los números capicúa que hay entre 1 y 99999.
Muestra la moda de 50 números enteros aleatorios entre 1 y 10.
Muestra la mediana de 10 números enteros aleatorios entre 1 y 50.
Muestra el máximo y mínimo de 1000 números enteros aleatorios entre 1 y 50000.
Muestra la varianza de 10 números enteros aleatorios entre 1 y 5.

Autor: Rafael del Castillo Gomariz
Fecha: 9/12/2022
"""
import random

from ej01_4 import menu
from ej02_biblioteca_funciones_num import es_primo, es_capicua
import util.statistics as st


def main():
    while True:
        opc = menu("Mostrar los números primos entre 1 y 1000", "Mostrar los números capicúa entre 1 y 99999",
                   "Mostrar la moda de 50 números aleatorios entre 1 y 10",
                   "Mostrar la mediana de 10 números aleatorios entre 1 y 50",
                   "Mostrar el máximo y mínimo de 1000 números aleatorios entre 1 y 50000",
                   "Mostrar la varianza de 10 números aleatorios entre 1 y 5", "Finalizar")
        if opc == 1:
            print_prime_numbers_between_1_and_1000()
        elif opc == 2:
            print_palindromic_numbers_between_1_and_99999()
        elif opc == 3:
            print_mode_of_50_random_numbers_between_1_and_10()
        elif opc == 4:
            print_median_of_10_random_numbers_between_1_and_50()
        elif opc == 5:
            print_maximum_and_minimum_of_1000_random_numbers_between_1_and_50000()
        elif opc == 6:
            print_variance_of_10_random_numbers_between_1_and_5()
        else:
            break

    print("¡Hasta la próxima! :-)")


def print_prime_numbers_between_1_and_1000():
    for n in range(1, 1001):
        if es_primo(n):
            print(n)


def print_palindromic_numbers_between_1_and_99999():
    for n in range(1, 100000):
        if es_capicua(n):
            print(n)


def print_mode_of_50_random_numbers_between_1_and_10():
    numbers = [random.randint(1, 10) for _ in range(50)]
    print("Números:", numbers)
    print("Moda:", st.mode(numbers))


def print_median_of_10_random_numbers_between_1_and_50():
    numbers = [random.randint(1, 50) for _ in range(10)]
    print("Números:", numbers)
    print("Mediana:", st.median(numbers))


def print_maximum_and_minimum_of_1000_random_numbers_between_1_and_50000():
    numbers = [random.randint(1, 50000) for _ in range(1000)]
    print("Números:", numbers)
    print("Máximo:", st.maximum(numbers))
    print("Mínimo:", st.minimum(numbers))


def print_variance_of_10_random_numbers_between_1_and_5():
    numbers = [random.randint(1, 5) for _ in range(10)]
    print("Números:", numbers)
    print("Varianza:", st.variance(numbers))


if __name__ == "__main__":
    main()
