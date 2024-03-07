# Ejercicios Tanda 3

**10.** Crea la clase abstracta *Vehicle*, así como las clases *Bike* y *Car* como subclases de la primera. Para la clase *Vehicle*, crea los atributos de clase *vehicles_created* y *total_kilometers*, así como el atributo de instancia *kilometers_traveled*.

En la clase *Vehicle* crea un método para viajar (*travel*) que incremente los kilómetros recorridos. 

En la clase *Bike* haz un método para hacer el caballito y en la clase *Car* otro para quemar rueda.

En la clase *Car*:

- Tendremos una variable de instancia con los litros de combustible que quedan en el depósito, inicialmente cero.
- Tendremos un método para quemar rueda y otro para llenar el depósito.
- Cuando el coche viaje disminuirá el número de litros en el depósito en relación a los kilómetros viajados. Si no hay combustible suficiente, el coche recorrerá únicamente los kilómetros que pueda.
- Para simplificar, cada kilómetro recorrido consumirá 0,1 litros de combustible, en un depósito caben 50 litros y quemar rueda consume 1 litro de combustible.

Prueba las clases creadas mediante un programa con un menú (usando la clase de la tanda anterior) como el que se muestra a continuación:

<pre>
VEHÍCULOS
=========
1. Anda con la bicicleta
2. Haz el caballito con la bicicleta
3. Anda con el coche
4. Quema rueda con el coche
5. Llena el depósito del coche
6. Ver kilometraje de la bicicleta
7. Ver kilometraje del coche
8. Ver el combustible que queda en el depósito del coche
9. Ver kilometraje total
10. Salir

Elige una opción (1-8):
</pre>

**11.** Implementa la clase *Terminal*. Un terminal tiene asociado un número de teléfono. Los terminales se pueden llamar unos a otros y el tiempo de conversación corre para ambos. A continuación se proporciona el contenido del programa principal que usa esta clase y el resultado que debe aparecer por pantalla. Los números de teléfono tienen que validarse como tales al crear el objeto (solo dígitos, empiezan por 9, 6 ó 7, su longitud es de nueve dígitos) y no puede haber dos terminales con el mismo número.

Programa principal:

<pre>
t1 = Terminal("678112233")
t2 = Terminal("644744469")
t3 = Terminal("622328909")
t4 = Terminal("664739818")
print(t1)
print(t2)
t1.call(t2, 320)
t1.call(t3, 200)
print(t1)
print(t2)
print(t3)
print(t4)
</pre>

Salida:

<pre>
No 678 11 22 33 - 0s de conversación
No 644 74 44 69 - 0s de conversación
No 678 11 22 33 - 520s de conversación
No 644 74 44 69 - 320s de conversación
No 622 32 89 09 - 200s de conversación
No 664 73 98 18 - 0s de conversación
</pre>

**12.** Implementa la clase *Mobile* como subclase de *Terminal* (la clase del ejercicio anterior que ya no hace falta modificar). Cada móvil lleva asociada una tarifa que puede ser “rata”, “mono” o “bisonte” (debes controlar esto). El coste por minuto es de 6, 12 y 30 céntimos respectivamente. Se tarifican los segundos exactos. La tarifa se puede cambiar. Obviamente, cuando un móvil llama a otro, se le cobra al que llama, no al que recibe la llamada. A continuación se proporciona el contenido del programa principal que usa esta clase y el resultado que debe aparecer por pantalla. El total tarificado debe aparecer con dos decimales.

Programa principal:

<pre>
m1 = Mobile("678112233", "rata")
m2 = Mobile("644744469", "mono")
m3 = Mobile("622328909", "bisonte")
print(m1)
print(m2)
m1.call(m2, 320)
m1.call(m3, 200)
m2.call(m3, 550)
print(m1)
print(m2)
print(m3)
</pre>

Salida:

<pre>
Nº 678 11 22 33 - 0s de conversación - tarificados 0,00 euros
Nº 644 74 44 69 - 0s de conversación - tarificados 0,00 euros
Nº 678 11 22 33 - 520s de conversación - tarificados 0,52 euros
Nº 644 74 44 69 - 870s de conversación - tarificados 1,10 euros
Nº 622 32 89 09 - 750s de conversación - tarificados 0,00 euros
</pre>

**13.** Implementa la clase *BankAccount*. Cada cuenta corriente tiene un número de cuenta de 10 dígitos. El número de cuenta se genera de forma aleatoria cuando se crea una cuenta nueva y no puede haber dos objetos con el mismo número de cuenta. La cuenta se puede crear con un saldo inicial; en caso de no especificar saldo, se pondrá a cero inicialmente. En una cuenta se pueden hacer ingresos y gastos. También es posible hacer una transferencia entre una cuenta y otra. No se permite el saldo negativo. En el siguiente capítulo se propone un ejercicio como mejora de éste, en el que se pide llevar un registro de los movimientos realizados.

Prueba la clase con este programa principal:

<pre>
cuenta1 = BankAccount()
cuenta2 = BankAccount(1500)
cuenta3 = BankAccount(6000)
print(cuenta1)
print(cuenta2)
print(cuenta3)
cuenta1.deposit(2000)
cuenta2.withdraw(600)
cuenta3.deposit(75)
cuenta1.withdraw(55)
cuenta2.transfer(cuenta3, 100)
print(cuenta1)
print(cuenta2)
print(cuenta3)
</pre>

La salida debe ser:

<pre>
Número de cta: 6942541557 Saldo: 0,00 €
Número de cta: 9319536518 Saldo: 1500,00 €
Número de cta: 7396941518 Saldo: 6000,00 €
Número de cta: 6942541557 Saldo: 1945,00 €
Número de cta: 9319536518 Saldo: 800,00 €
Número de cta: 7396941518 Saldo: 6175,00 €
</pre>

**14.** Crea en Python las siguientes clases:

- *Card* que simule una carta de naipes. Un naipe tiene un palo (de un conjunto de palos) y un valor (de un conjunto de valores).
- *CardPlayer* que simule un jugador de naipes. Un jugador tiene un nombre y un conjunto de naipes. Puede robar una carta de una baraja. Una vez robada el jugador tiene una carta más y la baraja una menos. Puede deshacerse de una carta. Puede recibir cartas.
- *Deck* que simula un conjunto de cartas de naipes. Inicialmente tiene las cartas que le llegan con el constructor. Puede repartir un conjunto de cartas a un jugador. En la baraja dejan de existir esas cartas. Le pueden quitar la primera carta (robar). Puede barajarse.
- Baraja Española e Inglesa (*SpanishDeck* e *EnglishDeck*) que heredan de *Deck*.