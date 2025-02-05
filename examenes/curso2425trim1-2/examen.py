"""
Examen de Programación de 16/12/2024.

Programa que usa una matriz de 3x3 y ofrezca un menú con las siguientes opciones:

1. Rellenar la matriz con números aleatorios entre 1 y 100.
    • Llama a la función fill() que recibe como parámetros 1 y 100.
        ◦ fill(1, 100)
2. Rellenar la matriz con números aleatorios entre 1 y 100 sin que se repitan.
    • Puedes reutilizar la función anterior de forma que reciba un tercer parámetro con un valor por defecto igual a
      True que indique si los números se pueden repetir.
        ◦ fill(1,100, False)
3. Desplazar todos los números una posición hacia la derecha.
    • Llama a la función shift_right() sin parámetros.
4. Desplazar todos los números una posición hacia abajo.
    • Llama a la función shift_down() sin parámetros.
5. Calcular la suma de los elementos de una fila.
    • Llama a la función show_sum_row() sin parámetros:
        ◦ Pide una fila y controla que esté entre 1 y 3. Si no es así muestra un mensaje de error.
        ◦ Llama a la función sum_row() pasándole como parámetro la fila anterior, esta función devuelve la suma.
        ◦ Muestra la suma.
6. Modificar un elemento de la matriz.
    • Llama a la función update_element() sin parámetros:
        ◦ Pide una fila y una columna, controla que estén entre 1 y 3. Si no es así muestra un mensaje de error.
        ◦ Muestra el contenido de esa posición y pregunta si de verdad quiere cambiarlo, controla que conteste Sí o No.
        ◦ Si contesta que Sí lo cambias, no hagas nada en caso contrario.
7. Mostrar la matriz.
    • Llama a la función show() sin parámetros:
        ◦ Muestra la matriz con los números alineados.
        ◦ Así estaría bien:
8. Salir del programa.
La matriz tiene que ser una variable global, llámala matrix. Créala, antes de mostrar el menú, rellena de ceros.

Cada opción del menú, excepto la de salir, llama a una función. Si no sabes hacerlo con funciones, hazlo sin ellas,
pero se penalizará con 2 puntos.

Si la opción 1 o 2 del menú no se han ejecutado, las demás (salvo la de salir) no funcionan y debes mostrar que hasta
que alguna de esas opciones no se ejecute, no funcionará.

Controla que las opciones del menú introducidas por el usuario son correctas.

Para operar con la matriz NO se pueden usar slices.
"""
import random

ROWS, COLUMNS = 3, 3
MIN_NUMBER, MAX_NUMBER = 1, 100
matrix = [[0] * COLUMNS for _ in range(ROWS)]


def main():
    data_initialized = False
    while True:
        show_menu()
        option = input_option()
        if not data_initialized and option not in [1, 2, 8]:
            print("ERROR. Lo primero que debe hacer es ejecutar la opción 1 o la 2.")
            continue  # vuelve al principio del ciclo
        match option:
            case 1:
                fill(MIN_NUMBER, MAX_NUMBER)
                data_initialized = True
            case 2:
                fill(MIN_NUMBER, MAX_NUMBER, False)
                data_initialized = True
            case 3:
                shift_right()
            case 4:
                shift_down()
            case 5:
                show_sum_row()
            case 6:
                update_element()
            case 7:
                show()
            case 8:
                break
            case _:
                print("Opción incorrecta.")

    print("¡Adiós! :-)")


def show_menu():
    print(f"\nMenú para manejo de una matriz de {ROWS}x{COLUMNS}\n")
    print("1. Rellenar la matriz con números aleatorios.")
    print("2. Rellenar la matriz con números aleatorios sin que se repitan.")
    print("3. Desplazar todos los números una posición hacia la derecha.")
    print("4. Desplazar todos los números una posición hacia abajo.")
    print("5. Calcular la suma de los elementos de una fila.")
    print("6. Modificar un elemento de la matriz.")
    print("7. Mostrar la matriz.")
    print("8. Terminar.\n")


def input_option():
    while True:
        option = input("Dame una opción del menú: ")
        if option.isdigit():
            break
        print("Solo puede introducir opciones numéricas.")
    return int(option)


def fill(min_number, max_number, allow_repeat = True):
    for i in range(ROWS):
        for j in range(COLUMNS):
            n = rand_number(min_number, max_number, allow_repeat)
            matrix[i][j] = n


def rand_number(min_number, max_number, allow_repeat):
    n = random.randint(min_number, max_number)
    if allow_repeat:
        return n
    while is_in_matrix(n):
        n = random.randint(min_number, max_number)
    return n


def is_in_matrix(n):
    """
    Versión más intuitiva pero menos pythonica:

    for i in range(ROWS):
        for j in range(COLUMNS):
            if n == matrix[i][j]:
                return True
    return False
    """
    for row in matrix:
        if n in row:
            return True
    return False


def shift_right():
    for row in matrix:
        last = row[-1]
        for i in range(COLUMNS-1, 0, -1):
            row[i] = row[i-1]
        row[0] = last


def shift_down():
    for col in range(COLUMNS):
        last = matrix[ROWS-1][col]
        for row in range(ROWS-1, 0, -1):
            matrix[row][col] = matrix[row-1][col]
        matrix[0][col] = last


def show_sum_row():
    row = input_row()
    if row == -1:
        return
    print(f"La suma de los elementos de la fila {row} es {sum_row(row)}")


def sum_row(row):
    total = 0
    for n in matrix[row-1]:
        total += n
    return total


def update_element():
    i, j = input_row_column()
    print(f"En la posición ({i},{j}) el valor de la matriz es {matrix[i-1][j-1]}")
    while True:
        resp = input("¿Lo cambiamos? (Sí/No)? ").lower()
        if resp in ["sí", "no"]:
            break
        print("Responda con Sí o No.")
    if resp == "sí":
        n = input(f"Deme el nuevo valor para las posiciones ({i},{j}): ")
        if n.isdigit():
            matrix[i-1][j-1] = int(n)
        else:
            print("Solo puede introducir valores enteros.")

def input_row_column():
    row = input_row()
    col = input_column()
    return row, col


def input_row():
    row = int(input("Dame la fila: "))
    if row < 1 or row > ROWS:
        print(f"La fila es incorrecta, debe estar entre 1 y {ROWS}")
        return -1
    return row


def input_column():
    col = int(input("Dame la columna: "))
    if col < 1 or col > COLUMNS:
        print(f"La columna es incorrecta, debe estar entre 1 y {COLUMNS}")
        return -1
    return col


def show():
    num_digits = len(str(MAX_NUMBER)) # número de cifras a mostrar
    for row in matrix:
        for n in row:
            print(f"{n:{num_digits}}", end=" ")
        print()


if __name__ == "__main__":
    main()
