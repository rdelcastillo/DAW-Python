import random

"""
Guardamos en un array de 15 × 5 elementos la calificación obtenida por 15 estudiantes 
(a los que conocemos por su número de lista) en la evaluación de 5 ejercicios entregados
semanalmente (cuando un ejercicio no se ha entregado, la calificación es −1). 
 
También guardamos en otro array los nombres de los 15 estudiantes, inicializa este 
array con los valores que quieras.
 
El programa muestre y ejecute el siguiente menú:
 
1. Generar aleatoriamente las calificaciones (enteros entre -1 y 10).
2. Mostrar el número de ejercicios entregados por un estudiante.
3. Mostrar la media de los ejercicios entregados por un estudiante (si los entregó 
todos; en caso contrario, la media es 0).
4. Mostrar la cantidad de estudiantes que han entregado todos los ejercicios y tienen 
una media superior o igual a un 5.
5. Mostrar el número de estudiantes que han presentado un ejercicio dado.
6. Dado el número de un ejercicio, mostrar la nota media obtenida por los estudiantes 
que lo presentaron.
7. Dado el número de un ejercicio, mostrar la nota más alta obtenida.
8. Dado el número de un ejercicio, mostrar la nota más baja obtenida.
9. Mostrar la relación de estudiantes y sus notas.
10. Finalizar.
 
A tener en cuenta:

- Cuando una opción necesite saber a qué estudiante nos referimos damos su número 
  (empezamos en 1) y al mostrar el resultado tiene que salir este número y su nombre.
- Si el array de calificaciones no se ha generado no funcionan las demás opciones.
- Si se da una opción equivocada en el menú se muestra un error.
 
Para este programa tienes que hacer y usar (como mínimo) las siguientes funciones:
 
 - Dado el número de un estudiante, devolver el número de ejercicios entregados.
 - Dado el número de un estudiante, devolver la media sobre los ejercicios entregados, 
   si los entregó todos; en caso contrario, la media es 0.
 - Devolver el número de todos los estudiantes que han entregado todos los ejercicios y 
   tienen una media superior a un valor pasado a la función como parámetro.
 - Dado el número de un ejercicio, devolver el número de estudiantes que lo han presentado.
 - Dado el número de un ejercicio, devolver la nota media obtenida por los estudiantes que
   lo presentaron.
 - Dado el número de un ejercicio, devolver la nota más alta obtenida.
 - Dado el número de un ejercicio, devolver la nota más baja obtenida (sin contar -1).
 
@author Rafael del Castillo Gomariz
"""


def menu() -> int:
    """Imprime el menú y devuelve la opción escogida."""

    # escribo el menú
    print("Menú de opciones")
    print("----------------")
    print("1.Generar aleatoriamente las calificaciones.\n"
          + "2.Mostrar el número de ejercicios entregados por un estudiante.\n"
          + "3.Mostrar la media de los ejercicios entregados por un estudiante.\n"
          + "4.Mostrar la cantidad de estudiantes que han entregado todos los ejercicios y tienen una media >= 5.\n"
          + "5.Mostrar el número de estudiantes que han presentado un ejercicio dado.\n"
          + "6.Dado el número de un ejercicio, mostrar la nota media obtenida por los estudiantes que lo presentaron.\n"
          + "7.Dado el número de un ejercicio, mostrar la nota más alta obtenida.\n"
          + "8.Dado el número de un ejercicio, mostrar la nota más baja obtenida.\n"
          + "9.Mostrar la relación de estudiantes y sus notas.\n"
          + "10.Finalizar.")

    # leo la opción
    opc = int(input("\nIntroduce una opción: "))
    # acabo
    print("\n")
    return opc


def genera_calificaciones():
    """Genera las calificaciones aleatoriamente."""

    # variables locales a usar (no es obligatorio declararlas)
    fila: int
    columna: int

    # proceso
    for fila in range(NUM_ESTUDIANTES):
        for columna in range(NUM_NOTAS):
            notas[fila][columna] = random.randint(-1, 10)


def pide_ejercicio() -> int:
    """pide número de ejercicio y lo devuelve"""
    ej: int  # anotación para "declarar" variable ej

    while True:
        ej = int(input(f"Dame un número de ejercicio (entre 1 y {NUM_NOTAS}): "))
        if 1 <= ej <= NUM_NOTAS:
            break
    print()
    return ej


def estudiante() -> int:
    """Pide un número de estudiante y lo devuelve"""
    est: int

    while True:
        est = int(input(f"Dame un número de estudiante (entre 1 y {NUM_ESTUDIANTES}): "))
        if not (est < 1 or est > NUM_ESTUDIANTES):
            break
    print()
    return est


def mostrar_ejercicios_entregados(alumno: int):
    """Muestra los ejercicios entregados por un estudiante"""
    print(estudiantes[alumno - 1], " ha entregado ", ejercicios_entregados(alumno), " ejercicios.\n")


def ejercicios_entregados(alumno: int) -> int:
    """Devuelve el número de ejercicios entregados por un estudiante"""
    entregados: int = 0
    nota: int

    for nota in notas[alumno - 1]:
        if nota > -1:
            entregados += 1
    return entregados


def mostrar_media_ejercicios(alumno: int):
    """Muestra la media de los ejercicios entregados, si los entregó todos; en caso contrario, la media es 0"""
    print(f"{estudiantes[alumno - 1]} tiene una media de {media_ejercicios(alumno)}.\n")


def media_ejercicios(alumno: int) -> float:
    """
    Devuelve la media sobre los ejercicios entregados por un estudiante, si los entregó todos;
    en caso contrario, la media es 0.
    """
    suma: float = 0
    nota: int

    for nota in notas[alumno - 1]:
        if nota > -1:  # ha realizado el ejercicio
            suma += nota
        else:
            return 0  # no ha hecho todo, la media es 0
    return suma / NUM_NOTAS


def numero_estudiantes_presenta_ejercicio(ejercicio: int) -> int:
    """Devuelve el número de estudiantes que han realizado un ejercicio"""
    n: int = 0
    fila: int

    for fila in range(NUM_ESTUDIANTES):
        if notas[fila][ejercicio - 1] > -1:
            n += 1
    return n


def media_ejercicio(ejercicio: int) -> float:
    """Devuelve la media de un ejercicio contando solo a quienes lo presentaron"""
    suma: float = 0
    num_estudiantes: int = 0

    for fila in range(NUM_ESTUDIANTES):
        if notas[fila][ejercicio - 1] > -1:
            suma += notas[fila][ejercicio - 1]
            num_estudiantes += 1
    return suma / num_estudiantes


def maximo_ejercicio(ejercicio: int) -> int:
    """Devuelve la máxima calificación de un ejercicio"""
    lista_notas: list = []

    for fila in range(NUM_ESTUDIANTES):
        lista_notas.append(notas[fila][ejercicio - 1])
    return max(lista_notas)


def minimo_ejercicio(ejercicio: int) -> int:
    """Devuelve la mínima calificación de un ejercicio"""
    lista_notas: list = []

    for fila in range(NUM_ESTUDIANTES):
        lista_notas.append(notas[fila][ejercicio - 1])
    return min(lista_notas)


def numero_estudiantes_entrega_todo_con_nota_mayor(nota: int) -> int:
    """
    Devuelve el número de estudiantes con todo entregado y nota mayor o igual que la nota pasada
    como parámetro.
    """
    n: int = 0
    fila: int

    for fila in range(NUM_ESTUDIANTES):
        # si ha entregado todo compruebo que la media sea mayor que nota, entonces contabilizo
        if ejercicios_entregados(fila + 1) == NUM_NOTAS and media_ejercicios(fila + 1) >= nota:
            n += 1
    return n


def mostrar_notas():
    """Muestra las notas de los estudiantes"""

    # cabecera
    print(" " * 24, end="")  # blancos iniciales
    for nota in range(NUM_NOTAS):
        print(f"{nota + 1 : 2d} ", end="")
    print("\n" + " " * 24 + "-" * (NUM_NOTAS * 3))

    # estudiantes
    for fila in range(NUM_ESTUDIANTES):
        print(f"{fila + 1 :2d}. {estudiantes[fila] :20s}", end="")
        for columna in range(NUM_NOTAS):
            print(f"{notas[fila][columna] :2d} ", end="")
        print()
    print()


# ------------------
# PROGRAMA PRINCIPAL
# ------------------

# Constantes
NUM_NOTAS: int = 5
NUM_ESTUDIANTES: int = 15

# Variables globales
estudiantes: list = [None] * NUM_ESTUDIANTES
notas: list = [[None] * NUM_NOTAS for i in range(NUM_ESTUDIANTES)]

# Variables "locales" al programa principal
opcion: int
continuar: bool = True
datos_generados: bool = False

# Inicializamos el array de estudiantes
for i in range(len(estudiantes)):
    estudiantes[i] = f"Estudiante {i + 1}"

# Proceso
while True:
    opcion = menu()
    if opcion == 1:  # generamos las calificaciones
        genera_calificaciones()
        datos_generados = True
    elif 2 <= opcion <= 9:
        if datos_generados:  # si se han las calificaciones
            if opcion == 2:
                mostrar_ejercicios_entregados(estudiante())
            elif opcion == 3:
                mostrar_media_ejercicios(estudiante())
            elif opcion == 4:
                print(numero_estudiantes_entrega_todo_con_nota_mayor(5), "estudiantes.\n")
            elif opcion == 5:
                print(numero_estudiantes_presenta_ejercicio(pide_ejercicio()), "estudiantes.\n")
            elif opcion == 6:
                print("La media es", media_ejercicio(pide_ejercicio()), "\n")
            elif opcion == 7:
                print("La máxima nota es", maximo_ejercicio(pide_ejercicio()), "\n")
            elif opcion == 8:
                print("La mínima nota es", minimo_ejercicio(pide_ejercicio()), "\n")
            else:  # opción 9
                mostrar_notas()
            input("Pulse Intro para continuar...\n")
        else:
            print("Primero debe generar las calificaciones.\n")
    elif opcion == 10:  # Fin
        break
    else:
        print("Opción incorrecta\n")

print("¡Adiós!")
