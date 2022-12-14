"""
Define la función mezcla de forma que tome dos listas como parámetros y devuelve otra que es el resultado de mezclar los
números de ambos de forma alterna, se coge un número de a, luego de b, luego de a, etc. Los arrays a y b pueden tener
longitudes diferentes; por tanto, si se terminan los números de un array se terminan de coger todos los que quedan del
otro.

Ejemplos:

Si a = [8, 9, 0] y b = [1, 2, 3], mezcla(a, b) devuelve [8, 1, 9, 2, 0, 3]

Si a = [4, 3] y b = [7, 8, 9, 10], mezcla(a, b) devuelve [4, 7, 3, 8, 9, 10]

Si a = [8, 9, 0, 3] y b = [1], mezcla(a, b) devuelve [8, 1, 9, 0, 3]

Si a = [ ] y b = [1, 2, 3], mezcla(a, b) devuelve [1, 2, 3]
"""


def mezcla(l1, l2):
    lista_mezclada = []
    if len(l1) <= len(l2):
        lista_mas_corta, lista_mas_larga = l1, l2
    else:
        lista_mas_corta, lista_mas_larga = l2, l1

    # añadimos los números de forma alterna hasta que se acabe la lista más corta
    for i in range(len(lista_mas_corta)):
        lista_mezclada.append(l1[i])
        lista_mezclada.append(l2[i])

    # añadimos los números restantes de la lista más larga
    for i in range(len(lista_mas_corta), len(lista_mas_larga)):
        lista_mezclada.append(lista_mas_larga[i])

    return lista_mezclada


if __name__ == "__main__":
    assert mezcla([8, 9, 0], [1, 2, 3]) == [8, 1, 9, 2, 0, 3]
    assert mezcla([4, 3], [7, 8, 9, 10]) == [4, 7, 3, 8, 9, 10]
    assert mezcla([8, 9, 0, 3], [1]) == [8, 1, 9, 0, 3]
    assert mezcla([], [1, 2, 3]) == [1, 2, 3]