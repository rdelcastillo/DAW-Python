"""
Este programa pide un día de la semana y nos dice su nombre.

Usaremos la forma compacta del if en Python.

Fecha: 14/10/2022
Autor: Rafael del Castillo
"""

print('Cálculo del día de la semana')
print('----------------------------')

day_of_week = int(input('Dime el número de día de la semana que quieres saber: '))

if day_of_week == 1:
    print('Lunes')
elif day_of_week == 2:
    print('Martes')
elif day_of_week == 3:
    print('Miércoles')
elif day_of_week == 4:
    print('Jueves')
elif day_of_week == 5:
    print('Viernes')
elif day_of_week == 6:
    print('Sábado')
elif day_of_week == 7:
    print('Domingo')
else:
    print('No existe ese día de la semana')
