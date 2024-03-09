Examen de Programación 1ºDAW-A. 8/3/2024.

1. (2 PUNTOS): Crea una clase que modele un dado (*Dice*) de manera que:

-   El constructor recibe los valores de las caras que tiene el dado.
    Ejemplo:

    -   *dice1 = Dice(1, 2, 3, 4, 5, 6)*
    -   dice2 = Dice('A', 'K', 'Q', 'J', 'R', 'N')

-   Los valores de las caras los obtendremos mediante una propiedad
    (*sides*).

-   Dispondremos de un método para tirar el dado (*roll*) que devolverá
    el resultado (uno de los valores anteriores), además actualizará una
    variable de instancia privada (*side*) que podrá consultarse
    mediante una propiedad.

-   Los métodos mágicos *\_\_str\_\_()* y *\_\_repr\_\_()* deben estar
    creados.

-   Puedo usar los operadores *==* y *!=* para comparar dos dados.

2. (1 PUNTO) Crea una clase que modele un dado de póker (*PokerDice*) que derive de la clase anterior de manera que:

-   Los posibles valores del dado son 'A', 'K', 'Q', 'J', 'R' y 'N'.
-   El dado tiene una propiedad (*score*) que nos da la puntuación del
    dado (6, 5, 4, 3, 2, 1).

3. (1 PUNTO) Crea una clase que modele un dado de parchís (*LudoDice*)
que derive de la clase del apartado 1. Un dado de parchís tiene seis
caras que van del 1 al 6 (valores enteros). En esta clase:

-   Tendremos la posibilidad de comparar dados entre sí con los
    operadores relaciones *\<*, *\<=*, *\>* y *\>=*.

4. (3 PUNTOS) Crea una clase que modele un dado de parchís trucado
(*TrickedLudoDice*) que derive de la clase anterior y que de cuando en
cuando nos permita poner el valor que queramos en la cara del dado
(entre 1 y 6), de manera que:

-   No puedo usar el método que pone el valor que queramos en la cara
    del dado (*put*) si no he tirado al menos tres veces de forma
    normal, si lo llamo sin haberse cumplido esta excepción lanzaremos
    una excepción.
-   Ten en cuenta que NO PUEDES cambiar directamente el valor de la cara
    de un dado ya que se almacena en una variable de instancia privada
    de una clase de la que heredas (*Dice*) y no tienes acceso.

5. (2 PUNTOS) Crea una clase que modele un cubilete de dados
(*DiceCup*) de manera que:

-   Al construirla le paso una serie de dados. Ejemplo:

    -   cup = DiceCup(LudoDace(), LudoDace(), LudoDace())

-   Dispondremos de una propiedad que devuelva los dados (*dices*) y
    otra que devuelva el número de dados que contiene (*size*).

-   Dispondremos de un método para añadir un dado (*add*).

-   Dispondremos de un método para quitar un dado (*remove*) pasándole
    el dado concreto que queremos quitar.

-   Debe estar creado el método mágico* \_\_str\_\_()*.

6. (1 PUNTO) Crea una clase que modele un cubilete de dados de póker
(*PokerDiceCup*) que derive de la clase anterior de manera que tenga una
propiedad (*score*) que devuelva la puntuación total del cubilete (la
suma de la de cada dado).

Hay que controlar los tipos de datos de los parámetros de los métodos. Usa los test proporcionados.