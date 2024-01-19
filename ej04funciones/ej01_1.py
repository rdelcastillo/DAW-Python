"""
Haz un programa que pida dos valores (a y b) y a continuación muestre un menú con cinco opciones: sumar, restar,
multiplicar, dividir y terminar.

Cada opción llama a una función a la que se le pasan las dos variables y muestra el resultado de la operación. Si se
introduce una opción incorrecta se muestra un mensaje de error. El menú se volverá a mostrar, a menos que no se escoja
la opción terminar.

Autor: Rafael del Castillo Gomariz.
Fecha: 6/12/2022.
"""

def main():
    a = int(input("Valor de A: "))
    b = int(input("Valor de B: "))

    while True:
        option = input_option()
        if option == 1:
            print_addition(a, b)
        elif option == 2:
            print_subtraction(a, b)
        elif option == 3:
            print_multiplication(a, b)
        elif option == 4:
            print_division(a, b)
        elif option == 5:
            break
        else:
            print("Opción incorrecta.")

    print("Adiós! :-)")

def input_option():
    print("\nMenú de opciones")
    print("----------------")
    print("1. Sumar A y B")
    print("2. Restar A y B")
    print("3. Multiplicar A y B")
    print("4. Dividir A y B")
    print("5. Terminar")
    option = int(input("\nEscoja una opción: "))
    print()
    return option

def print_addition(n1, n2):
    print(f"La suma de {n1} y {n2} es {n1 + n2}")

def print_subtraction(n1, n2):
    print(f"La resta de {n1} y {n2} es {n1 - n2}")

def print_multiplication(n1, n2):
    print(f"La multiplicación de {n1} y {n2} es {n1 * n2}")

def print_division(n1, n2):
    if n2 != 0:
        print(f"La división de {n1} y {n2} es {n1 / n2}")
    else:
        print("ERROR. No se puede dividir por 0.")

if __name__ == "__main__":
    main()
