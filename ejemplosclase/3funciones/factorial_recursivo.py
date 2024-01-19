"""
Ejemplo de recursividad usando la función factorial.

    1 si n == 1
n! =
    n * (n-1)! en otro caso
"""


def main():
    print("Cálculo del factorial de un número")
    print("----------------------------------")

    n = int(input("Introduzca un número: "))

    print(f"El factorial de {n} es {factorial(n)}")

def factorial(n):
    assert(n > 0)
    if n == 1:
        return 1
    return n * factorial(n-1)

if __name__ == "__main__":
    main()
    