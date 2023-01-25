"""
Clase Gato derivada de Animal. Además de las características definidas para los animales, los gatos tendrán una raza.

Al tener la clase Animal el método eat() como abstracto es obligatorio implementarlo.

Ejemplo sacado del libro "Aprende Java con Ejercicios" de Luis José Sánchez:
https://github.com/LuisJoseSanchez/aprende-java-con-ejercicios

Adaptado a Python por Rafael del Castillo Gomariz.
"""
from animal import Animal, Sex
from typeguard import typechecked

@typechecked
class Cat(Animal):

    def __init__(self, name: str, sex: Sex = Sex.HEMBRA, species: str = ''):
        super().__init__(name, sex)
        self.species = species

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        self.__species = value

    def eat(self, food: str):
        """
        Hace que el gato coma. A los gatos les gusta el pescado, si le damos otra comida la rechazará.
        """
        print(f"({self.name}) ", end="")
        if food == "pescado":
            print("Hmmmm, gracias :-)")
        else:
            print("Lo siento, yo solo como pescado.")

    def __str__(self):  # redefinimos este método basándonos en la clase base
        super().__str__() + "Raza: " + self.species + "\n*************************\n"
