"""
Cálculo del combinatorio de dos números.

Combinatorio(n,m) = n! / (m! * (n-m)!) si n>m

Usamos anotaciones para los tipos.
"""


def factorial(x: int) -> int:
    f: int = 1
    for i in range(x, 0, -1):
        f = f * i
    return f


# Pedimos los datos: n y m de forma que n > m
while True:
    n: int = int(input("indique el valor de n (recuerde que debe ser mayor que m) "))
    m: int = int(input("indique el valor de m (recuerde que debe ser menor que n) "))
    if n > m:
        break

# Cálculo de combinatorio de n sobre m
combinatorio: int = factorial(n) // (factorial(m) * factorial(n - m))
# Resultado
print(f"El número combinatorio de {n} sobre {m} es {combinatorio}")
