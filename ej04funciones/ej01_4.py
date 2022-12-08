"""
Modificación del programa anterior.

Crea una función para gestionar menús: recibe una lista de opciones, las muestra numeradas, pide una opción
(por su número) y devuelve la opción escogida.

Autor: Rafael del Castillo Gomariz.
Fecha: 7/12/2022.
"""
def main():
    a, b = 0, 0
    data_has_been_entered = False
    while True:
        option = menu("Introducción de A y B", "Sumar A y B", "Restar A y B", "Multiplicar A y B", "Dividir A y B",
                      "Terminar")
        if option == 1:
            a, b = input_data()
            data_has_been_entered = True
        elif not data_has_been_entered:
            print("ERROR. Lo primero que debe hacer es introducir A y B.")
        elif option == 2:
            print_addition(a, b)
        elif option == 3:
            print_subtraction(a, b)
        elif option == 4:
            print_multiplication(a, b)
        elif option == 5:
            print_division(a, b)
        else:   # solo puede ser la 6, la función menu() impide opciones incorrectas
            break
    print("¡Adiós! :-)")

def menu(*options):
    while True:
        print("\nMenú de opciones")
        print("----------------")
        for i in range(len(options)):
            print(f"{i+1}. {options[i]}")
        option = int(input("\nEscoja una opción: "))
        print()
        if 1 <= option <= len(options):
            return option
        print("Opción incorrecta.")

def input_data():
    a = int(input("Valor de A: "))
    b = int(input("Valor de B: "))
    return a, b

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
