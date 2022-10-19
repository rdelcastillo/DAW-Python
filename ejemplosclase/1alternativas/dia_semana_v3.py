"""
Este programa pide un día de la semana y nos dice su nombre.

Usaremos la instrucción match de Python (a partir versión 3.10).

Fecha: 14/10/2022
Autor: Rafael del Castillo
"""

print('Cálculo del día de la semana')
print('----------------------------')

day_of_week = int(input('Dime el número de día de la semana que quieres saber: '))

match day_of_week:
    case 1:
        print('Lunes')
    case 2:
        print('Martes')
    case 3:
        print('Miércoles')
    case 4:
        print('Jueves')
    case 5:
        print('Viernes')
    case 6:
        print('Sábado')
    case 7:
        print('Domingo')
    case _:
        print('No existe ese día de la semana')
