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


def mode(*numbers):
    if len(numbers) == 1 and isinstance(numbers[0], (list, tuple)):
        numbers = numbers[0]

    for n in numbers:
        if not isinstance(n, int):
            raise TypeError(f"Encontrado {n} que no es int")

    individual_numbers, frequencies_numbers = [], []
    for n in numbers:
        if n in individual_numbers:
            index_number = individual_numbers.index(n)
            frequencies_numbers[index_number] += 1
        else:
            individual_numbers.append(n)
            frequencies_numbers.append(1)

    max_frequencies = max(frequencies_numbers)
    modes = []
    for i in range(len(individual_numbers)):
        if frequencies_numbers[i] == max_frequencies:  # es una moda
            modes.append(individual_numbers[i])
    return tuple(modes)


def main():
    print("Estoy probando la biblioteca de estadística.")
    numbers = [3, 7, 7, 1, 4, 1, 7, 1]
    print(f"La media de {numbers} es {mean(numbers)}")
    print(f"La varianza de {numbers} es {variance(numbers)}")
    print(f"La desviación típica de {numbers} es {dev(numbers)}")
    print(f"La moda de {numbers} es {mode(3, 7, 7, 1, 4, 1, 7, 1)}")


if __name__ == "__main__":
    main()
