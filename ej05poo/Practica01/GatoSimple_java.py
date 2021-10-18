"""
Implementación en Python de la clase del libro 'Aprende Java con Ejercicios'

Estilo Java
"""

class GatoSimple():


    def __init__(self, sexo):
        """constructor de la clase"""
        self.sexo = sexo
        self.color = ""
        self.raza = ""
        self.edad = 0
        self.peso = 0

    def get_sexo(self):
        """getter estilo Java"""
        return self.sexo

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
        if comida=="pescado":
            print("Hmmmm, gracias")
        else:
            print("Lo siento, yo solo como pescado")

    def pelea_con(self, contrincante):
        """
        Pone a pelear dos gatos.
        Solo se van a pelear dos machos entre sí.

        @param contrincante es el gato contra el que pelear
        """
        if self.sexo=="hembra":
            print("no me gusta pelear")
        else:
            if contrincante.get_sexo()=="hembra":
                print("no peleo contra gatitas")
            else:
                print("ven aquí que te vas a enterar")

# Prueba de la clase
if __name__=="__main__":
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
