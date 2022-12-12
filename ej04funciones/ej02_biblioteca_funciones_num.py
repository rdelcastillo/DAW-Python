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

def digito_n(n, pos):
    lanza_excepcion_si_posicion_erronea(n, pos)
    num_hasta_pos = abs(n) // 10 ** (digitos(n)-pos-1)
    return num_hasta_pos % 10   # el último dígito está en pos

def lanza_excepcion_si_posicion_erronea(n, pos):
    if pos < 0:
        raise ValueError("La posición no puede ser negativa")
    if pos >= digitos(n):  # si la posición sobrepasa el número de dígitos posible lanzamos una excepción
        raise ValueError(f"No hay dígitos en la posición {pos} de {n}")

def posicion_de_digito(n, cifra):
    lanza_excepcion_si_digito_erroneo(cifra)
    total_digitos = digitos(n)
    for pos in range(total_digitos):  # podríamos haber usado digitos(), pero con la variable es más rápido
        if digito_n(n, pos) == cifra:
            return pos
    return -1  # si llegamos aquí es que cifra no está en n

def pega_por_detras(n, cifra):
    lanza_excepcion_si_digito_erroneo(cifra)
    return n*10 + signo(n) * cifra

def pega_por_delante(n, cifra):
    lanza_excepcion_si_digito_erroneo(cifra)
    num = signo(n) * cifra * 10 ** digitos(n) + n
    return num

def signo(n):
    if n == 0:
        return 1
    return abs(n)//n

def lanza_excepcion_si_digito_erroneo(cifra):
    if cifra < 0 or cifra > 9:
        raise ValueError("El dígito no está entre 0 y 9")

def voltea(n):
    n_volteado = digito_n(n, 0) * signo(n)
    total_digitos = digitos(n)
    for pos in range(1, total_digitos):
        n_volteado = pega_por_delante(n_volteado, digito_n(n, pos))
    return n_volteado

def es_capicua(n):
    return n == voltea(n)

def junta_numeros(n1, n2):
    num = n1
    total_digitos_n2 = digitos(n2)
    for pos in range(total_digitos_n2):
        num = pega_por_detras(num, digito_n(n2, pos))
    return num

def quita_por_detras(n, cifras):
    lanza_excepcion_si_cifras_erroneas(n, cifras)
    return int(n / 10 ** cifras)  # con // hay problemas con los números negativos: -15215//100 = -153

def quita_por_delante(n, cifras):
    lanza_excepcion_si_cifras_erroneas(n, cifras)
    return signo(n) * (abs(n) % (10 ** (digitos(n) - cifras)))

def lanza_excepcion_si_cifras_erroneas(n, cifras):
    if cifras < 0 or cifras > digitos(n):
        raise ValueError(f"El número de dígitos a quitar ({cifras}) es erróneo para {n}")

def trozo_de_numero(n, pos_inicio, pos_fin):
    n_sin_final = quita_por_detras(n, digitos(n) - pos_fin)
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