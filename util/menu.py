"""
Clase para gestionar menús de texto.

Autor: Rafael del Castillo Gomariz
"""
class Menu:

    def __init__(self, *options, title="Menú de opciones"):
        self.__options = list(options)
        self.__title = title

    @property
    def last_option(self):
        return len(self.__options)

    def choose(self):
        self.__print_menu()
        return self.__chosen_option()

    def __print_menu(self):
        print(self.__title)
        print("-" * len(self.__title))
        for n in range(len(self.__options)):
            print(f"{n + 1}. {self.__options[n]}")

    def __chosen_option(self):
        while True:
            opc = Menu.__input_option()
            if 1 <= opc <= len(self.__options):
                return opc
            print("Ha introducido una opción incorrecta.")

    @staticmethod
    def __input_option():
        while True:
            try:
                option = int(input("\nIntroduzca una opción: "))
                return option
            except ValueError:
                print("Debe introducir un valor entero. Vuelva a intentarlo")
            except KeyboardInterrupt:
                print("Ha pulsado Ctrl-C. Acabe con la opción de terminar")
