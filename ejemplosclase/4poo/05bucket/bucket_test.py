"""
Programa que prueba la clase WaterCube.

Ejemplo sacado del libro "Aprende Java con Ejercicios" de Luis José Sánchez:
https://github.com/LuisJoseSanchez/aprende-java-con-ejercicios

Adaptado a Python por Rafael del Castillo Gomariz.

Fecha: 16/01/2023.
"""
from bucket import Bucket

small_bucket = Bucket(2)
big_bucket = Bucket(7, 1)

print(f"Cubo pequeño:\n{small_bucket}\n")
print(f"Cubo grande:\n{big_bucket}\n")

print("Lleno el cubo pequeño:")
small_bucket.fill()
print(small_bucket)

print(f"\nEl cubo grande está casi vacío:\n{big_bucket}\n")
print("Ahora vuelco lo que tiene el cubo pequeño en el cubo grande.\n")
small_bucket.dump_in(big_bucket)
print(f"Cubo pequeño:\n{small_bucket}\n")
print(f"Cubo grande:\n{big_bucket}\n")

print("Ahora vuelco lo que tiene el cubo grande en el cubo pequeño.\n")
big_bucket.dump_in(small_bucket)
print(f"Cubo pequeño:\n{small_bucket}\n")
print(f"Cubo grande:\n{big_bucket}")
