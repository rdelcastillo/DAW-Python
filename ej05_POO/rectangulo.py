import pickle
import sys

class DimensionRectanguloError(Exception):
    """
    Excepción que se produce cuando no se respetan las dimensiones permitidas de un rectángulo.
    """
    def __init__(self, mensaje):
        super.__init__(self)
        self.mensaje_error = mensaje


class Rectangulo:
    """
    Versión 5.0.

    Esta clase representa objetos de tipo rectángulo.
    Acciones: cálculo del perímetro, área, dibujar, comparar.

    Mejoras respecto a la versión 4.0:

    - Sustituimos los assert por excepciones:
        * cuando se le asigne al rectángulo un valor que no sea entero en el lado o en el ancho tiene que lanzar la excepción "TypeError".
        * crea una excepción propia para cuando el rectángulo sobrepasa las dimensiones permitidas: "DimensionRectanguloError".
    - Tiene un método (guardar) para guardar en un fichero el objeto actual usando pickle.
    - Tiene un método (recuperar) para recuperar un objeto Rectángulo almacenado en un fichero usando pickle.
    """
    lado_maximo = 10  # lado máximo del rectángulo
    __num_creados = 0  # contador de rectángulos creados

    def __init__(self, base, altura):
        """
        Constructor de la clase.
        :param base: base del rectángulo.
        :param altura: altura del rectángulo.
        """
        self.__base = 1
        self.__altura = 1
        Rectangulo.__num_creados += 1
        # por si hubiera errores en los parámetros hemos dado valor inicial
        self.base = base
        self.altura = altura

    def __del__(self):
        Rectangulo.__num_creados -= 1

    # propiedades

    @property
    def base(self):
        return self.__base

    @base.setter
    def base(self, value):
        Rectangulo.__comprueba_lado(value)
        self.__base = value

    @property
    def altura(self):
        return self.__altura

    @altura.setter
    def altura(self, value):
        Rectangulo.__comprueba_lado(value)
        self.__altura = value

    # resto métodos

    @staticmethod
    def num_creados():
        return Rectangulo.__num_creados

    @staticmethod
    def es_lado_correcto(value):
        return isinstance(value, int) and 0 < value <= Rectangulo.lado_maximo

    @staticmethod
    def __comprueba_lado(value):
        """
        Comprueba el valor recibido, si no es entero lanza la excepción TypeError y si no está dentro de los límites
        lanza la excepción DimensionRectanguloError.

        :param value: base o una altura del rectángulo.
        """
        if not isinstance(value, int):
            raise TypeError
        elif value < 0 or value > Rectangulo.lado_maximo:
            raise DimensionRectanguloError(f"{value} no está dentro de las dimensiones permitidas.")

    def perimetro(self):
        """
        :return: perímetro del rectángulo.
        """
        return 2 * (self.base + self.altura)

    def area(self):
        """
        :return: área del rectángulo.
        """
        return self.base * self.altura

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
        return self.base == otro.base and self.altura == otro.altura

    def muestra(self):
        """
        Muestra en pantalla el rectángulo.
        """
        print(self)

    def guarda(self, fichero):
        """
        Guarda el objeto actual en el fichero enviado como parámetro.
        :param fichero: nombre del fichero que hay que guardar.
        :return: true si se ha podido hacer y false si no se ha podido hacer.
        """
        try:
            f = open(fichero, "wb")
            pickle.dump(self, f)
            f.close()
            return True
        except:
            print("No se ha podido crear el fichero.", fichero, file=sys.stderr)
            return False

    def recupera(self, fichero):
        """
        Recupera un objeto rectángulo guardado en un fichero con el método 'guarda' en el objeto actual.
        :param fichero: nombre del fichero donde se guardó el objeto.
        :return: true si se ha podido hacer y false si no se ha podido hacer.
        """
        try:
            # recuperamos objeto del fichero
            f = open(fichero, "rb")
            r = pickle.load(f)    # objeto Rectángulo auxiliar
            f.close()
            # asignamos el estado al objeto actual
            self.base = r.base
            self.altura = r.altura
            return True
        except:
            print("No se ha podido recuperar el objeto.", fichero, file=sys.stderr)
            return False

    # métodos sobrecargados

    def __str__(self):
        str = ""
        for i in range(self.altura):
            str += "*" * self.base
            str += "\n"
        str = str[:-1]
        return str

    def __mul__(self, other):
        """
        Multiplica la base por el parámetro si no se pasa del lado máximo, en ese caso lo hace con la altura.
        :param other: Valor entero positivo
        :return: Otro rectángulo con la superficie original*other.
        """
        if not isinstance(other, int):  # no es entero el operando, error
            raise TypeError
        if other == 0:                  # es cero, error, no hay rectángulos de superficie 0
            raise DimensionRectanguloError("No puede haber rectángulos de superficie 0")
        if self.base * other > Rectangulo.lado_maximo and self.altura * other > Rectangulo.lado_maximo:
            raise DimensionRectanguloError(f"Multiplicar por {other} sobrepasa las dimensiones.")
        # proceso
        if self.base * other <= Rectangulo.lado_maximo:
            return Rectangulo(self.base * other, self.altura)
        else:
            return Rectangulo(self.base, self.altura * other)

    def __rmul__(self, other):
        return self * other

    def __lt__(self, other):
        if not isinstance(other, Rectangulo):
            raise TypeError
        return self.area() < other.area()

    def __le__(self, other):
        if not isinstance(other, Rectangulo):
            raise TypeError
        return self.area() <= other.area()

    def __eq__(self, other):
        if not isinstance(other, Rectangulo):
            raise TypeError
        return self.area() == other.area()


if __name__ == "__main__":
    r1 = Rectangulo(4, 1)
    r2 = Rectangulo(3, 2)
    print(f"Probamos clase rectángulo con r1: ({r1.base},{r1.altura}) y "
          f"r2: ({r2.base},{r2.altura})\n")
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
    # accedemos a variables de instancia de clase
    print("Rectángulos creados", Rectangulo.num_creados())
