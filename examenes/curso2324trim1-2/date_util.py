"""
Colección de funciones para manejar fechas asumiendo que una fecha se guarda en una cadena con el
siguiente formato: 'AAAAMMDD'.

1. ok_date: dice si la fecha que se pasa como parámetro es correcta.

2. tomorrow: suma un día a la fecha que se pasa como parámetro y lo devuelve.

3. next_n_days: suma una serie de días a la fecha que se pasa como parámetro y lo devuelve.

4. yesterday: resta un día a la fecha que se pasa como parámetro y lo devuelve.

5. past_n_days: resta una serie de días a la fecha que se pasa como parámetro y lo devuelve.

6. leap_year: dice si el año de la fecha que se pasa como parámetro es bisiesto.

7. compare_dates: recibe dos fechas y devuelve un valor negativo si la 1ª es anterior a la
   segunda, cero si son iguales, y un valor positivo si la 1ª es posterior a la segunda.

8. date_to_str: recibe un fecha y devuelve una cadena con el formato:
   DD de {MES} de AAAA     (Ejemplo: "15 de Diciembre de 2019")

9. year, month, day, month_name: recibe un fecha y devuelve esos valores.
"""

def ok_date(date):
    if len(date) != 8:
        return False
    if not date.isdigit():
        return False
    day_, month_, year_ = int(date[6:]), int(date[4:6]), int(date[:4])
    if year_ == 0:  # no existe el año 0
        return False
    if month_ < 1 or month_ > 12:
        return False
    if day_ < 1 or day_ > month_days(month_, year_):
        return False
    return True

def month_days(m, y):
    month_days_ = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if leap_year(f"{y}0101"):
        month_days_[1] += 1
    return month_days_[m-1]

def tomorrow(date): # TODO suma un día a la fecha que se pasa como parámetro y lo devuelve
    pass

def next_n_days(date, n): # TODO suma una serie de días a la fecha que se pasa como parámetro y lo devuelve
    pass

def yesterday(date): # TODO resta un día a la fecha que se pasa como parámetro y lo devuelve
    pass

def past_n_days(date, n): # TODO resta una serie de días a la fecha que se pasa como parámetro y lo devuelve
    pass

def leap_year(date): # TODO dice si el año de la fecha que se pasa como parámetro es bisiesto.Ç
    return False

def compare_dates(date1, date2): # TODO
    """
    Devuelve un valor negativo si la date1 es anterior a date2, cero si son iguales, y un valor positivo si
    date1 es posterior a la date2.
    """

def date_to_str(date):
    """
    Recibe una fecha y devuelve una cadena con el formato: DD de {MES} de AAAA (Ejemplo: "15 de diciembre de 2019")
    """
    return f"{day(date)} de {month_name(date)} de {year(date)}"

def year(date):
    check_date(date)
    return int(date[:4])

def month(date):
    check_date(date)
    return int(date[4:6])

def day(date):
    check_date(date)
    return int(date[6:])

def month_name(date):
    month_names = ("enero", "febrero", "marzo", "abril", "mayo", "junio", "julio", "agosto", "septiembre",
                   "octubre", "noviembre", "diciembre")
    return month_names[month(date) - 1]

def check_date(date):
    if not ok_date(date):
        raise TypeError(f"'{date}' no tiene un formato de fecha")

if __name__ == "__main__":
    assert date_to_str("20231221") == "21 de diciembre de 2023"
    assert year("20231221") == 2023
    assert month("20231221") == 12
    assert day("20231221") == 21
    assert month_name("20231221") == "diciembre"

    assert ok_date("20231221")
    assert ok_date("20200229")
    assert not ok_date("20230229")

    assert tomorrow("20231221") == "20231222"
    assert tomorrow("20231231") == "20240101"
    assert tomorrow("20230228") == "20230301"
    assert tomorrow("20200228") == "20200229"

    assert next_n_days("20231221", 5) == "20231226"
    assert next_n_days("20231221", 12) == "20240102"
    assert next_n_days("20231221", 366) == "20241221"

    assert yesterday("20231221") == "20231220"
    assert yesterday("20240101") == "20231231"
    assert yesterday("20230301") == "20230228"
    assert yesterday("20200229") == "20200228"

    assert past_n_days("20231221", 5) == "20231216"
    assert past_n_days("20231221", 365) == "20221221"

    assert not leap_year("20230101")
    assert leap_year("20240202")
    assert not leap_year("21000123")
    assert leap_year("20001010")

    assert compare_dates("20231221", "20240130") < 0
    assert compare_dates("20240130", "20231221") > 0
    assert compare_dates("20231221", "20231221") == 0

    print("Las pruebas se pasaron correctamente")
