"""
Funciones estadísticas.
"""


def mean(numbers):
    addition = 0
    for n in numbers:
        addition += n
    return addition / len(numbers)


def variance(numbers):
    addition = 0
    mean_numbers = mean(numbers)
    for n in numbers:
        addition += (n - mean_numbers) ** 2
    return addition / len(numbers)


def dev(numbers):
    return variance(numbers) ** 0.5


if __name__ == "__main__":
    numbers = [3, 7, 1, 4]
    print(f"La media de {numbers} es {mean(numbers)}")
    print(f"La varianza de {numbers} es {variance(numbers)}")
    print(f"La desviación típica de {numbers} es {dev(numbers)}")
