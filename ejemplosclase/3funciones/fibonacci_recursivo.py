"""
Cálculo de un término de la serie de Fibonacci de forma recursiva.

Fecha: 2022-11-03
Autor: Clase de CEIABD del IES Gran Capitán.
"""

def main():
    """
    Función principal del programa.
    """
    n = int(input("Introduce el término de la serie de Fibonacci a calcular: "))
    print(f"El término {n} de la serie de Fibonacci es {fibonacci(n)}")


def fibonacci(n):
    """
    Calcula el término n de la serie de Fibonacci de forma recursiva.
    """
    if n == 1 or n == 2:
        return 1
    return fibonacci(n - 1) + fibonacci(n - 2)

if __name__ == "__main__":
    main()
