"""
Biblioteca de funciones (statistics) dentro de un paquete (util) que contiene las siguientes funciones:

- maximum
  - recibiendo como parámetro un array de enteros
  - recibiendo un conjunto de parámetros enteros
- minimum
  - recibiendo como parámetro un array de enteros
  - recibiendo un conjunto de parámetros enteros
- mean
  - recibiendo como parámetro un array de enteros
  - recibiendo un conjunto de parámetros enteros
- variance
  - recibiendo como parámetro un array de enteros y haciendo uso de la función anterior
  - recibiendo un conjunto de parámetros enteros y haciendo uso de la función anterior
- median
  - recibiendo como parámetro un array de enteros
  - recibiendo un conjunto de parámetros enteros
- mode
  - recibiendo como parámetro un array de enteros
  - recibiendo un conjunto de parámetros enteros
  - devuelve un array de enteros (puede haber varias modas)

Autor: Rafael del Castillo Gomariz
Fecha: 8/12/2022

Nota: cuando comparamos float no es adecuado usar ==, los errores de aproximación nos pueden jugar malas pasadas, mejor
es usar math.isclose() -> https://davidamos.dev/the-right-way-to-compare-floats-in-python/
"""
import math

def maximum(*numbers):
    if len(numbers) == 1 and isinstance(numbers[0], (list, tuple)):  # ¿hemos recibido una lista/tupla o varios enteros?
        numbers = numbers[0]
    max_number = numbers[0]
    for n in numbers[1:]:
        if n > max_number:
            max_number = n
    return max_number

def minimum(*numbers):
    if len(numbers) == 1 and isinstance(numbers[0], list):
        numbers = numbers[0]
    min_number = numbers[0]
    for n in numbers[1:]:
        if n < min_number:
            min_number = n
    return min_number

def mean(*numbers):
    if len(numbers) == 1 and isinstance(numbers[0], (list, tuple)):
        numbers = numbers[0]
    total = 0
    for n in numbers:
        total += n
    return total / len(numbers)

def variance(*numbers):
    if len(numbers) == 1 and isinstance(numbers[0], (list, tuple)):
        numbers = numbers[0]
    mean_numbers = mean(numbers)
    total = 0
    for n in numbers:
        total += (n - mean_numbers) ** 2  # no se debe usar la función mean() en vez de la variable
    return total / len(numbers)

def median(*numbers):
    if len(numbers) == 1 and isinstance(numbers[0], (list, tuple)):
        numbers = numbers[0]
    sorted_numbers = sorted(numbers)
    half_pos = len(numbers) // 2
    if len(sorted_numbers) % 2 == 0:
        return (sorted_numbers[half_pos] + sorted_numbers[half_pos - 1]) / 2
    else:
        return float(sorted_numbers[half_pos])  # para que siempre devuelva float

def mode(*numbers):
    if len(numbers) == 1 and isinstance(numbers[0], (list, tuple)):
        numbers = numbers[0]

    # creamos lista de los números de la lista (una sola aparición) y de las frecuencias asociadas (mismo índice)
    frequencies = []
    individual_numbers = []
    for n in numbers:
        if n in individual_numbers:
            index = individual_numbers.index(n)
            frequencies[index] += 1
        else:
            individual_numbers.append(n)
            frequencies.append(1)

    # buscamos frecuencia máxima y creamos la lista de números con esa frecuencia
    max_frequency = maximum(frequencies)
    mode_numbers = []
    for i in range(len(individual_numbers)):
        if frequencies[i] == max_frequency:
            mode_numbers.append(individual_numbers[i])
    mode_numbers.sort()
    return mode_numbers

if __name__ == "__main__":
    assert maximum(8, -5, 4, 7, 6, 11, 10) == 11
    assert maximum([8, -5, 4, 7, 6, 11, 10]) == 11

    assert minimum(8, -5, 4, 7, 6, 11, 10) == -5
    assert minimum([8, -5, 4, 7, 6, 11, 10]) == -5

    assert math.isclose(mean(8, -5, 4, 7, 6, 11, 10), 5.857142857) == True  # no se debe usar == con float
    assert math.isclose(mean([8, -5, 4, 7, 6, 11, 10]), 5.857142857) == True

    assert math.isclose(variance(8, -5, 4, 7, 6, 11, 10), 24.408163265306122) == True
    assert math.isclose(variance([8, -5, 4, 7, 6, 11, 10]), 24.408163265306122) == True

    assert math.isclose(median(8, -5, 4, 7, 6, 11, 10), 7) == True
    assert math.isclose(median([8, -5, 4, 7, 6, 11, 10]), 7) == True
    assert math.isclose(median(8, -5, 4, 7, 6, 11, 10, 15), 7.5) == True
    assert math.isclose(median([8, -5, 4, 7, 6, 11, 10, 15]), 7.5) == True

    assert mode(1, 1, 2, 2, 1, 2, 2, 2, 3, 5, 6, 1, 3) == [2]
    assert mode([1, 1, 2, 2, 1, 2, 2, 2, 3, 5, 6, 1, 3]) == [2]
    assert mode(1, 1, 2, 2, 1, 2, 2, 2, 3, 5, 6, 1, 3, 1) == [1, 2]
    assert mode(1, 1, 2, 2, 1, 2, 2, 2, 3, 5, 6, 1, 3, 1) == [1, 2]