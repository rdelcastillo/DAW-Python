"""
Ejemplo de uso de clases en Python
"""

class Test():
    """
    Ejemplo para ilustrar una clase en Python.

    Usaremos variables de clase y de instancia, métodos de instancia, de clase y estáticos
    """
    n_tests = 0                             # variables de clase (estática)
    __centro = ""

    def __init__(self, nombre, comentario):
        """Constructor de la clase"""
        self.__nombre = nombre              # variable de instancia (oculta)
        self.comentario = comentario        # variable de instancia
        self.__ciclo = ""                   # variable de instancia (oculta)
        Test.n_tests += 1                   # incrementamos el número de tests

    @property
    def nombre(self):
        """
        Similar getter de Java, pero con una filosofía 'pythonica'.
        En Python se prefiere acceder a los atributos directamente, si son ocultos se hace
        con una propiedad.
        """
        return self.__nombre

    @property
    def ciclo(self):
        """Similar getter de Java"""
        return self.__ciclo

    @ciclo.setter
    def ciclo(self,c):
        """
        Similar al setter de Java, pero con una filosofía 'pythonica'.
        Accedemos (desde fuera) a la propiedad del objeto como si fuera un atributo y le damos valor.
        """
        c = c.upper()
        if c in ["DAW","ASIR"]:
            self.__ciclo = c
        else:
            print(f"ERROR: {c} no es un ciclo válido")

    @classmethod
    def asigna_centro(cls, centro):
        """
        Método de clase.
        Observa que debe llevar también un primer parámetro obligatorio, la clase,
        por convención 'cls'.
        En este caso le asigna un valor a la variable de clase (y oculta) __centro
        """
        cls.__centro = centro

    @staticmethod
    def dame_animos():
        """
        Método estático. Igual que anteponer 'static' en Java.
        Las características principales de un método estático es que pueden ser llamados sin tener una instancia de la
        clase, además este tipo de métodos no tienen acceso al exterior, por lo cual no pueden acceder a ningún otro
        atributo o llamar a ninguna otra función dentro de la clase.
        """
        print("No se puede vencer a la persona que nunca se rinde 😎\n")

    def __str__(self):
        """Como toString() en Java"""
        estado = f"Nombre: {self.__nombre}\t {self.comentario}"
        if self.ciclo:
            estado += f"\t {self.ciclo}"    # usamos la propiedad
        if Test.__centro:
            estado += f"\t {Test.__centro}"
        return estado

    def __del__(self):
        """
        Destructor.
        A veces nos gustaría hacer algo cuando el objeto se destruye, con este método podemos hacerlo.
        En este caso ponemos un mensaje y decrementamos el número de tests.
        """
        print(f"--Test '{self.nombre}' que seas corregido con benevolencia--")
        Test.n_tests -= 1

# Prueba
if __name__ == "__main__":
    # Llamada a un método estático de la clase, no hace falta ninguna instancia
    Test.dame_animos()

    # Creamos dos objetos
    test1 = Test("Prueba de BDA","Formas normales")
    test2 = Test("Prueba de POO","Conceptos básicos")

    # Comprobamos cuántos hay
    print(f"Total tests: {Test.n_tests}\n")

    # Mostramos sus estados
    print(test1)
    print(test2,"\n")

    # Con un método de clase ponemos nombre al centro
    Test.asigna_centro("IES Gran Capitán")

    # Asignamos un ciclo a este test con un método de instancia
    test2.ciclo = "DAW"

    # Mostramos sus estados (que han cambiado)
    print(test1)
    print(test2,"\n")

    # Borramos un test
    print("Mandamos a corregir test2...\n")
    del test2

    # Comprobamos cuantos tests quedan
    print("\nQuedan",Test.n_tests,"tests\n")

    # Fin
    print("----------------")
    print("That's all folks")
    print("----------------\n")
