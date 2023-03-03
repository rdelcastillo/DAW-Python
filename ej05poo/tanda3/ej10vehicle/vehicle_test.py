import random

from ej05poo.tanda2.ej08_menu import Menu
from bike import Bike
from car import Car
from vehicle import Vehicle

MIN_TRAVEL_BIKE = 10
MAX_TRAVEL_BIKE = 50
MIN_TRAVEL_CAR = 50
MAX_TRAVEL_CAR = 500

my_bike = Bike()
my_car = Car()


def main():
    menu = Menu("Anda con la bicicleta", "Haz el caballito con la bicicleta", "Anda con el coche",
                "Quema rueda con el coche", "Ver kilometraje de la bicicleta", "Ver kilometraje del coche",
                "Ver kilometraje total", "Salir", title = "VEHÍCULOS")
    while True:
        opc = menu.choose()
        match opc:
            case 1: travel_with_bike()
            case 2: my_bike.do_wheelie()
            case 3: travel_with_car()
            case 4: my_car.do_burnout()
            case 5: show_bike_mileage()
            case 6: show_car_mileage()
            case 7: show_total_mileage()
            case _: break
    print("Hasta la próxima! :-)")


def travel_with_bike():
    kilometers = random.randint(MIN_TRAVEL_BIKE, MAX_TRAVEL_BIKE)
    my_bike.travel(kilometers)
    print("La bicicleta recorre", kilometers, "kms.\n")


def travel_with_car():
    kilometers = random.randint(MIN_TRAVEL_CAR, MAX_TRAVEL_CAR)
    my_car.travel(kilometers)
    print("El coche recorre", kilometers, "kms.\n")


def show_bike_mileage():
    print("El kilometraje de la bicicleta es de", my_bike.kilometers_traveled, "kms.\n")


def show_car_mileage():
    print("El kilometraje del coche es de", my_car.kilometers_traveled, "kms.\n")


def show_total_mileage():
    print("El kilometraje TOTAL es de", Vehicle.total_kilometers(), "kms.\n")


if __name__ == '__main__':
    main()