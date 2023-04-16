# Ejercicios de colecciones

## Ejercicio 1
Implementa el control de acceso al área restringida de un programa. Se debe pedir un nombre de usuario y una contraseña. Si el usuario introduce los datos correctamente, el programa dirá “Ha accedido al área restringida”. El usuario tendrá un máximo de 3 oportunidades. Si se agotan las oportunidades el programa dirá “Lo siento, no tiene acceso al área restringida”. Los nombres de usuario con sus correspondientes contraseñas deben estar almacenados en un diccionario.

## Ejercicio 2
Realiza un programa que escoja al azar 10 cartas de la baraja española (10 objetos de la clase *Carta*). Emplea una lista para almacenarlas y asegúrate de que no se repite ninguna. Las cartas se deben mostrar ordenadas. Primero se ordenarán por palo (bastos, copas, espadas, oros) y cuando coincida el palo, se ordenará por número: as, 2, 3, 4, 5, 6, 7, sota, caballo, rey.

## Ejercicio 3
Crea un mini-diccionario español-inglés que contenga, al menos, 20 palabras (con su correspondiente traducción). Utiliza un diccionario para almacenar las parejas de palabras. El programa pedirá una palabra en español y dará la correspondiente traducción en inglés.

## Ejercicio 4
Realiza un programa que escoja al azar 5 palabras en español del mini-diccionario del ejercicio anterior. El programa irá pidiendo que el usuario teclee la traducción al inglés de cada una de las palabras y comprobará si son correctas. Al final, el programa deberá mostrar cuántas respuestas son válidas y cuántas erróneas.

## Ejercicio 5
Escribe un programa que genere una secuencia de 5 cartas de la baraja española y que sume los puntos según el juego de la brisca. El valor de las cartas se debe guardar en un diccionario que debe contener parejas (figura, valor), por ejemplo (“caballo”, 3). La secuencia de cartas debe ser una lista que contiene objetos de la clase *Carta*. El valor de las cartas es el siguiente: as → 11, tres → 10, sota → 2, caballo → 3, rey → 4; el resto de cartas no vale nada.

## Ejercicio 6
Realiza un programa que sepa decir la capital de un país (en caso de conocer la respuesta) y que, además, sea capaz de aprender nuevas capitales. En principio, el programa solo conoce las capitales de España, Portugal y Francia. Estos datos deberán estar almacenados en un diccionario. Los datos sobre capitales que vaya aprendiendo el programa se deben almacenar en el mismo diccionario. El usuario sale del programa escribiendo la palabra “salir”.

Ejemplo:
<pre>
Escribe el nombre de un país y te diré su capital: España
La capital de España es Madrid
Escribe el nombre de un país y te diré su capital: Alemania
No conozco la respuesta ¿cuál es la capital de Alemania?: Berlín
Gracias por enseñarme nuevas capitales
Escribe el nombre de un país y te diré su capital: Portugal
La capital de Portugal es Lisboa
Escribe el nombre de un país y te diré su capital: Alemania
La capital de Alemania es Berlín
Escribe el nombre de un país y te diré su capital: Francia
La capital de Francia es París
Escribe el nombre de un país y te diré su capital: salir
</pre>

## Ejercicio 7
Una empresa de venta por internet de productos electrónicos nos ha encargado implementar un carrito de la compra. Crea la clase Carrito. Al carrito se le pueden ir agregando elementos que se guardarán en una lista, por tanto, deberás crear la clase Elemento. Cada elemento del carrito deberá contener el nombre del producto, su precio y la cantidad (número de unidades de dicho producto). A continuación se muestra tanto el contenido del programa principal como la salida que debe mostrar el programa. Los métodos a implementar se pueden deducir del programa principal.

Contenido del programa principal:

<pre>
mi_carrito = Carrito()
mi_carrito.agrega(Elemento("Tarjeta SD 64Gb", 19.95, 2))
mi_carrito.agrega(Elemento("Canon EOS 2000D", 449, 1))
print(mi_carrito)
print(f"Hay {mi_carrito.numero_elementos()} productos en la cesta.")
print(f"El total asciende a {mi_carrito.importe_total():.2f} euros")
print("\nContinúa la compra...\n")
mi_carrito.agrega(Elemento("Samsung Galaxy Tab", 199, 3))
mi_carrito.agrega(Elemento("Tarjeta SD 64Gb", 19.95, 1))
print(mi_carrito);
print(f"Ahora hay {mi_carrito.numero_elementos()} productos en la cesta.")
print(f"El total asciende a {mi_carrito.importe_total():.2f} euros")
</pre>

Salida:
<pre>
Contenido del carrito
=====================
Tarjeta SD 64Gb PVP: 19,95 Unidades: 2 Subtotal: 39,90
Canon EOS 2000D PVP: 449,00 Unidades: 1 Subtotal: 449,00
Hay 2 productos en la cesta.
El total asciende a 488,90 euros

Continúa la compra...

Contenido del carrito
=====================
Tarjeta SD 64Gb PVP: 19,95 Unidades: 2 Subtotal: 39,90
Canon EOS 2000D PVP: 449,00 Unidades: 1 Subtotal: 449,00
Samsung Galaxy Tab PVP: 199,00 Unidades: 3 Subtotal: 597,00
Tarjeta SD 64Gb PVP: 19,95 Unidades: 1 Subtotal: 19,95
Ahora hay 4 productos en la cesta.
El total asciende a 1105,85 euros
</pre>
## Ejercicio 8
Mejora el programa anterior (en otro diferente) de tal forma que al intentar agregar un elemento al carrito, se compruebe si ya existe el producto y, en tal caso, se incremente el número de unidades sin añadir un nuevo elemento. Observa que en el programa anterior, se repetía el producto “Tarjeta SD 64Gb” dos veces en el carrito. En esta nueva versión ya no sucede esto, sino que se incrementa el número de unidades del producto que se agrega. El contenido del programa principal es idéntico al ejercicio anterior.

Salida:
<pre>
Contenido del carrito
=====================
Tarjeta SD 64Gb PVP: 19,95 Unidades: 2 Subtotal: 39,90
Canon EOS 2000D PVP: 449,00 Unidades: 1 Subtotal: 449,00
Hay 2 productos en la cesta.
El total asciende a 488,90 euros

Continúa la compra...

Contenido del carrito
=====================
Tarjeta SD 64Gb PVP: 19,95 Unidades: 3 Subtotal: 59,85
Canon EOS 2000D PVP: 449,00 Unidades: 1 Subtotal: 449,00
Samsung Galaxy Tab PVP: 199,00 Unidades: 3 Subtotal: 597,00
Ahora hay 3 productos en la cesta.
El total asciende a 1105,85 euros
</pre>
## Ejercicio 9
Amplía el ejercicio de la tanda anterior que implementaba cuentas corrientes de un banco de tal forma que cada cuenta lleve un registro de todos los movimientos realizados: ingresos, cargos y transferencias (tanto enviadas como recibidas).

Contenido del programa principal:
<pre>
cuenta1 = CuentaCorriente()
cuenta2 = CuentaCorriente(1500)
cuenta3 = CuentaCorriente(6000)
cuenta1.ingreso(2000)
cuenta1.cargo(600)
cuenta3.ingreso(75)
cuenta1.cargo(55)
cuenta2.transferencia(cuenta1, 100)
cuenta1.transferencia(cuenta3, 250)
cuenta3.transferencia(cuenta1, 22)
print(cuenta1.movimientos())
</pre>
Salida:
<pre>
Movimientos de la cuenta 1654432813
-----------------------------------
Ingreso de 2000 € Saldo: 2000,00 €
Cargo de 600 € Saldo: 1400,00 €
Cargo de 55 € Saldo: 1345,00 €
Transferencia recibida de 100 € de la cuenta 1654432813 Saldo 1445,00 €
Transferencia emitida de 250 € a la cuenta 6546817008 Saldo 1195,00 €
Transferencia recibida de 22 € de la cuenta 1654432813 Saldo 1217,00 €
</pre>