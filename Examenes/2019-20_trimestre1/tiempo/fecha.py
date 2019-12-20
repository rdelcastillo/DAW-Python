"""
Colección de funciones para manejar fechas en cadenas de caracteres.

El formato de la cadena es: AAAAMMDD.
Ejemplo: El 15 de diciembre de 2019 sería: "20191215"

Colección de funciones:

1. fecha_correcta: dice si la fecha que se pasa como parámetro es correcta.

2. fecha_mas_1dia: suma un día a la fecha que se pasa como parámetro y lo devuelve.

3. fecha_mas_ndias: suma una serie de días a la fecha que se pasa como parámetro y lo devuelve.

4. fecha_menos_1dia: resta un día a la fecha que se pasa como parámetro y lo devuelve.

5. fecha_menos_ndias: resta una serie de días a la fecha que se pasa como parámetro y lo devuelve.

6. es_bisiesto: dice si la fecha que se pasa como parámetro es bisiesto.

7. compara_fechas: recibe dos fechas y devuelve un valor negativo si la 1ª es anterior a la
   segunda, cero si son iguales, y un valor positivo si la 1ª es posterior a la segunda.

8. fecha_formateada: recibe un fecha y devuelve una cadena con el formato:
   DD de {MES} de AAAA     (Ejemplo: "15 de Diciembre de 2019")

9. año, mes, dia, nombre_mes: recibe un fecha y devuelve esos valores.

"""


def fecha_correcta(fecha_):
    """
    Dice si la fecha que se pasa como parámetro es correcta.

    @param fecha_
    @return verdadero o falso.
    """
    # tiene que tener longitud 8
    if len(fecha_) != 8:
        return False
    # todos sus caracteres tienen que ser dígitos
    # podemos usar el método isdigit(), pero por motivos didácticos no lo uso
    for i in range(len(fecha_)):
        c = fecha_[i]
        if c < '0' or c > '9':
            return False
    # El mes tiene que estar entre 1 y 12
    mes_ = mes(fecha_)
    if mes_ < 1 or mes_ > 12:
        return False
    # Si es año bisiesto el nº de días de febrero es 29.
    # Llamo a una función que me actualiza el nº de días de febrero si es bisiesto
    dias_mes_este_año = dias_mes_año(fecha_)
    dia_ = dia(fecha_)
    # esta expresión lógica la permite python, equivale a:
    #   dia_>0 and dia_<=dias_mes_este_año[mes_-1]
    return 0 < dia_ <= dias_mes_este_año[mes_ - 1]  # restamos 1 al mes para que esté entre 0 y 11


def fecha_mas_1dia(fecha_):
    """
    Suma un día a la fecha que se pasa como parámetro y la devuelve.

    @param fecha_
    @return nuevo fecha
    """
    dia_ = dia(fecha_)
    mes_ = mes(fecha_)
    año_ = año(fecha_)
    dias_mes_este_año = dias_mes_año(fecha_)

    # aumentamos el día
    ultimo_dia_mes = dias_mes_este_año[mes_ - 1]
    dia_ += 1
    if dia_ > ultimo_dia_mes:  # mes siguiente si no es 29/2 y bisiesto
        # mes siguiente
        dia_ = 1
        mes_ += 1
        if mes_ > 12:  # nos pasamos de diciembre, año siguiente
            mes_ = 1
            año_ += 1
    return fecha(dia_, mes_, año_)


def fecha_mas_n_dias(fecha_, dias_):
    """
    Suma una serie de días a la fecha que se pasa como parámetro y la devuelve.

    @param fecha_
    @param dias_
    @return nueva fecha
    """
    fecha2 = fecha_
    if dias_ >= 0:
        for i in range(dias_):
            fecha2 = fecha_mas_1dia(fecha2)
    else:
        for i in range(abs(dias_)):
            fecha2 = fecha_menos_1dia(fecha2)
    return fecha2


def fecha_menos_1dia(fecha_):
    """
    Resta un día a la fecha que se pasa como parámetro y la devuelve.

    @param fecha_
    @return nuevo fecha
    """
    dia_ = dia(fecha_)
    mes_ = mes(fecha_)
    año_ = año(fecha_)
    dias_mes_este_año = dias_mes_año(fecha_)
    # disminuimos el día
    dia_ -= 1
    if dia_ == 0:  # mes anterior y último día de mes
        mes_ -= 1
        if mes_ == 0:  # 31 de diciembre del año anterior
            mes_ = 12
            año_ -= 1
        dia_ = dias_mes_este_año[mes_ - 1]  # último día del mes anterior
    return fecha(dia_, mes_, año_)


def fecha_menos_n_dias(fecha_, dias_):
    """
    Resta una serie de días a la fecha que se pasa como parámetro y la devuelve.

    @param fecha_
    @param dias_
    @return nuevo fecha
    """
    fecha2 = fecha_
    if dias_ >= 0:
        for i in range(dias_):
            fecha2 = fecha_menos_1dia(fecha2)
    else:
        for i in range(abs(dias_)):
            fecha2 = fecha_mas_1dia(fecha2)
    return fecha2


def es_bisiesto(fecha_):
    """
    Dice si la fecha que se pasa como parámetro es de un año bisiesto.

    @param fecha_
    @return verdadero o falso
    """
    año_ = año(fecha_)
    return año_ % 4 == 0 and (año_ % 100 != 0 or año_ % 400 == 0)


def compara_fechas(fecha1, fecha2):
    """
    Recibe dos fechas y devuelve un valor negativo si la 1º es anterior a la 2º,
    cero si son iguales, y un valor positivo si la 1º es posterior a la segunda.

    @param fecha1
    @param fecha2
    @return entero negativo, cero o un entero positivo.
    """
    return int(fecha1) - int(fecha2)


def fecha_formateada(fecha_):
    """
    Recibe un fecha y devuelve una cadena con el formato DD de {MES} de AAAA
    (Ejemplo: "15 de Diciembre de 2019")

    @param fecha_
    @return fecha formateada
    """
    dia_ = dia(fecha_)
    año_ = año(fecha_)
    return str(dia_) + " de " + nombre_mes(fecha_) + " de " + str(año_)


def año(fecha_):
    """
    Devuelve el año de la fecha

    @param fecha_
    @return año
    """
    return int(fecha_[0:4])


def mes(fecha_):
    """
    Devuelve el mes de la

    @param fecha_
    @return mes
    """
    return int(fecha_[4:6])


def nombre_mes(fecha_):
    """
    Devuelve el nombre del mes de la fecha.

    @param fecha_
    @return nombre del mes
    """
    meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio", "Julio",
             "Agosto", "Septiembre", "Noviembre", "Diciembre"]
    mes_ = mes(fecha_)
    return meses[mes_ - 1]


def dia(fecha_):
    """
    Devuelve el día de la fecha

    @param fecha_
    @return día del mes
    """
    return int(fecha_[6:8])


def fecha(d, m, a):
    """
    Devuelve una cadena en formato AAAAMMDD

    @param d, m, a
    """
    dia_ = str(d).strip()
    mes_ = str(m).strip()
    año_ = str(a).strip()
    # día
    if len(dia_) < 2:
        dia_ = "0" + dia_
    # mes
    if len(mes_) < 2:
        mes_ = "0" + mes_
    # año
    for i in range(len(año_), 4):
        año_ = "0" + año_
    return año_ + mes_ + dia_

def dias_mes_año(fecha_):
    """
    Esta función se usará para simplificar otras funciones que requieren saber
    el número de días de cada mes y se complican al tener en cuenta el 29 de febrero
    de los años bisiestos.

    @param fecha_
    @return vector con los días de cada mes para el año de fecha_
    """
    dias_mes_este_año = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    if es_bisiesto(fecha_):
        dias_mes_este_año[1] += 1  # hay 29 días en febrero en este caso
    return dias_mes_este_año
