"""
Implementación de la clase Fracción.

Echar un vistazo a http://interactivepython.org/runestone/static/pythoned/Introduction/ProgramacionOrientadaAObjetosEnPythonDefinicionDeClases.html
"""

def mcd(m,n):
    """Devuelve el máximo común divisor de los dos números pasados como parámetro"""
    while m%n != 0:
        m_anterior = m
        n_anterior = n
        m = n_anterior
        n = m_anterior % n_anterior
    return n


class Fraccion():

    def __init__(self, n, d):
        # Comprobamos si hay errores al pasar los parámetros
        Fraccion.__verifica_numerador(n)
        Fraccion.__verifica_denominador(d)
        # Proceso
        self.__num = n
        self.__den = d

    @property
    def den(self):
        return self.__den

    @den.setter
    def den(self, d):
        Fraccion.__verifica_denominador(d)
        self.__den = d

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, n):
        Fraccion.__verifica_numerador(n)
        self.__num = n

    def __str__(self):
        return "%d/%d" %(self.num, self.den)

    def resultado(self):
        return self.num / self.den

    def simplifica(self):
        """Simplifica la fracción"""
        div = mcd(self.num, self.den)
        self.num //= div
        self.den //= div

    def incrementa(self, f):
        """Suma la fracción enviada como parámetro al objeto actual y la simplifica. Permite que se sumen números."""
        if isinstance(f, int):
            f = Fraccion(f,1)   # un entero n es igual a la fracción n/1
        else:
            Fraccion.__verifica_fraccion(f)
        # proceso
        self.num = self.num * f.den + self.den * f.num
        self.den = self.den * f.den
        self.simplifica()

    def decrementa(self, f):
        """Resta la fracción enviada como parámetro al objeto actual y la simplifica. Permite que se resten números."""
        if isinstance(f, int):
            f = Fraccion(f,1)   # un entero n es igual a la fracción n/1
        else:
            Fraccion.__verifica_fraccion(f)
        # proceso
        self.num = self.num * f.den - self.den * f.num
        self.den = self.den * f.den
        self.simplifica()

    def multiplica(self, f):
        """
        Comprueba si el parámetro enviado es un entero, en ese caso hace una multiplicación escalar,
        en caso contrario es una fracción y hace una multiplicación de fracciones.
        El resultado se guarda en el objeto actual y se hace una simplificación
        """
        if isinstance(f, int):
            f = Fraccion(f, 1)  # un entero n es igual a la fracción n/1
        else:
            Fraccion.__verifica_fraccion(f)
        # proceso
        self.num *= f.numerador
        self.den *= f.denominador
        self.simplifica()

    def divide(self, f):
        """
        Comprueba si el parámetro enviado es un entero, en ese caso hace una división escalar,
        en caso contrario es una fracción y hace una división de fracciones.
        El resultado se guarda en el objeto actual y se hace una simplificación
        """
        if isinstance(f, int):
            if f == 0:
                raise ZeroDivisionError("Intento de dividir por 0")
            self.den *= f
        else:
            Fraccion.__verifica_fraccion(f)
            self.num *= f.denominador
            self.den *= f.numerador
        self.simplifica()

    #
    # Sobrecarga de operadores. Ver https://riptutorial.com/es/python/example/7334/sobrecarga-del-operador
    #

    # Sobrecarga de operadores aritméticos. Ver http://elclubdelautodidacta.es/wp/2015/05/python-sumando-objetos/

    def __add__(self, other):
        """
        Sobrecarga del operador +.

        Permite que se sumen valores a una fracción con los formatos "<fracción> + <valor>" y "<valor> + <fracción>"
        Para el 1er formato usamos este método, para el 2º hay que usar "__radd__" que al ser la suma conmutativa basta
        con igualarlo.
        Ver: https://www.reddit.com/r/learnpython/comments/3cvgpi/can_someone_explain_radd_to_me_in_simple_terms_i/

        El parámetro 'other' se corresponde con el valor a sumar, que puede ser una fracción o un entero.

        Devuelve una nueva fracción.
        """
        if isinstance(other, int):
            other = Fraccion(other, 1)   # un entero n es igual a la fracción n/1
        else:
            Fraccion.__verifica_fraccion(other)
        # proceso
        n = self.num * other.den + self.den * other.num
        d = self.den * other.den
        resultado = Fraccion(n, d)
        resultado.simplifica()
        return resultado

    __radd__ = __add__

    def __sub__(self, other):
        """
        Sobrecarga del operador -.

        Permite que se resten elementos a una fracción con el formato "<fracción> - <elemento>".

        El parámetro 'other' se corresponde con el elemento a restar, que puede ser una fracción o un entero.

        Devuelve una nueva fracción.
        """
        if isinstance(other, int):
            other = Fraccion(other, 1)   # un entero n es igual a la fracción n/1
        else:
            Fraccion.__verifica_fraccion(other)
        # proceso
        n = self.num * other.den - self.den * other.num
        d = self.den * other.den
        resultado = Fraccion(n, d)
        resultado.simplifica()
        return resultado

    def __rsub__(self, other):
        """
        Sobrecarga del operador -.

        Permite que se resten fracciones a números con el formato "<número> - <fracción>".

        El parámetro 'other' se corresponde con el número a restar.

        Devuelve una nueva fracción.
        """
        if not isinstance(other, int):  # si no es entero lanzamos excepción
            raise TypeError("El minuendo debería ser entero", other)
        n = other * self.den - self.num
        d = self.den
        resultado = Fraccion(n, d)
        resultado.simplifica()
        return resultado

    def __mul__(self, other):
        """
        Sobrecarga del operador *.

        Permite que se multipliquen fracciones y el producto escalar (un entero por una fracción).
        La multiplicación escalar puede ser con los formatos "<fracción> * <valor>" y "<valor> * <fracción>"
        Para el 1er formato usamos este método, para el 2º hay que usar "__rmul__" que al ser el producto escalar
        conmutativo basta con igualarlo.

        El parámetro 'other' se corresponde con el valor a multiplicar, que puede ser una fracción o un entero.

        Devuelve una nueva fracción
        """
        if isinstance(other, int):
            other = Fraccion(other, 1)  # un entero n es igual a la fracción n/1
        else:
            Fraccion.__verifica_fraccion(other)
        # proceso
        n = self.num * other.num
        d = self.den * other.den
        resultado = Fraccion(n, d)
        resultado.simplifica()
        return resultado

    __rmul__ = __mul__

    def __truediv__(self, other):
        """
        Sobrecarga del operador /.

        Permite que se dividan fracciones y la división escalar.
        La división escalar puede ser con los formatos "<fracción> / <valor>" y "<valor> / <fracción>"
        Para el 1er formato usamos este método, para el 2º hay que usar "__rtruediv__"

        El parámetro 'other' se corresponde con el valor a multiplicar, que puede ser una fracción o un entero.

        Devuelve una nueva fracción
        """
        if isinstance(other, int):
            other = Fraccion(other, 1)  # un entero n es igual a la fracción n/1
        else:
            Fraccion.__verifica_fraccion(other)
        # proceso
        n = self.num * other.den
        d = self.den * other.num
        resultado = Fraccion(n, d)
        resultado.simplifica()
        return resultado

    def __rtruediv__(self, other):
        """
        Sobrecarga del operador /.

        Permite que se haga la división escalar (un entero entre una fracción) con el formato "<valor> / <fracción>"

        El parámetro 'other' se corresponde con el valor a multiplicar, que puede ser una fracción o un entero.

        Devuelve una nueva fracción
        """
        if not isinstance(other, int):  # si no es entero lanzamos excepción
            raise TypeError("El dividendo debería ser entero", other)
        resultado = Fraccion(other, 1) / self
        resultado.simplifica()
        return resultado

    # Sobrecarga de operadores relaciones. Ver http://elclubdelautodidacta.es/wp/tag/sobrecarga-de-operadores/
    #
    # No necesitamos sobrecargar los seis operadores, basta definir solo tres en este caso:
    # Dado que "a > b" también equivale, leído de derecha izquierda, a "b < a" se interpreta que si se incluye
    # una declaración específica del método __lt__, el <, “menor que”, es un __gt__ intercambiando los argumentos.
    # Se dice que los operadores > y < actúan “en espejo”. Lo mismo sucede con los pares >= y <=, así como con == y !=.
    # Pero si queremos usar enteros en uno y otro lado nos va a hacer falta sobrecargar __lt__ y __le__.
    #

    def __gt__(self, other):
        """Sobrecarga del operador >"""
        if isinstance(other, int):
            other = Fraccion(other, 1)   # un entero n es igual a la fracción n/1
        else:
            Fraccion.__verifica_fraccion(other)
        return (self.num * other.den) > (other.num * self.den)

    def __lt__(self, other):
        """Sobrecarga del operador <"""
        if isinstance(other, int):
            other = Fraccion(other, 1)   # un entero n es igual a la fracción n/1
        else:
            Fraccion.__verifica_fraccion(other)
        return (self.num * other.den) < (other.num * self.den)

    def __ge__(self, other):
        """Sobrecarga del operador >="""
        if isinstance(other, int):
            other = Fraccion(other, 1)   # un entero n es igual a la fracción n/1
        else:
            Fraccion.__verifica_fraccion(other)
        return (self.num * other.den) >= (other.num * self.den)

    def __le__(self, other):
        """Sobrecarga del operador <="""
        if isinstance(other, int):
            other = Fraccion(other, 1)   # un entero n es igual a la fracción n/1
        else:
            Fraccion.__verifica_fraccion(other)
        return (self.num * other.den) <= (other.num * self.den)

    def __eq__(self, other):
        """Sobrecarga del operador =="""
        if isinstance(other, int):
            other = Fraccion(other, 1)   # un entero n es igual a la fracción n/1
        else:
            Fraccion.__verifica_fraccion(other)
        return (self.num * other.den) == (other.num * self.den)

    # Comprobación de errores

    @staticmethod
    def __verifica_numerador(num):
        if not isinstance(num, int):  # numerador no entero
            raise TypeError("Numerador no entero", num)

    @staticmethod
    def __verifica_denominador(num):
        if not isinstance(num, int):  # denominador no entero
            raise TypeError("Denominador no entero", num)
        elif num == 0:
            raise ZeroDivisionError("Denominador 0")

    @staticmethod
    def __verifica_fraccion(f):
        if not isinstance(f, Fraccion):
            raise TypeError("El tipo de dato no es Fracción", f)


if __name__ == "__main__":

    x = Fraccion(1, 2)
    y = Fraccion(2, 3)

    print("Probamos operadores aritméticos:")

    print(x, "+", y, "=", x + y)
    print(x, "+ 1 =", x + 1)
    print("1 +", x, "=", 1 + x)
    print()

    print(x, "-", y, "=", x - y)
    print(x, "- 1 =", x - 1)
    print("1 -", x, "=", 1 - x)
    print()

    print(x, "*", y, "=", x * y)
    print(x, "/", y, "=", x / y)
    print()

    print("Probamos multiplicación y división escalar:")
    print(x, "* 2 =", x * 2)
    print("2 *", x, "=", 2 * x)
    print(x, "/ 2 =", x / 2)
    print("2 /", x, "=", 2 / x)
    print()

    print("Probamos operadores relacionales:")
    print(x, "==", y, "es", x == y)
    print(x, "!=", y, "es", x != y)
    print(x, "< ", y, "es", x < y)
    print(x, "<=", y, "es", x <= y)
    print(x, "> ", y, "es", x > y)
    print(x, ">=", y, "es", x >= y)
    print()

    print("1 ==", x, "es", 1 == x)
    print("1 !=", x, "es", 1 != x)
    print("1 < ", x, "es", 1 < x)
    print("1 <=", x, "es", 1 <= x)
    print("1 > ", x, "es", 1 > x)
    print("1 >=", x, "es", 1 >= x)
    print()
    print(y, "==", 1, "es", y == 1)
    print(y, "!=", 1, "es", y != 1)
    print(y, "< ", 1, "es", y < 1)
    print(y, "<=", 1, "es", y <= 1)
    print(y, "> ", 1, "es", y > 1)
    print(y, ">=", 1, "es", y >= 1)

