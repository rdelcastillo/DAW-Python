"""
Pide una fecha en formato dd/mm/aaaa del siglo XXI, comprueba si es correcta, en caso de no serlo, señala el error
correspondiente (en el dispositivo de errores) y acaba el programa de forma anormal, en caso de serlo, muestra el día
siguiente a la misma en el mismo formato.

Algoritmo:
----------
PEDIR fecha

* Comprobamos fecha correcta
SI LONGITUD(fecha) <> 10 O NO_TIENE_/
    FIN
FIN-SI

dia <-- EXTRAER_DIA_DE(fecha)
mes <-- EXTRAER_MES_DE(fecha)
año <-- EXTRAER_DIA_DE(fecha)

SI NO_ES_NUMÉRICO(dia) O NO_ES_NUMÉRICO(mes) O NO_ES_NUMÉRICO(año)
    FIN
FIN-SI

SI año < 2000 O año >=2100
    FIN
FIN-SI

SI mes == 0 O mes > 12
    FIN
FIN-SI

dias_mes = CALCULAR_DIAS_MES(mes, año)
SI dia == 0 o DIA > dias_mes
    FIN
FIN-SI

* Calculamos día siguiente
dia <-- dia + 1
SI dia > dias_mes
    dia <-- 1
    mes <-- mes + 1
    SI mes > 12
        mes <-- 1
        año <-- año + 1
    FIN-SI
FIN-SI

ESCRIBIR dia + "/" + mes + "/" + año
-----------------

Fecha: 25/11/2021
Autor: Rafael del Castillo
"""
import sys

print("Día siguiente a una fecha")
print("-------------------------")
date = input("Dame una fecha en formato dd/mm/aaaa: ")

# ¿Fecha correcta?

# ¿longitud correcta y separadores son "/"?
if len(date) != 10 or date[2] != "/" or date[5] != "/":
    print("Formato de fecha incorrecto", file=sys.stderr)
    exit(1)

# ¿datos numéricos?
day_str = date[0:2]
month_str = date[3:5]
year_str = date[6:]
if not day_str.isdigit() or not month_str.isdigit() or not year_str.isdigit():
    print("El día, mes y/o año no son numéricos", file=sys.stderr)
    exit(1)

# ¿año correcto?
year = int(year_str)
if year < 2000 or year >= 2100:
    print("No es una fecha del siglo XXI", file=sys.stderr)
    exit(1)

# ¿mes correcto?
month = int(month_str)
if month == 0 or month > 12:
    print("Mes incorrecto", file=sys.stderr)
    exit(1)

# ¿día correcto?
# primero calculamos cuantos días tiene el mes
days_month = 31  # la mayoría de meses tiene 31 días
if month == 4 or month == 6 or month == 9 or month == 11:
    days_month = 30
elif month == 2:
    if year % 4 == 0 and (year % 100 != 0 or year % 400 == 0):  # ¿bisiesto?
        days_month = 29
    else:
        days_month = 28
# ¿el valor del día está en el rango correcto?
day = int(day_str)
if day == 0 or day > days_month:
    print("Día incorrecto", file=sys.stderr)
    exit(1)

# Cálculo del día siguiente
day += 1
if day > days_month:    # me voy al mes siguiente
    day = 1
    month += 1
    if month > 12:      # me voy al año siguiente
        month = 1
        year += 1

# Resultado
print(f"El día siguiente es {day:02}/{month:02}/{year:02}")
