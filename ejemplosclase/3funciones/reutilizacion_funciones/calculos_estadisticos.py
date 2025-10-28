"""
Probamos el módulo 'estadística'.
"""
import random
import estadistica as st


def main():
    # Generamos una lista de números aleatorios
    numbers = []
    for _ in range(100):
        numbers.append(random.randint(1, 100))

    # Mostramos media, varianza y desviación típica
    print("Números generados: ", numbers)
    print("La media de los números generados es", st.mean(numbers))
    print("La varianza de los números generados es", st.variance(numbers))
    print("La desviación típica de los números generados es", st.dev(numbers))


if __name__ == "__main__":
    main()
