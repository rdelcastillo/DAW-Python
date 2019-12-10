'''
Muestra en pantalla los N primeros números primos. Se pide por teclado la cantidad
de números primos que queremos mostrar.

Análisis:
Tengo que leer la cantidad de números primos que voy a mostrar. La cantidad debe
ser positivo. El primer número primo es el 2 (lo muestro) a partir de este son
todos impares. Voy probando desde el 3 todos los impares hasta que muestre la
cantidad que hemos indicados (necesito un contador).
Para comprobar si son primos, los voy dividiendo desde 3 hasta la raíz cuadrada
del número, si es divisible por algún número no es primo (necesito un indicador).
Datos de entrada: Cantidad de números a mostrar.
Información de salida: Los números primos indicados.
Variables: cantidad_a_mostrar, cant_mostradis, divisor (entero), esPrimo(lógico)

Diseño:
- Leer cantidad de número primos a mostrar, debe ser positivo
- Muestro el primer número primo, el 2.
- Inicializo el contador de número mostrados a 1.
- Inicializo la variable donde guardo el número a probar -> num=3
- Mientras no haya mostrado la cantidad de número indicados
- Considero que es primo. Inicializo el indicador -> esPrimo=Verdadero
- desde el 3 hasta la raíz cuadrada del número
- Si es divisible -> Ya no es primo -> esPrimo=Falso
- Si es primo
- Incremento el contador de números mostrados
- Escribo el número primo
- Como son impares, incremento en 2 el número a probar


@author Rafael del Castillo

'''

import math

# ---------
# Funciones
# ---------

def esPrimo(n):
    '''
    Comprueba si el parámetro que recibe es o no un número primo.

    @param n número entero a comprobar

    @return True si es primo
            False si no es primo
    '''
    esprimo = True
    for i in range(3, int(math.sqrt(n))+1):
        if n%i==0:  # es divisible, no es primo, acabamos
            return False
    return esprimo

# ---------
# Principal
# ---------

# Pedimos datos
while True:
    cantidad_a_mostrar = int(input("Ingrese la cantidad de números primos a mostrar: "))
    if not (cantidad_a_mostrar<=0): break

# Proceso
# el primer primo es 2, los otros son todos impares...
print("1: 2")
cantidad_mostrados = 1
# ...a partir de 3
num = 3
while cantidad_mostrados < cantidad_a_mostrar:
    # me muevo solo por los números impares
    if esPrimo(num):
        cantidad_mostrados+=1
        print(f"{cantidad_mostrados}: {num}")
    num += 2

