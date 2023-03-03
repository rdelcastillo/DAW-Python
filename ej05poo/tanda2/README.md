# Ejercicios tanda 2

**5.** Crea una clase que represente una estructura de datos tipo [pila](https://es.wikipedia.org/wiki/Pila_\(informática\)) (stack) y otra tipo [cola](https://es.wikipedia.org/wiki/Cola_\(informática\)) (queue).

La pila y la cola permitirán estas operaciones:

- Crear la pila o la cola con o sin valores iniciales o a partir de otra cola o pila.
- Obtener el número de elementos almacenados (tamaño).
- Saber si la pila o la cola está vacía.
- Vaciar completamente la pila o la cola.
- Para el caso de la pila:
  - Apilar (push): se añade un elemento a la pila. Se añade al principio de esta.
  - Desapilar (pop): se saca (debe devolverse) un elemento de la pila y se elimina. 
  - Leer el elemento superior de la pila sin retirarlo (top).
- Para el caso de la cola:
  - Encolar (enqueue): se añade un elemento a la cola. Se añade al final de esta.
  - Desencolar (dequeue): se saca (debe devolverse) y se elimina el elemento frontal de la cola, es decir, el primer elemento que entró.
  - Leer el elemento frontal de la cola, es decir, el primer elemento que entró, sin retirarlo (front).

**6.** Crea una clase para almacenar duraciones de tiempo (Duration). Los objetos de esta clase son intervalos de tiempo y se crean de la forma:

t1 = Duration(1, 20, 30)  # almacenará 1 hora, 20 minutos y 30 segundos.

t2 = Duration(2, 75, -10)  # almacenará 3 horas, 14 minutos y 50 segundos.

t3 = Duration(t2)  # almacenará las horas, minutos y segundos del objeto t2

Crea los getters y setters mediante propiedades y métodos para:

- Sumar y restar objetos de la clase (el resultado es otro objeto).
- Sumar y restar segundos, minutos o horas (se cambia el objeto actual).
- Devolver una cadena con el tiempo almacenado, de forma que si lo que hay es (10 35 5) la cadena sea 10h 35m 5s.

**7.** Crea una clase "Fraction" inmutable (no hay setters, solo getters para numerador y denominador) de forma que podamos hacer las siguientes operaciones:

- Construir un objeto Fracción pasándole al constructor el numerador y el denominador. La fracción se construye simplificada, no se puede dividir por cero.
- Obtener resultado de la fracción (número real).
- Multiplicar la fracción por un número (el método devuelve otra fracción, simplificada).
- Multiplicar, dividir, sumar y restar fracciones (los métodos devuelven otra fracción, simplificada).

**8.** Muestra un menú con las siguientes opciones:

1. Introducir (por teclado) una fecha pidiendo por teclado año, mes y día en formato dd/mm/aaaa. Si no se introduce correctamente se devuelve un mensaje de error. Usa una función booleana para validar la fecha.
1. Añadir días a la fecha. Pide un número de días para sumar a la fecha introducida previamente y actualiza su valor. Si el número es negativo restará los días. Esta opción sólo podrá realizarse si hay una fecha introducida (se ha ejecutado la opción anterior), si no la hay mostrará un mensaje de error. 
1. Añadir meses a la fecha. El mismo procedimiento que la opción anterior.
1. Añadir años a la fecha. El mismo procedimiento que la opción 2.
1. Comparar la fecha introducida con otra. Pide una fecha al usuario en formato dd/mm/aaaa (válida, si no lo es da error) y la comparará con la que tenemos guardada, posteriormente mostrará si esta fecha es anterior, igual o posterior a la que tenemos almacenada y el número de días comprendido entre las dos fechas.
1. Mostrar la fecha en formato largo (ejemplo: "lunes, 1 de febrero de 2021").
1. Terminar.

Consideraciones a tener en cuenta:

- El menú lo hacemos con una clase a la que llamaremos Menú, esa clase permitirá ir añadiendo opciones y escoger alguna opción.
- Las fechas las manejaremos con la clase [datetime.date](https://docs.python.org/3/library/datetime.html#date-objects).

**9.** Nos hemos enterado que la clase *datetime.date* ha sido comprometida y tenemos que crear una clase nueva para almacenar fechas locales (Date), en este caso la clase será mutable (los objetos pueden cambiar el día, mes o año). Los objetos de la clase Fecha son fechas de tiempo y se crean de la forma:

f1 = Date(1, 10, 2020)  # almacena el 1 de Octubre de 2020

f2 = Date(f1)  # almacena una copia de la fecha almacenada en f1

Para simplificar consideraremos que las fechas son todas a partir del 1 de enero del año 1.

Si al constructor se le pasan valores incorrectos lanzaremos la excepción *ValueError*.

Crea métodos para:

- Sumar y restar días a la fecha. 
- Restar fechas. Devuelve el número de días comprendidos entre ambas.
- Comparar la fecha almacenada con otra.
- Saber si el año de la fecha almacenada es bisiesto.
- Obtener el día de la semana de una fecha concreta.
- El método \_\_str\_\_() devuelve una cadena con el formato "<día del mes> de <nombre del mes> de <año>".

