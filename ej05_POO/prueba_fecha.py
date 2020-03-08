"""
Probamos la clase fecha
"""
from Fecha import Fecha, FechaErronea

# Pido una fecha
while True:
    try:
        # Pido la fecha
        dia = int(input("Día para construir la fecha: "))
        mes = int(input("Mes para construir la fecha: "))
        anyo = int(input("Año para construir la fecha: "))
        # Construyo la fecha
        fecha = Fecha(dia, mes, anyo)
        print("La fecha introducida es:", fecha)
    except FechaErronea:
        input("Ha introducido una fecha inválida, pulse Intro y vuelva a intentarlo.")
    except:
        input("Ha introducido valores que no son enteros, pulse Intro y vuelva a intentarlo.")
    else:
        break

