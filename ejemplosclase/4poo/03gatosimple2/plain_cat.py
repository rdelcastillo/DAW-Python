"""
En esta versión de la clase 'Gato Simple', solucionamos los problemas del ejemplo anterior creando atributos "privados"
y usaremos getters y setters para acceder y modificar los mismos.

El uso de getters y setters como se plantea aquí no es la forma "pythonica" de hacerlo, esta se implementará en la
siguiente versión.

Ejemplo sacado del libro "Aprende Java con Ejercicios" de Luis José Sánchez:
https://github.com/LuisJoseSanchez/aprende-java-con-ejercicios

Adaptado a Python por Rafael del Castillo Gomariz.

Fecha: 7/01/2023.
"""
import datetime


class PlainCat:

    def __init__(self, name, sex, species='', birth_day=datetime.date.today()):
        """
        Constructor de 'Gato Simple', necesita un nombre y un sexo, que no podrán ser modificados una vez creado el
        objeto. Además, se puede especificar una raza y fecha de nacimiento que sí podrán ser modificadas.
        """
        if sex not in ['macho', 'hembra']:
            raise ValueError(f"{sex} es un sexo incorrecto.")
        self.__name = name
        self.__sex = sex
        self.set_species(species)
        self.set_birth_day(birth_day)

    def get_name(self):
        return self.__name

    def get_sex(self):
        return self.__sex

    def get_species(self):
        return self.__species

    def set_species(self, value):
        self.__species = value.upper()

    def get_birth_day(self):
        return self.__birth_day

    def set_birth_day(self, value):
        if not isinstance(value, datetime.date):
            raise ValueError(f"{value} no es un objeto de clase datetime.date")
        self.__birth_day = value

    def meow(self):
        print(f"({self.__name}) Miauuuu!!!")

    def purr(self):
        print(f"({self.__name}) Mrrrrrr!!!")

    def eat(self, food):
        """
        Hace que el gato coma. A los gatos les gusta el pescado, si le damos otra comida la rechazará.
        """
        print(f"({self.__name}) ", end="")
        if food == "pescado":
            print("Hmmmm, gracias :-)")
        else:
            print("Lo siento, yo solo como pescado.")

    def fight_with(self, opponent):
        """
        Pone a pelear dos gatos. Solo se van a pelear dos machos entre sí.
        """
        print(f"({self.__name}) ", end="")
        if self.__sex == "hembra":
            print("No me gusta pelear.")
        elif opponent.__sex == "hembra":
            print("No peleo contra gatitas.")
        else:
            print(f"Ven aquí {opponent.__name}, que te vas a enterar :-@")
