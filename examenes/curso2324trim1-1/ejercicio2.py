"""
Se dice que un número es “perfecto” si es igual a la suma de todos sus divisores excluído él mismo. Por ejemplo, 28 es
un número perfecto, pues sus divisores (excepto él mismo) son 1, 2, 4, 7 y 14, que suman 28.

Tienes que realizar un programa que:

1. Pida un número entero mayor que cero. Si lo que introduce el usuario es incorrecto, avisa del error producido y lo
vuelve a pedir hasta que se introduce un número correcto.

2. Averigua si el número introducido es “perfecto” e indica al usuario si lo es o no.

3. Pregunta al usuario/a si quiere continuar, en caso afirmativo vuelve al punto 1. Si la respuesta no es “S” o “N”
(mayúscula o minúscula) hay que decir al usuario/a que no entiendes la respuesta y vuelves a preguntar hasta que tengas
una respuesta correcta.

Cuando el usuario/a no quiera continuar tienes que mostrar la cantidad de números que se han introducido y de ellos,
cuantos eran perfectos.
"""

print("Números perfectos")
print("-----------------")

total_numbers = 0
perfect_counter = 0

while True:
    # Pedir un número correcto
    while True:
        try:
            n = int(input("Introduce un número positivo: "))
            if n > 0:
                break
            print(f"{n} NO es un número positivo.")
        except ValueError:
            print("No has introducido un número entero")

    # ¿Es un número perfecto?

    # sumar los divisores de n
    sum_divisors = 1  # contabilizo el 1 como divisor
    for d in range(2, n):
        if n % d == 0:
            sum_divisors += d

    # compruebo si la suma de los divisores es igual a n (perfecto) y actualizo contadores
    if n == sum_divisors:
        print(f"{n} es un número perfecto")
        perfect_counter += 1
    else:
        print(f"{n} NO es un número perfecto")
    total_numbers += 1

    # ¿Continuamos?
    while True:
        resp = input("¿Quieres continuar introduciendo números? (S/N) ").upper()
        if resp == "S" or resp == "N":
            break
        print("Debes introducir S o N.")

    # Salida de mi ciclo repetir
    if resp == "N":
        break

# Muestro resultados
print(f"\nTotal números introducidos: {total_numbers}")
print(f"Números que eran perfectos: {perfect_counter}")
