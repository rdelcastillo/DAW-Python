"""
Ejemplo de herencia en POO. Clases DadoSimple, DadoTrucado, DadoPoker, DadoPokerTrucado que heredarán de Dado.

Autor: Rafael del Castillo.
"""
from dado import Dado


class DadoSimple(Dado):
    """
    Simulará un dado normal con las caras del 1 al 6.
    """

    def __init__(self):
        super().__init__(1, 2, 3, 4, 5, 6)


class DadoSimpleTrucado(Dado):
    """
    Simulará un dado trucado en el que el 5 y el 6 tienen el doble de posibilidades de salir.
    """

    def __init__(self):
        super().__init__(1, 2, 3, 4, 5, 5, 6, 6)  # añadimos un 5 y un 6 más a los valores posibles del dado.

    @property
    def caras(self):
        """
        Propiedad caras redefinida de la clase Dado para que salgan seis caras, si no la redefinimos saldrán
        ocho caras en vez de seis.
        """
        return [1, 2, 3, 4, 5, 6]


class DadoPoker(Dado):
    """
    Simulará un dado de póquer
    """

    def __init__(self):
        super().__init__("Negro", "Rojo", "J", "Q", "K", "As")


class DadoPokerTrucado(Dado):
    """
    Simulará un dado de póquer trucado en el que el As tiene el doble de probabilidad de salir, a menos que se
    indique con un parámetro que tiene más probabilidad.
    """
    __valores_caras = "Negro", "Rojo", "J", "Q", "K", "As"  # variable de clase oculta

    def __init__(self, p=2):
        """
        Constructor de la clase.
        :param p: factor de probabilidad de salir el As (2=doble, 3=triple, etc...), por defecto 2.
        """
        valores = list(DadoPokerTrucado.__valores_caras)
        valores.extend(["As"] * (p-1))  # añadimos más ases a los valores posibles
        super().__init__(*valores)  # desempaquetamos la lista valores para que cada elemento sea un parámetro

    @property
    def caras(self):
        """
        Propiedad caras redefinida de la clase Dado para que salgan seis caras, si no la redefinimos saldrá
        un número mayor de caras.
        """
        return DadoPokerTrucado.__valores_caras


if __name__ == "__main__":
    # Probamos dado simple
    d = DadoSimple()
    print("Tiramos dado simple 1000 veces con estos resultados:")
    tiradas = [d.tirada() for i in range(1000)]
    for i in d.caras:
        print(f"{i} ha salido {tiradas.count(i)} veces")

    # Probamos dado simple trucado
    d = DadoSimpleTrucado()
    print("\nTiramos dado simple trucado 1000 veces con estos resultados:")
    tiradas = [d.tirada() for i in range(1000)]
    for i in d.caras:
        print(f"{i} ha salido {tiradas.count(i)} veces")

    # Probamos dado póquer
    d = DadoPoker()
    print("\nTiramos dado de póquer 1000 veces con estos resultados:")
    tiradas = [d.tirada() for i in range(1000)]
    for i in d.caras:
        print(f"{i} ha salido {tiradas.count(i)} veces")

    # Probamos dado póquer trucado con doble probabilidad para el As
    d = DadoPokerTrucado()
    print("\nTiramos dado de póquer trucado con doble As 1000 veces con estos resultados:")
    tiradas = [d.tirada() for i in range(1000)]
    for i in d.caras:
        print(f"{i} ha salido {tiradas.count(i)} veces")

    # Probamos dado póquer trucado con triple probabilidad para el As
    d = DadoPokerTrucado(3)
    print("\nTiramos dado de póquer trucado con doble As 1000 veces con estos resultados:")
    tiradas = [d.tirada() for i in range(1000)]
    for i in d.caras:
        print(f"{i} ha salido {tiradas.count(i)} veces")
