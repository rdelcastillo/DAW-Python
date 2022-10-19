"""
Este programa pide un mes y nos dice cuantos días tiene.

Usaremos la instrucción match de Python (a partir versión 3.10).

Fecha: 14/10/2022
Autor: Rafael del Castillo
"""

print('Cálculo del número de días de un mes')
print('------------------------------------')

day_of_month = int(input('Dime el mes del que quieres saber los días: '))

match day_of_month:
    case 1 | 3 | 5 | 7 | 8 | 10 | 12:
        print('El mes tiene 31 días')
    case 2:
        print('El mes tiene 28 días y en los años bisiestos 29 días')
    case 4 | 6 | 9 | 11:
        print('El mes tiene 30 días')
    case _:
        print('Ese mes no existe')
