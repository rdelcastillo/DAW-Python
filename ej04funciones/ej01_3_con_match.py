"""
Modificación del programa anterior.

Si no se introducen las dos variables a y b desde su opción, no se puede ejecutar el resto de las opciones.

Autor: Rafael del Castillo Gomariz.
Fecha: 7/12/2022.
"""

def main():
    a, b = 0, 0
    data_has_been_entered = False
    while True:
        option = input_option()
        if not data_has_been_entered and option != 1 and option != 6:
            print("ERROR. Lo primero que debe hacer es introducir A y B.")
            continue  # vuelve al principio del ciclo
        match option:
            case 1:
                a, b = input_data()
                data_has_been_entered = True
            case 2: print_addition(a, b)
            case 3: print_subtraction(a, b)
            case 4: print_multiplication(a, b)
            case 5: print_division(a, b)
            case 6: break
            case _: print("Opción incorrecta.")
    print("¡Adiós! :-)")

def input_option():
    print("\nMenú de opciones")
    print("----------------")
    print("1. Introducción de A y B")
    print("2. Sumar A y B")
    print("3. Restar A y B")
    print("4. Multiplicar A y B")
    print("5. Dividir A y B")
    print("6. Terminar")
    option = int(input("\nEscoja una opción: "))
    print()
    return option

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
