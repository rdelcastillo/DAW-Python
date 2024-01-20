"""
En esta versión de la clase 'Gato Simple' sustituimos el uso de getters y setters por propiedades, que es la forma
"pythonica" de hacerlo, añadimos más funcionalidad a la propiedad 'fecha de nacimiento' y creamos una propiedad de solo
lectura que nos da la edad del gato.

Ejemplo sacado del libro "Aprende Java con Ejercicios" de Luis José Sánchez:
https://github.com/LuisJoseSanchez/aprende-java-con-ejercicios

Adaptado a Python por Rafael del Castillo Gomariz.

Fecha: 7/01/2023.
"""
import datetime


class PlainCat:

    def __init__(self, name, sex, species='', birthday=datetime.date.today()):
        """
        Constructor de 'Gato Simple', necesita un nombre y un sexo, que no podrán ser modificados una vez creado el
        objeto. Además, se puede especificar una raza y fecha de nacimiento que sí podrán ser modificadas.
        """
        if sex not in ['macho', 'hembra']:
            raise ValueError(f"{sex} es un sexo incorrecto.")
        self.__name = name
        self.__sex = sex
        self.species = species  # invocamos al setter a través de la propiedad
        self.birthday = birthday

    @property
    def name(self):
        return self.__name

    @property
    def sex(self):
        return self.__sex

    @property
    def species(self):
        return self.__species

    @species.setter
    def species(self, value):
        self.__species = value.upper()

    @property
    def birthday(self):
        return self.__birthday

    @birthday.setter
    def birthday(self, value):  # admitimos tanto una fecha como una cadena formateada como tal
        if isinstance(value, datetime.date):
            self.__birthday = value
        elif isinstance(value, str):  # cadena formateada como fecha que convertimos a datetime.date
            self.__birthday = datetime.datetime.strptime(value, "%d/%m/%Y").date()
        else:
            raise TypeError(f"{value} no es un objeto de clase datetime.date")

    @property
    def age(self):
        age_cat = datetime.date.today().year - self.birthday.year
        if not self.__has_a_birthday_this_year():
            age_cat -= 1
        return age_cat

    def __has_a_birthday_this_year(self):
        today = datetime.date.today()
        if today.month > self.birthday.month:
            return True
        if today.month == self.birthday.month and today.day >= self.birthday.day:
            return True
        return False

    def meow(self):
        print(f"({self.name}) Miauuuu!!!")

    def purr(self):
        print(f"({self.name}) Mrrrrrr!!!")

    def eat(self, food):
        """
        Hace que el gato coma. A los gatos les gusta el pescado, si le damos otra comida la rechazará.
        """
        print(f"({self.name}) ", end="")
        if food == "pescado":
            print("Hmmmm, gracias :-)")
        else:
            print("Lo siento, yo solo como pescado.")

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
