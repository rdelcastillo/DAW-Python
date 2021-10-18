"""
Implementación en Python la clase del libro 'Aprende Java con Ejercicios'

A diferencia de GatoSimple_java.py aquí usaremos una filosofía más 'pythonica'
"""


class GatoSimple():

    def __init__(self, sexo):
        """constructor de la clase"""
        self.__sexo = sexo
        self.color = ""
        self.raza = ""
        self.edad = 0
        self.peso = 0

    @property
    def sexo(self):
        # En Python es aceptable acceder directamente a los miembros de la clase o del objeto.
        # Si no quisiéramos hacerlo podemos hacerlo así, el código siguiente hará que 'sexo' se similar a un atributo público.
        # Los métodos get_sexo()y set_sexo() tipo Java ya no son necesarios y no es una filosofía "pythonica".
        return self.__sexo

    @sexo.setter
    def sexo(self, s):
        self.__sexo = s

    def maulla(self):
        """Hace que el gato maulle"""
        print("Miauuuu")

    def ronronea(self):
        """Hace que el gato ronronee"""
        print("mrrrrrr")

    def come(self, comida):
        """
        Hace que el gato coma.
        A los gatos les gusta el pescado, si le damos otra comida
        la rechazará.

        @param comida la comida que se le ofrece al gato
        """
        if comida == "pescado":
            print("Hmmmm, gracias")
        else:
            print("Lo siento, yo solo como pescado")

    def pelea_con(self, contrincante):
        """
        Pone a pelear dos gatos.
        Solo se van a pelear dos machos entre sí.

        @param contrincante es el gato contra el que pelear
        """
        if self.__sexo == "hembra":
            print("no me gusta pelear")
        else:
            if contrincante.sexo == "hembra":
                print("no peleo contra gatitas")
            else:
                print("ven aquí que te vas a enterar")


# Prueba de la clase
if __name__ == "__main__":
    garfield = GatoSimple("macho")
    print("hola gatito")
    garfield.maulla()
    print("toma tarta")
    garfield.come("tarta selva negra")
    print("toma pescado, a ver si esto te gusta")
    garfield.come("pescado")

    tom = GatoSimple("macho")
    print("Tom, toma sopita de verduras")
    tom.come("sopa de verduras")

    lisa = GatoSimple("hembra")

    print("gatitos, a ver cómo maulláis")
    garfield.maulla()
    tom.maulla()
    lisa.maulla()

    garfield.pelea_con(lisa)
    lisa.pelea_con(tom)
    tom.pelea_con(garfield)
