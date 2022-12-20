"""
El Ministerio del Interior está preparando la infraestructura para las elecciones municipales de mayo de 2023 y ha
contactado con el IES Gran Capitán para que le hagamos un simulador de resultados electorales municipales, ya que
sospecha que alguno de sus sistemas ha podido ser atacado y no se acaba de fiar de la veracidad de los datos.

La ley electoral dice que para poder tener representación en un municipio hay que superar el 5% de los votos válidos y
el reparto de escaños se hace mediante la Ley D’Hont.

Con el propósito de testear mejor el programa se incluye una opción que carga los resultados electorales municipales de
Córdoba de 2019.
"""
from utilities import menu

MIN_PERCENT_VOTES = 0.05

city = None
valid_votes = 0
seats = 0
votes_parties = []

def main():
    while True:
        option = menu("Simulador electoral municipal", "Cargar datos de las elecciones municipales de Córdoba de 2019",
                      "Introducir datos electorales", "Introducir partido y votos", "Ver simulación", "Finalizar")

        if option == 1:
            load_electoral_data_cordova()
        elif option == 2:
            input_electoral_data()
        elif option == 3:
            input_party_votes()
        elif option == 4:
            print_simulation()
        else:
            break
        print()

    print("¡Hasta la próxima! ;-)")


def load_electoral_data_cordova():
    global city, valid_votes, seats, votes_parties
    city = "CÓRDOBA"
    valid_votes = 146548
    seats = 29
    votes_parties = [[43434, "PP"], [36169, "PSOE"], [22094, "Ciudadanos"], [15656, "IU ANDALUCÍA"],
                     [11788, "VOX"], [9144, "PODEMOS"], [1653, "PACMA"], [951, "ACCIÓN POR CÓRDOBA"],
                     [380, "PCTE"], [360, "ANDALUCÍA ENTRE TOD@S"], [320, "GANEMOS"], [320, "EB"],
                     [161, "PUM+J"]]
    print("Datos de Córdoba cargados.")


def input_electoral_data():
    pass


def input_party_votes():
    pass


def print_simulation():
    pass


if __name__ == "__main__":
    main()