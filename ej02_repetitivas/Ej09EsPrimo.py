'''
Este codigo ha sido generado por el modulo psexport 20180125-l64 de PSeInt.
Es posible que el codigo generado no sea completamente correcto. Si encuentra
errores por favor reportelos en el foro (http:#pseint.sourceforge.net).

Retocado por Rafael del Castillo con el comando sed.
'''
import math


# ################################################################################
# Escribe un programa que diga si un número introducido por teclado es o no primo.
# Un número primo es aquel que sólo es divisible entre él mismo y la unidad.
# Nota: Es suficiente probar hasta la raíz cuadrada del número para ver si es
# divisible por algún otro número.
# ################################################################################
# Análisis
# Leemos un número y vamos comprobando si es divisible entre 2 hasta la raíz
# cuadrada del número. Si es divisible por algún número no es primo.
# Si no es divisible por ningún número es primo.
# Para saber si es divisible usamos el operador módulo.
# Datos de entrada: el número a comprobar si es primo o no
# Información de salida: Un mensaje diciendo si es primo o no
# Variables: numero_es_primo (entero), num (entero) contador desde 2 hasta
# raíz cuadrada del num_es_primo, es_primo (lógico)
# ################################################################################
# Diseño
# 1.- Supongo que el número es primo -> es_primo<-Verdadero
# 2.- Leer num_es_primo
# 3.- Desde num = 2 hasta raíz(numero_es_rpimo)
# 4.- Si numero_es_primo es divisible entre num -> es_primo<-Falso
# 5.- Si es_primo -> Mostrar "Es primo"
# 6.- Si no -> Mostrar "No es primo"
# ################################################################################

es_primo = True

# Pedimos datos
numero_es_primo = int(input("Introduce un número para comprobar si es primo: "))

# Proceso
num=2
while num<=math.sqrt(numero_es_primo) and es_primo:
    if numero_es_primo%num==0:
        es_primo = False
    num+=1
    
# Mostramos resultado    
if es_primo:
    print("Es Primo")
else:
    print("No es Primo")

