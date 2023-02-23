"""
Este programa muestra un menú con las siguientes opciones:

- Introducir (por teclado) una fecha pidiendo por teclado año, mes y día en formato dd/mm/aaaa. Si no se introduce
  correctamente se devuelve un mensaje de error. Usa una función booleana para validar la fecha.
- Añadir días a la fecha. Pide un número de días para sumar a la fecha introducida previamente y actualiza su valor.
  Si el número es negativo restará los días. Esta opción solo podrá realizarse si hay una fecha introducida (se ha
  ejecutado la opción anterior), si no la hay mostrará un mensaje de error.
- Añadir meses a la fecha. El mismo procedimiento que la opción anterior.
- Añadir años a la fecha. El mismo procedimiento que la opción 2.
- Comparar la fecha introducida con otra. Pide una fecha al usuario en formato dd/mm/aaaa (válida, si no lo es da error)
  y la comparará con la que tenemos guardada, posteriormente mostrará si esta fecha es anterior, igual o posterior a la que tenemos almacenada y el número de días comprendido entre las dos fechas.
- Mostrar la fecha en formato largo (ejemplo: "lunes, 1 de febrero de 2021").
- Terminar.

Autor: Rafael del Castillo Gomariz
"""
import locale
from datetime import datetime
from dateutil.relativedelta import relativedelta
from ej08_menu import Menu

date_ = None


def main():
    locale.setlocale(locale.LC_TIME, "es_ES.UTF8")
    menu = Menu("Introducir una fecha", "Añadir días a la fecha", "Añadir meses a la fecha",
                "Añadir años a la fecha", "Comparar la fecha con otra", "Mostrar fecha en formato largo",
                "Terminar")
    while True:
        opc = menu.choose()
        if opc != 1 and date_ is None and opc != menu.last_option:
            print("Debes introducir primero una fecha\n")
            continue
        match opc:
            case 1: input_date()
            case 2: add_days()
            case 3: add_months()
            case 4: add_years()
            case 5: compare_dates()
            case 6: print_date()
            case _: break

    print("Hasta la próxima :-)")


def input_date():
    global date_
    date_str = input("Introduzca una fecha en formato dd/mm/aaaa: ")
    date_ = datetime.strptime(date_str, "%d/%m/%Y").date()


def add_days():
    global date_
    days = int(input(f"Introduzca el número de días a añadir a {date_.strftime('%d/%m/%Y')}: "))
    date_ += relativedelta(days=days)


def add_months():
    global date_
    months = int(input(f"Introduzca el número de meses a añadir a {date_.strftime('%d/%m/%Y')}: "))
    date_ += relativedelta(months=months)


def add_years():
    global date_
    years = int(input(f"Introduzca el número de años a añadir a {date_.strftime('%d/%m/%Y')}: "))
    date_ += relativedelta(years=years)


def compare_dates():
    global date_
    date_to_compare_str = input("Introduzca una fecha para comparar con la almacenada en formato dd/mm/aaaa: ")
    date_to_compare = datetime.strptime(date_to_compare_str, "%d/%m/%Y").date()
    if date_to_compare < date_:
        print("La fecha introducida es menor que la fecha almacenada.")
    elif date_to_compare == date_:
        print("La fecha introducida es igual a la fecha almacenada.")
    else:
        print("La fecha introducida es mayor que la fecha almacenada.")


def print_date():
    print(date_.strftime("%A, %d de %B de %Y"))

if __name__ == '__main__':
    main()