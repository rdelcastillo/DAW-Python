"""
Clase Gato derivada de Animal. Además de las características definidas para los animales, los gatos tendrán una raza.

Al tener la clase Animal el método eat() como abstracto es obligatorio implementarlo.

Ejemplo sacado del libro "Aprende Java con Ejercicios" de Luis José Sánchez:
https://github.com/LuisJoseSanchez/aprende-java-con-ejercicios

Adaptado a Python por Rafael del Castillo Gomariz.
"""
import datetime
from animal import Animal, Sex
from typeguard import typechecked

@typechecked
class Cat(Animal):

    def __init__(self, name: str, sex: Sex = Sex.HEMBRA, species: str = '', birth_day=datetime.date.today()):
        super().__init__(name, sex)
        self.species = species
        self.birth_day = birth_day

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        self.__species = value

    @property
    def birth_day(self):
        return self.__birthday

    @birth_day.setter
    def birth_day(self, value):  # admitimos tanto una fecha como una cadena formateada como tal
        if isinstance(value, datetime.date):
            self.__birthday = value
        elif isinstance(value, str):  # cadena formateada como fecha que convertimos a datetime.date
            self.__birthday = datetime.datetime.strptime(value, "%d/%m/%Y").date()
        else:
            raise TypeError(f"{value} no es un objeto de clase datetime.date")

    @property
    def age(self):
        age_cat = datetime.date.today().year - self.birth_day.year
        if not self.__has_a_birthday_this_year():
            age_cat -= 1
        return age_cat

    def __has_a_birthday_this_year(self):
        today = datetime.date.today()
        if today.month > self.birth_day.month:
            return True
        if today.month == self.birth_day.month and today.day >= self.birth_day.day:
            return True
        return False

    def eat(self, food: str):
        """
        Hace que el gato coma. A los gatos les gusta el pescado, si le damos otra comida la rechazará.
        """
        print(f"({self.name}) ", end="")
        if food == "pescado":
            print("Hmmmm, gracias :-)")
        else:
            print("Lo siento, yo solo como pescado.")

    def meow(self):
        print(f"({self.name}) Miauuuu!!!")

    def purr(self):
        print(f"({self.name}) Mrrrrrr!!!")

    def fight_with(self, opponent):
        """
        Pone a pelear dos gatos. Solo se van a pelear dos machos entre sí.
        """
        print(f"({self.name}) ", end="")
        if self.sex == "hembra":
            print("No me gusta pelear.")
        elif opponent.sex == "hembra":
            print("No peleo contra gatitas.")
        else:
            print(f"Ven aquí {opponent.name}, que te vas a enterar :-@")

    def __str__(self):  # redefinimos este método basándonos en la clase base
        return super().__str__() + "Raza: " + self.species + "\n"
