"""
Este programa pedirá al usuario/a un valor entre 1 y 7 y nos dirá
el día de la semana al que corresponde.

Autoría: clase de 1º de Daw-B.
Fecha: 20/10/2020.

Análisis:
Pedir un número e indicar a qué día de la semana corresponde.
Si no está entre 1 y 7 decir que hay un error.
"""

print("Cálculo del día de la semana")
print("----------------------------")

# Pedir datos
n = int(input("Número de día de la semana: "))

# Cálculo e impresión del día
if n == 1:
    print("Lunes")
elif n == 2:
    print("Martes")
elif n == 3:
    print("Miércoles")
elif n == 4:
    print("Jueves")
elif n == 5:
    print("Viernes")
elif n == 6:
    print("Sábado")
elif n == 7:
    print("Domingo")
else:
    print("No corresponde a ningún día de la semana")
