"""
Crea una biblioteca de funciones numéricas que contenga las siguientes funciones. Recuerda que puedes usar unas dentro
de otras si es necesario.

Observa bien lo que hace cada función, ya que, si las implementas en el orden adecuado, te puedes ahorrar mucho trabajo.
Por ejemplo, la función es_capicua() resulta trivial teniendo voltea() y la función siguiente_primo() también es muy
fácil de implementar teniendo es_primo().

Prohibido utilizar funciones de conversión del número a una cadena.

- es_capicua: devuelve verdadero si el número que se pasa como parámetro es capicúa y falso en caso contrario
- es_primo: devuelve verdadero si el número que se pasa como parámetro es primo y falso en caso contrario
- siguiente_primo: devuelve el menor primo que es mayor al número que se pasa como parámetro
- digitos: devuelve el número de dígitos de un número entero
- voltea: le da la vuelta a un número
- digito_n: devuelve el dígito que está en la posición n de un entero. Se empieza por 0 y de izquierda a derecha.
- posicion_de_digito: da la posición de la 1ª ocurrencia de un dígito dentro de un entero. Si no está, devuelve -1.
- quita_por_detras: le quita a un número n dígitos por detrás (por la derecha).
- quita_por_delante: le quita a un número n dígitos por delante (por la izquierda).
- pega_por_detras: añade un dígito a un número por detrás.
- pega_por_delante: añade un dígito a un número por delante.
- trozo_de_numero: toma como parámetros las posiciones inicial y final de un número y devuelve el trozo correspondiente.
- junta_numeros: pega dos números para formar uno.

En esta biblioteca se hace un test haciendo assert de las diferentes funciones. Además, las funciones lanzan la
excepción ValueError si se le pasan parámetros erróneos.

Autor: Rafael del Castillo Gomariz
Fecha: 8/12/2022
"""
import math

def es_primo(n):
    if n < 2:   # 1, 0 y los números negativos no son primos
        return False
    if n % 2 == 0 and n != 2:   # los pares, salvo el 2, no son primos
        return False
    for i in range(3, int(math.sqrt(n))+1, 2):
        if n % i == 0:
            return False
    return True # si llegamos aquí, el número es primo

def siguiente_primo(n):
    candidato_a_primo = n+1
    while not es_primo(candidato_a_primo):
        candidato_a_primo += 1
    return candidato_a_primo

def digitos(n):
    num = abs(n)
    total_digitos = 1   # cualquier número tiene al menos un dígito
    while num // 10 > 0:
        total_digitos += 1
        num //= 10
    return total_digitos

def quita_por_detras(num, cifras):
    lanza_excepcion_si_cifras_erroneas(num, cifras)
    return int(num / 10 ** cifras)  # con // hay problemas con los números negativos: -15215//100 = -153

def quita_por_delante(num, cifras):
    lanza_excepcion_si_cifras_erroneas(num, cifras)
    return signo(num) * (abs(num) % (10 ** (digitos(num) - cifras)))

def lanza_excepcion_si_cifras_erroneas(num, cifras):
    if cifras < 0 or cifras > digitos(num):
        raise ValueError(f"El número de dígitos a quitar ({cifras}) es erróneo para {num}")

def digito_n(num, pos_n):
    lanza_excepcion_si_posicion_erronea(num, pos_n)
    num_hasta_pos_n = quita_por_delante(num, pos_n)
    digito_en_pos_n = abs(quita_por_detras(num_hasta_pos_n, digitos(num_hasta_pos_n) - 1))
    return digito_en_pos_n

def lanza_excepcion_si_posicion_erronea(num, pos):
    if pos < 0:
        raise IndexError("La posición no puede ser negativa")
    if pos >= digitos(num):  # si la posición sobrepasa el número de dígitos posible lanzamos una excepción
        raise IndexError(f"No hay dígito en la posición {pos} de {num}")

def posicion_de_digito(num, cifra):
    lanza_excepcion_si_no_es_digito(cifra)
    total_digitos = digitos(num)
    for pos in range(total_digitos):  # podríamos haber usado digitos(), pero con la variable es más rápido
        if digito_n(num, pos) == cifra:
            return pos
    return -1  # si llegamos aquí es que cifra no está en n

def pega_por_detras(num, cifra):
    lanza_excepcion_si_no_es_digito(cifra)
    return num*10 + signo(num) * cifra

def pega_por_delante(num, cifra):
    lanza_excepcion_si_no_es_digito(cifra)
    num = signo(num) * cifra * 10 ** digitos(num) + num
    return num

def signo(num):
    if num == 0:
        return 1
    return abs(num)//num

def lanza_excepcion_si_no_es_digito(cifra):
    if cifra < 0 or cifra > 9:
        raise ValueError("El dígito no está entre 0 y 9")

def voltea(num):
    n_volteado = digito_n(num, 0) * signo(num)
    total_digitos = digitos(num)
    for pos in range(1, total_digitos):
        n_volteado = pega_por_delante(n_volteado, digito_n(num, pos))
    return n_volteado

def es_capicua(num):
    return num == voltea(num)

def junta_numeros(n1, n2):
    num = n1
    total_digitos_n2 = digitos(n2)
    for pos in range(total_digitos_n2):
        num = pega_por_detras(num, digito_n(n2, pos))
    return num

def trozo_de_numero(num, pos_inicio, pos_fin):
    n_sin_final = quita_por_detras(num, digitos(num) - pos_fin)
    return quita_por_delante(n_sin_final, pos_inicio)

if __name__ == "__main__":  # test de las funciones
    assert es_primo(2) == True
    assert es_primo(3) == True
    assert es_primo(4) == False
    assert es_primo(9) == False
    assert es_primo(19) == True
    assert es_primo(1) == False

    assert digitos(12345) == 5
    assert digitos(45) == 2
    assert digitos(-1) == 1
    assert digitos(-12345) == 5
    assert digitos(0) == 1
    assert digitos(1234) == 4

    assert siguiente_primo(2) == 3
    assert siguiente_primo(-5) == 2
    assert siguiente_primo(3) == 5
    assert siguiente_primo(4) == 5
    assert siguiente_primo(9) == 11
    assert siguiente_primo(19) == 23
    assert siguiente_primo(1) == 2

    assert digito_n(12345, 0) == 1
    assert digito_n(12345, 1) == 2
    assert digito_n(-12345, 2) == 3
    assert digito_n(12345, 3) == 4
    assert digito_n(12345, 4) == 5
    # assert digito_n(12345, 10) == 5  # esto debe lanzar una excepción

    assert posicion_de_digito(12345, 0) == -1
    assert posicion_de_digito(12345, 1) == 0
    assert posicion_de_digito(-12345, 2) == 1
    assert posicion_de_digito(12345, 3) == 2
    assert posicion_de_digito(12345, 4) == 3
    assert posicion_de_digito(12345, 5) == 4

    assert pega_por_detras(123, 9) == 1239
    assert pega_por_detras(123, 0) == 1230
    assert pega_por_detras(-123, 9) == -1239

    assert pega_por_delante(123, 9) == 9123
    assert pega_por_delante(123, 0) == 123
    assert pega_por_delante(-123, 9) == -9123

    assert voltea(1521) == 1251
    assert voltea(-1521) == -1251
    assert voltea(0) == 0
    assert voltea(8) == 8

    assert es_capicua(1521) == False
    assert es_capicua(-1521) == False
    assert es_capicua(1551) == True
    assert es_capicua(151) == True
    assert es_capicua(-151) == True
    assert es_capicua(5) == True

    assert junta_numeros(1521, 58) == 152158
    assert junta_numeros(-1521, 58) == -152158
    assert junta_numeros(0, 58) == 58
    assert junta_numeros(58, 0) == 580

    assert quita_por_detras(15215, 2) == 152
    assert quita_por_detras(-15215, 2) == -152
    assert quita_por_detras(15215, 4) == 1
    assert quita_por_detras(15215, 5) == 0
    assert quita_por_detras(15215, 0) == 15215

    assert quita_por_delante(15215, 2) == 215
    assert quita_por_delante(-15215, 2) == -215
    assert quita_por_delante(15215, 4) == 5
    assert quita_por_delante(15215, 5) == 0
    assert quita_por_delante(15215, 0) == 15215

    assert trozo_de_numero(15215, 1, 3) == 52
    assert trozo_de_numero(-15215, 1, 3) == -52
    assert trozo_de_numero(15215, 0, 3) == 152
    assert trozo_de_numero(15215, 2, 5) == 215
    assert trozo_de_numero(15215, 2, 3) == 2
    assert trozo_de_numero(15215, 3, 3) == 0