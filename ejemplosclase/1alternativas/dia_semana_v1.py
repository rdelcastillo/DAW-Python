"""
Este programa pide un día de la semana y nos dice su nombre.

Usaremos solo instrucciones alternativas dobles.

Fecha: 14/10/2022
Autor: Rafael del Castillo
"""

print('Cálculo del día de la semana')
print('----------------------------')

day_of_week = int(input('Dime el número de día de la semana que quieres saber: '))

if day_of_week == 1:
    print('Lunes')
else:
    if day_of_week == 2:
        print('Martes')
    else:
        if day_of_week == 3:
            print('Miércoles')
        else:
            if day_of_week == 4:
                print('Jueves')
            else:
                if day_of_week == 5:
                    print('Viernes')
                else:
                    if day_of_week == 6:
                        print('Sábado')
                    else:
                        if day_of_week == 7:
                            print('Domingo')
                        else:
                            print('No existe ese día de la semana')
