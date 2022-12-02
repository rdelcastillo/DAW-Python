"""
Ejemplo de como usar una función main().

Es frecuente crear una función main() para poder poner variables locales en el programa principal,
no tener que poner la funciones al principio y así poder leer de arriba abajo, etc.
"""


def main():
    n = int(input("Dame un número y te dire a qué término de la serie de Fibonacci se corresponde: "))
    print(f"El término número {n} de la serie de Fibonacci es {fibonacci_iterative(n)}")


def fibonacci_recursive(n):
    """
    Devuelve el término n de la sucesión de Fibonacci. Ojo, la forma recursiva no es eficiente.
    """
    # caso base o trivial
    if n == 0 or n == 1:
        return n
    # caso genérico
    return fibonacci_recursive(n - 1) + fibonacci_recursive(n - 2)


def fibonacci_iterative(n):
    """
    Devuelve el término n de la sucesión de Fibonacci de manera iterativa
    """
    # caso base o trivial
    if n == 0 or n == 1:
        return n

    # caso genérico
    last = 0
    actual = 1
    for term in range(2, n + 1):
        new_value = actual + last
        last = actual
        actual = new_value
    return actual


if __name__ == "__main__":
    main()
