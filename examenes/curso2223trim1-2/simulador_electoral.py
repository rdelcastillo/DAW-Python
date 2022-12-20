"""
El Ministerio del Interior está preparando la infraestructura para las elecciones municipales de mayo de 2023 y ha
contactado con el IES Gran Capitán para que le hagamos un simulador de resultados electorales municipales, ya que
sospecha que alguno de sus sistemas ha podido ser atacado y no se acaba de fiar de la veracidad de los datos.

La ley electoral dice que para poder tener representación en un municipio hay que superar el 5% de los votos válidos y
el reparto de escaños se hace mediante la Ley D’Hont.

Con el propósito de testear mejor el programa se incluye una opción que carga los resultados electorales municipales de
Córdoba de 2019.

Autor: Rafael del Castillo Gomariz
Fecha: 18/12/2022
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
        elif option == 5:
            break
        elif not city:
            print("ERROR. No ha introducido los datos electorales.\n")
        elif option == 3:
            input_party_votes()
        else:
            print_simulation()
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
    global city, valid_votes, seats, votes_parties

    def want_delete_data():
        resp = input("Esto implica borrar los datos ya introducidos. Responda 'Sí' para proceder: ")
        return resp=="Sí"

    if city and not want_delete_data():
        return
    city = input("Municipio: ").upper()
    valid_votes = int(input("Votos válidos: "))
    seats = int(input("Número de ediles: "))
    votes_parties = []


def input_party_votes():
    name_party = input("Partido político: ")
    if exist_name_party(name_party):
        print("ERROR. Ese partido ya ha sido añadido.")
        return
    votes = int(input("Número de votos obtenido: "))
    if votes + total_votes_parties() > valid_votes:
        print("ERROR. Con ese número de votos se supera el total de votos emitidos.")
        return
    votes_parties.append([votes, name_party])


def exist_name_party(name_party):
    for p in votes_parties:
        if p[1] == name_party:
            return True
    return False


def total_votes_parties():
    total = 0
    for p in votes_parties:
        total += p[0]
    return total


def print_simulation():
    seats_parties = seats_with_dhont()
    print_seats(seats_parties)


def seats_with_dhont():

    def delete_votes_below_min():
        for p in remains_votes_seats_parties:
            if p[0] < MIN_PERCENT_VOTES * valid_votes:
                p[0] = 0

    # lista auxiliar con los restos, votos obtenidos, escaños y nombre del partido
    remains_votes_seats_parties = [[p[0], p[0], 0, p[1]] for p in votes_parties]
    delete_votes_below_min()

    for _ in range(seats):  # asignamos un escaño en cada iteración
        party_most_remaining_votes = max(remains_votes_seats_parties)
        # ajustamos restos de votos y le asignamos un escaño más
        party_most_remaining_votes[0] = party_most_remaining_votes[1] // (2 + party_most_remaining_votes[2])
        party_most_remaining_votes[2] += 1

    votes_parties.sort(reverse=True)
    return [[p[3], p[2], p[1]] for p in remains_votes_seats_parties]


def print_seats(seats_political_parties):
    print("REPARTO DE EDILES EN", city, "\n")
    print(f"{'PARTIDO':25} EDILES   VOTOS        %\n")
    for p in seats_political_parties:
        print(f"{p[0]:25}    {p[1]:3}  {p[2]:6,d}  {100*p[2]/valid_votes:5.2f} %")
    print(f"\nTOTAL EDILES: {seats}\tTOTAL VOTOS: {valid_votes:,d}")


if __name__ == "__main__":
    main()