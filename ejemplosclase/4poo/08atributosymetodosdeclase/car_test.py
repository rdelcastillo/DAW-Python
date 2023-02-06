"""
Prueba de la clase Coche.
"""
from car import Car

car1 = Car("2007-GVG")
car2 = Car("0891-YST")
car3 = Car("0922-HJK")

car1.travel(30)
car1.travel(100)
car1.travel(130)

car2.travel(50)
car2.travel(70)
car2.travel(10)

car3.travel(25)
car3.travel(75)
car3.travel(85)

print(f"El coche {car1.registration} ha recorrido {car1.mileage} Km.")
print(f"El coche {car2.registration} ha recorrido {car2.mileage} Km.")
print(f"El coche {car3.registration} ha recorrido {car3.mileage} Km.")
print(f"El kilometraje total ha sido de {Car.total_mileage()} Km.")

print(f"Damos de baja el coche {car2}")
del car2
print(f"El kilometraje total ha sido de {Car.total_mileage()} Km.")
