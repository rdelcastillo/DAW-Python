<h1>Examen primer trimestre 2019</h1>
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
