"""
Mostrar en pantalla los N primeros números primos. Se pide por teclado la cantidad
de números primos que queremos mostrar.
--------
Análisis
--------
Tengo que leer la cantidad de números primos que voy a mostrar, que debe ser positiva.

El primer número primo es el 2 (lo muestro) a partir de este son todos impares. Voy probando desde el 3 todos
los impares hasta que muestre la cantidad que hemos indicado (necesito un contador).

Para comprobar si son primos, los voy dividiendo desde 3 hasta la raíz cuadrada del número, si es divisible por
algún número no es primo (necesito un interruptor).

Datos de entrada: cantidad de números a mostrar.
Información de salida: Los números primos indicados.

Variables: cantidad_a_mostrar, cantidad_mostrados, divisor (entero), es_primo(lógico)
---
Diseño
1.- Leer cantidad de número primos a mostrar, debe ser positivo
2.- Muestro el primer número primo, el 2.
3.- Inicializo el contador de número mostrados a 1.
4.- Inicializo la variable donde guardo el número a probar -> num=3
4.- Mientras no haya mostrado la cantidad de número indicados
5.- Considero que es primo. Inicializo el indicador -> es_primo=Verdadero
6.- desde el 3 hasta la raíz cuadrada del número
7.- Si es divisible -> Ya no es primo -> es_primo=Falso
8.- Si es primo
9.- Incremento el contador de números mostrados
10.- Escribo el número primo
11.- Como son impares, incremento en 2 el número a probar

Usamos una función para comprobar si un número es primo
"""
import math


def es_primo(num_a_comprobar):
    creo_que_es_primo = True
    n = 2
    while n <= math.sqrt(num_a_comprobar) and creo_que_es_primo:
        if num_a_comprobar % n == 0:
            creo_que_es_primo = False
        n += 1
    return creo_que_es_primo


# Principal

# Pedimos datos
while True:  # postcondición
    cantidad_a_mostrar = int(input("Ingrese la cantidad de números primos a mostrar: "))
    if cantidad_a_mostrar > 0:
        break  # condición de salida del ciclo

# Proceso
# el primer primo es 2, los otros son todos impares...
print("1: 2")
cantidad_mostrados = 1
# ...a partir de 3
num = 3
while cantidad_mostrados < cantidad_a_mostrar:
    if es_primo(num):  # Compruebo si "num" es primo
        cantidad_mostrados += 1
        print(f"{cantidad_mostrados}: {num}")
    num += 2
