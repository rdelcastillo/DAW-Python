"""
Test clase TrickedLudoDice.
"""
from tricked_ludo_dice import TrickedLudoDice

d = TrickedLudoDice()
print("Tiramos el dado trucado tres veces de manera normal:")
for i in range(3):
    d.roll()
    print(f"Tirada {i+1}: {d}")

d.put(5)
print(f"Le hemos asignado al dado un 5: {d}")

d.roll()
print(f"Tiramos el dado de nuevo: {d}")

input("Y si intentamos asignarle un valor de nuevo saltará una excepción por no haber tirado tres veces. Pulsa Intro")
d.put(5)
