"""
Programa que nos dice los pasos para resolver el problema de las torres de Hanoi.
"""

def main():
    print("Problema de las torres de Hanoi (pasar discos de A a B usando c como auxiliar)")
    print("------------------------------------------------------------------------------")

    n = int(input("¿Cuantos discos quiere pasar de A a B pasando por C: "))

    print("Los pasos que tiene que dar son:")
    hanoi(n, 'A', 'B', 'C')

def hanoi(n, a, b, aux):
    if n == 1:
        print(f"{a} -> {b}")
        return
    hanoi(n-1, a, aux, b)
    hanoi(1, a, b, aux)
    hanoi(n-1, aux, b, a)

if __name__ == '__main__':
    main()
