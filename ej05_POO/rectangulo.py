class Rectangulo:
    """
    Versión 2.0.

    Esta clase representa objetos de tipo rectángulo.
    Acciones: cálculo del perímetro, área, dibujar, comparar.

    Mejoras respecto a la versión 1:

    - Protegemos (ocultamos) los atributos.
    - Creamos getters y setters para acceder a los mismos. Ojo, esta no
    es la filosofía de Python, esto es estilo Java.
    - Sobrecargamos el método __str__ para poder usar la función print y otras.

    Hay cosas que mejorar, en la siguiente se explica.
    """

    def __init__(self, base, altura):
        """
        Constructor de la clase.
        :param base: base del rectángulo.
        :param altura: altura del rectángulo.
        """
        self.__base = 1
        self.__altura = 1
        # Ojo, solo así en este ejemplo
        self.set_base(base)
        self.set_altura(altura)

    # getters y setters (ojo!!! estilo Java, no Python)

    def get_base(self):
        """
        Getter tipo Java
        :return: base
        """
        return self.__base

    def set_base(self, base):
        """
        Setter tipo Java.
        :param base:
        """
        if base>0:
            self.__base = base
        else:
            # Mucho mejor sería lanzar una excepción
            print("ERROR. Base incorrecta")

    def get_altura(self):
        """
        Getter tipo Java
        :return:
        """
        return self.__altura

    def set_altura(self, altura):
        """
        Setter tipo Java
        :param altura:
        :return: altura
        """
        if altura>0:
            self.__altura = altura
        else:
            # Mucho mejor sería lanzar una excepción
            print("ERROR. Altura incorrecta")

    # resto métodos

    def perimetro(self):
        """
        :return: perímetro del rectángulo.
        """
        return 2 * (self.__base + self.__altura)

    def area(self):
        """
        :return: área del rectángulo.
        """
        return self.__base * self.__altura

    def compara(self, otro):
        """
        Compara nuestro rectángulo con otro.
        :param otro: objeto con el que comparamos el actual.
        :return: >0 si mayor, 0 si igual, <0 si menor.
        """
        return self.area() - otro.area()

    def es_gemelo(self, otro):
        """
        Comprueba si el objeto pasado es el mismo rectángulo, o sea,
        tiene la misma base y altura.
        :param otro: objeto con el que comparamos el actual.
        :return: True o False
        """
        return self.__base == otro.get_base() and self.__altura == otro.get_altura()

    def muestra(self):
        """
        Muestra en pantalla el rectángulo.
        """
        print(self)

    # métodos sobrecargados

    def __str__(self):
        str = ""
        for i in range(self.__altura):
            str += "*" * self.__base
            str += "\n"
        str = str[:-1]
        return str



if __name__ == "__main__":
    r1 = Rectangulo(4, 1)
    r2 = Rectangulo(3, 2)
    print(f"Probamos clase rectángulo con r1: ({r1.get_base()},{r1.get_altura()}) y "
          f"r2: ({r2.get_base()},{r2.get_altura()})\n")
    # mostramos
    r1.muestra()
    print()
    r2.muestra()
    # comparamos
    print("Resultado de comparar r1 con r2:", r1.compara(r2))
    print("¿Son gemelos?", r1.es_gemelo(r2))
    # magnitudes
    print("Área r1:", r1.area(), "Perímetro r1:", r1.perimetro())
    print("Área r2:", r2.area(), "Perímetro r2:", r2.perimetro())
