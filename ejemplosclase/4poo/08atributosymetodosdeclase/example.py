"""
Ejemplo de uso de atributos de clase, métodos de clase y estáticos.

Autor: Rafael del Castillo.
"""

class Example:
    class_attribute = "ATRIBUTO (público) de CLASE"

    def __init__(self, value):
        self.__id = value
        self.instance_attribute = f"Soy un ATRIBUTO (público) de INSTANCIA. Mi identificador es {value}"

    def instance_method(self):
        print(f"Soy un método de instancia ({self.__id}), accedo a los atributos de mi clase", self.class_attribute)

    @classmethod
    def class_method(cls):
        print("Soy un método de de clase, accedo a mis atributos de clase pero no de la instancia", cls.class_attribute)

    @staticmethod
    def static_method():
        print("Soy un método estático, no tengo acceso a los atributos de mi clase ni de la instancia")

if __name__ == "__main__":
    Example.static_method()         # para acceder a los métodos estáticos no necesito una instancia
    Example.class_method()          # para acceder a los métodos de clase no necesito una instancia
    print(Example.class_attribute)  # para acceder a un atributo de clase no necesito una instancia

    obj = Example(1)
    obj.instance_method()           # puedo acceder a los métodos de instancia (públicos) de obj
    obj.class_method()              # puedo acceder a los métodos de clase de mi clase
    obj.static_method()             # puedo acceder a los métodos estáticos de mi clase
    print(obj.class_attribute)      # puedo acceder a los atributos de clase de mi clase
