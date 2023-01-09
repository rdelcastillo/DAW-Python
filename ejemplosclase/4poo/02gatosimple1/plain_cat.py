"""
Vamos a crear la clase 'Gato Simple', la llamamos así porque más adelante crearemos otra clase algo más elaborada que se
llamará 'Gato'.

Para saber qué atributos debe tener esta clase hay que preguntarse qué características tienen los gatos. Todos los gatos
son de un color determinado, pertenecen a una raza, tienen una edad, tienen un determinado sexo (machos o hembras) y
tienen un peso que se puede expresar en kilogramos. Estos serán los atributos que tendrá la clase "Gato Simple".

Para saber qué métodos debemos implementar hay que preguntarse qué acciones están asociadas a los gatos. Bien, pues los
gatos maúllan, ronronean, comen y, si son machos, se pelean entre ellos para disputarse el favor de las hembras. Esos
serán los métodos que definamos en la clase.

Aunque esta versión es funcional, tal como está implementada se pueden crear objetos inconsistentes, te invito a que
encuentres situaciones en las que pueda ocurrir esto.

Ejemplo sacado del libro "Aprende Java con Ejercicios" de Luis José Sánchez:
https://github.com/LuisJoseSanchez/aprende-java-con-ejercicios

Adaptado a Python por Rafael del Castillo Gomariz.

Fecha: 7/01/2023.
"""
import datetime


class PlainCat:

    def __init__(self, name, sex):
        """
        Constructor de 'Gato Simple', necesita un nombre y un sexo.
        """
        self.name = name
        self.sex = sex
        self.species = ''
        self.birth_day = datetime.date.today()

    def meow(self):
        """
        Hace que el gato maúlle.
        """
        print(f"({self.name}) Miauuuu!!!")

    def purr(self):
        """
        Hace que el gato ronronee.
        """
        print(f"({self.name}) Mrrrrrr!!!")

    def eat(self, food):
        """
        Hace que el gato coma. A los gatos les gusta el pescado, si le damos otra comida la rechazará.
        :param food: comida que se le ofrece al gato.
        """
        print(f"({self.name}) ", end="")
        if food == "pescado":
            print("Hmmmm, gracias :-)")
        else:
            print("Lo siento, yo solo como pescado.")

    def fight_with(self, opponent):
        """
        Pone a pelear dos gatos. Solo se van a pelear dos machos entre sí.
        :param opponent: gato contra el que pelear.
        """
        print(f"({self.name}) ", end="")
        if self.sex == "hembra":
            print("No me gusta pelear.")
        elif opponent.sex == "hembra":
            print("No peleo contra gatitas.")
        else:
            print(f"Ven aquí {opponent.name}, que te vas a enterar :-@")
