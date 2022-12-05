"""
Se desea almacenar las calificaciones del alumnado de 1DAW del IES Gran Capitán en los módulos de PROGRAMACIÓN,
LENGUAJE DE MARCAS, BASES DE DATOS Y SISTEMAS INFORMÁTICOS.

El número de alumnos no lo sabemos de antemano por lo que se han de añadir conforme se vayan introduciendo los datos.

El programa pedirá el nombre y apellidos del alumno y a continuación las calificaciones en los módulos mencionados
anteriormente.

Cuando el usuario desee dejar de introducir información deberá de introducir una cadena vacía al introducir el nombre.

Asimismo el programa deberá de proporcionar las siguientes funcionalidades:

- Impresión de las calificaciones del curso completo.
- Impresión de las calificaciones de un alumno en concreto. El programa pedirá nombre y apellidos del alumno y de
  encontrarlo mostrará las calificaciones de todos los módulos de este alumno.
- Nota media de un módulo. Se pedirá al usuario el nombre del módulo tras lo cual el programa mostrará la nota media.
- Nota máxima en un módulo. Se pedirá al usuario el nombre del módulo tras lo cual el programa mostrará la nota máxima
  así como el alumno con la misma.
- Nota más baja en un módulo. Se pedirá al usuario el nombre del módulo tras lo cual el programa mostrará la nota más
  baja así como el alumno con la misma.
- Listado ordenado de los datos con respecto a su nota (de mayor a menor). El programa pedirá el módulo y deberá de ser
  capaz de realizar una ordenación descendente por dicha nota.

Este programa es mejor hacerlo con funciones, saldrá más corto, más legible y más eficiente.
"""
import random
from statistics import mean

MODULES = ["Programación", "Lenguaje de Marcas", "Bases de Datos", "Sistemas Informáticos"]
LEN_STUDENT_NAME = 30
LEN_MARK_NAME = 22
MARK_FORMAT = "5.2f"

def input_marks():
    """Lectura por teclado de las notas de los y las estudiantes"""
    def input_mark(mod):
        while True:
            mark = float(input(f"Dame su nota en {mod} (entre 0 y 10): "))
            if 0 <= mark <= 10:
                break
            print("El valor de la nota es erróneo, debe ser entre 0 y 10")
        return mark

    while True:
        student_name = input("\nDame el nombre y apellidos del alumno/a a dar de alta (Intro para terminar): ")
        if student_name == "":
            break
        marks = []
        for module in MODULES:
            marks.append(input_mark(module))
        students.append([student_name] + marks)

def print_marks_course():
    """Impresión por pantalla de las notas del curso"""
    print(f"\n{'Estudiante':{LEN_STUDENT_NAME}} PROGR L.MAR B.DAT S.INF\n") # cabecera listado
    for student in students:
        print(f"{student[0]:{LEN_STUDENT_NAME}} ", end="")   # nombre estudiante
        marks = student[1:]
        for mark in marks:
            print(f"{mark:{MARK_FORMAT}} ", end="")    # nota estudiante formateada
        print()

def print_marks_student():
    """Impresión de las notas de un/a estudiante"""
    def print_marks():
        marks = student[1:]
        for i in range(len(MODULES)):
            print(f"{MODULES[i]+':':{LEN_MARK_NAME}} {marks[i]:{MARK_FORMAT}}")

    student_name = input("Nombre del o de la estudiante: ")
    for student in students:
        if student[0] == student_name:
            print_marks()
            return
    print("Ese nombre de estudiante no existe.")

def input_module():
    """Pide el código de un módulo, devuelve -1 si se mete mal"""
    module = int(input("Número de módulo (1-PROGR 2-L.MAR 3-B.DAT 4-S.INF): "))
    if module < 0 or module > len(MODULES):
        print("ERROR. El número de módulo es erróneo.")
        return -1
    return module

def print_marks_module_sorted():
    """Listado ordenado de estudiantes respecto a la nota de un módulo"""
    module = int(input("Número de módulo (1-PROGR 2-L.MAR 3-B.DAT 4-S.INF): "))
    if module == -1:
        return
    marks = [[student[module], student[0]] for student in students] # lista auxiliar con nota y nombre estudiante
    marks.sort(reverse=True)
    for mark in marks:
        print(f"{mark[1]:{LEN_STUDENT_NAME}} {mark[0]:{MARK_FORMAT}}")

def print_min_mark_module():
    """Imprime la nota más baja de un módulo"""
    module = input_module()
    if module != -1:
        marks = [student[module] for student in students]
        print(f"La nota más baja de {MODULES[module-1]} es {min(marks)}")

def print_max_mark_module():
    """Imprime la nota más alta de un módulo"""
    module = input_module()
    if module != -1:
        marks = [student[module] for student in students]
        print(f"La nota más alta de {MODULES[module-1]} es {max(marks)}")

def print_mean_module():
    """Imprime la nota media de un módulo"""
    module = input_module()
    if module != -1:
        marks = [student[module] for student in students]
        print(f"La nota media de {MODULES[module-1]} es {mean(marks)}")

def fill_students_randomly(n):
    for i in range(n):
        marks = [random.randint(0,1000)/100 for _ in range(4)]  # 4 notas (float) entre 0 y 10 aleatorias
        students.append([f"Estudiante {i+1}"] + marks)


# Programa principal
print("Gestión de calificaciones")
print("-------------------------")

students = []
# fill_students_randomly(20) # la usaremos para hacer pruebas y no tener que meter los datos

input_marks()

while True:
    # mostramos las opciones del menú
    print("\nMenú de opciones para gestionar notas\n"
          "_____________________________________\n"
          "1. Impresión de las calificaciones del curso completo.\n"
          "2. Impresión de las calificaciones de un/a estudiante.\n"
          "3. Nota media de un módulo.\n"
          "4. Nota máxima en un módulo.\n"
          "5. Nota más baja en un módulo.\n"
          "6. Listado ordenado de los estudiantes respecto a su nota en un módulo (de mayor a menor).\n"
          "7. Finalizar.\n")

    option = int(input("Introduzca una opción: "))
    if option == 1:
        print_marks_course()
    elif option == 2:
        print_marks_student()
    elif option == 3:
        print_mean_module()
    elif option == 4:
        print_max_mark_module()
    elif option == 5:
        print_min_mark_module()
    elif option == 6:
        print_ma0rks_module_sorted()
    elif option == 7:
        break
    else:
        print("\nLa opción introducida es errónea")

print("\n¡Hasta la próxima! :-)")
