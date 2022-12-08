## Ejercicios

**Ejercicio 1**

- Haz un programa que pida dos valores (a y b) y a continuación muestre un menú con cinco opciones: sumar, restar, multiplicar, dividir y terminar. Cada opción llama a una función a la que se le pasan las dos variables y muestra el resultado de la operación. Si se introduce una opción incorrecta se muestra un mensaje de error. El menú se volverá a mostrar, a menos que no se de a la opción terminar.
- Modifica el programa anterior para que la introducción de las variables sea una opción del menú (la primera). Las variables se inicializan a cero.
- Modifica el programa anterior para que si no se introducen las dos variables desde la opción correspondiente no se puedan ejecutar el resto de las opciones.
- Crea una función para gestionar menús: recibe una lista de opciones, las muestra numeradas, pide una opción (por su número) y devuelve la opción escogida. Modifica el último programa para que use esta función. 

**Ejercicio 2**

Crea una biblioteca de funciones numéricas que contenga las siguientes funciones. Recuerda que puedes usar unas dentro de otras si es necesario.

Observa bien lo que hace cada función ya que, si las implementas en el orden adecuado, te puedes ahorrar mucho trabajo. Por ejemplo, la función es\_capicua() resulta trivial teniendo voltea() y la función siguiente\_primo() también es muy fácil de implementar teniendo es\_primo().

Prohibido usar funciones de conversión del número a una cadena.

- es\_capicua: devuelve verdadero si el número que se pasa como parámetro es capicúa y falso en caso contrario.
- es\_primo: devuelve verdadero si el número que se pasa como parámetro es primo y falso en caso contrario.
- siguiente\_primo: devuelve el menor primo que es mayor al número que se pasa como parámetro.
- digitos: devuelve el número de dígitos de un número entero.
- voltea: le da la vuelta a un número.
- digito\_n: devuelve el dígito que está en la posición n de un número entero. Se empieza contando por el 0 y de izquierda a derecha.
- posicion\_de\_digito: da la posición de la primera ocurrencia de un dígito dentro de un número entero. Si no se encuentra, devuelve -1.
- quita\_por\_detras: le quita a un número n dígitos por detrás (por la derecha).
- quita\_por\_delante: le quita a un número n dígitos por delante (por la izquierda).
- pega\_por\_detras: añade un dígito a un número por detrás.
- pega\_por\_delante: añade un dígito a un número por delante.
- trozo\_de\_numero: toma como parámetros las posiciones inicial y final dentro de un número y devuelve el trozo correspondiente.
- junta\_numeros: pega dos números para formar uno.

Haz el programa de manera que al ejecutarse pruebe cada una de las funciones.

**Ejercicio 3**

Crea una biblioteca de funciones (statistics) dentro de un paquete (util) que contenga las siguientes funciones:

- maximum
  - recibiendo como parámetro un array de enteros
  - recibiendo un conjunto de parámetros enteros
- minimum
  - recibiendo como parámetro un array de enteros 
  - recibiendo un conjunto de parámetros enteros
- mean
  - recibiendo como parámetro un array de enteros 
  - recibiendo un conjunto de parámetros enteros
- variance
  - recibiendo como parámetro un array de enteros y haciendo uso de la función anterior
  - recibiendo un conjunto de parámetros enteros y haciendo uso de la función anterior
- median
  - recibiendo como parámetro un array de enteros 
  - recibiendo un conjunto de parámetros enteros
- mode
  - recibiendo como parámetro un array de enteros 
  - recibiendo un conjunto de parámetros enteros
  - devuelve un array de enteros (puede haber varias modas)

**Ejercicio 4**

Haz un programa que muestre un menú y, usando las funciones anteriores, ejecute las siguientes opciones:

- Muestra los números primos que hay entre 1 y 1000.
- Muestra los números capicúa que hay entre 1 y 99999.
- Muestra la moda de 50 números enteros aleatorios entre 1 y 10.
- Muestra la mediana de 10 números enteros aleatorios entre 1 y 50.
- Muestra el máximo y mínimo de 1000 números enteros aleatorios entre 1 y 50000.
- Muestra la varianza de 10 números enteros aleatorios entre 1 y 5.

**Ejercicio 5**

Crea una función que reciba un número, lo convierta al sistema de palotes y lo devuelva en una cadena de caracteres. 

Por ejemplo, el 470213 en decimal es el | | | | - | | | | | | | - - | | - | - | | | en el sistema de palotes. 

Utiliza esta función en un programa para comprobar que funciona bien. Desde la función no se debe mostrar nada por pantalla, solo se debe usar print desde el programa principal.

**Ejercicio 6**

Crea una función que reciba un número, lo convierta al sistema Morse y lo devuelve en una cadena de caracteres. 

Por ejemplo, el 213 es el . . _ _ _ . _ _ _ _ . . . _ _ en Morse. Utiliza esta función en un programa para comprobar que funciona bien.

Desde la función no se debe mostrar nada por pantalla, solo se debe usar print desde el programa principal.

Los números en Morse los puedes encontrar [aquí](https://morsecw.com/alfabeto.html#numeros).

**Ejercicio 7**

Define la función mezcla de forma que tome dos listas como parámetros y devuelve otra que es el resultado de mezclar los números de ambos de forma alterna, se coge un número de a, luego de b, luego de a, etc. Los arrays a y b pueden tener longitudes diferentes; por tanto, si se terminan los números de un array se terminan de coger todos los que quedan del otro.

Ejemplos

Si a = [8, 9, 0] y b = [1, 2, 3], mezcla(a, b) devuelve [8, 1, 9, 2, 0, 3 ]

Si a = [4, 3] y b = [7, 8, 9, 10], mezcla(a, b) devuelve [4, 7, 3, 8, 9, 10]

Si a = [8, 9, 0, 3] y b = [1], mezcla(a, b) devuelve [8, 1, 9, 0, 3]

Si a = [ ] y b = [1, 2, 3], mezcla(a, b) devuelve [1, 2, 3]


