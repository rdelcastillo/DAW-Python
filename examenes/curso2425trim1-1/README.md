**EJERCICIO 1**

Desarrolla un programa en Python que simule el juego clásico "Piedra, papel o tijera" contra el ordenador.

**Requerimientos:**

1. **Selección del Jugador:**
   * Al iniciar el juego, el usuario debe ingresar su elección: piedra, papel o tijera. Asegúrate de que el usuario introduzca una opción válida.

1. **Selección del Ordenador:**
   * El programa debe generar aleatoriamente la elección del ordenador entre piedra, papel y tijera.

1. **Reglas del Juego:**
   * Piedra gana a tijera.
   * Tijera gana a papel.
   * Papel gana a piedra.

1. **Contador:**
   * Implementa un contador para llevar la cuenta de las rondas jugadas.

1. **Interruptor:**
   * Usa una variable booleana que actúe como un interruptor para terminar el juego después de que el usuario decida no continuar. El juego debe preguntar al usuario si desea jugar otra ronda al final de cada partida. Asegúrate de que el usuario introduzca una opción válida.

1. **Sentencias Condicionales y Ciclos:**
   * Utiliza un bucle while que se mantenga activo mientras el usuario quiera seguir jugando.
   * Dentro del bucle, emplea sentencias if, elif y else para determinar el ganador de cada ronda y mostrar el resultado.

1. **Resultados:**
   * Después de cada ronda, muestra el resultado de quién ganó y cuál fue la elección de cada uno.
   * Al finalizar el juego, muestra el total de rondas jugadas y cuántas rondas ganó el usuario, perdió o fueron empate.

**Ejemplo de Interacción:**

~~~
¿Piedra, papel o tijera? papel
El ordenador eligió: piedra
¡Ganaste! Papel envuelve piedra.

¿Quieres jugar otra vez? (sí/no): sí

¿Piedra, papel o tijera? tijera
El ordenador eligió: tijera
Es un empate.

¿Quieres jugar otra vez? (sí/no): no

Fin del juego. Has jugado 2 rondas: 1 ganadas, 0 perdidas, 1 empate.
~~~

**EJERCICIO 2**

Desarrolla un programa en Python que simule un juego de dados contra el ordenador, donde se acumulen puntos basados en el resultado de los lanzamientos.

**Requerimientos:**

1. **Lanzamiento de Dados:**
   * El usuario y el ordenador lanzan un dado (simulado por números aleatorios del 1 al 6). El usuario decide cuándo lanzar el dado presionando Intro, y el resultado del ordenador se genera automáticamente.

1. **Puntuación:**
   * Si el número en el dado del jugador es mayor que el del ordenador, el jugador gana la ronda y se acumulan puntos igual al número en su dado.
   * Si el número en el dado del ordenador es mayor, el ordenador gana la ronda y se acumulan puntos igual al número en su dado.
   * Si ambos números son iguales, se considera un empate y no se acumulan puntos.

1. **Acumuladores:**
   * Implementa un acumulador para sumar los puntos del jugador y otro para sumar los puntos del ordenador a lo largo del juego.

1. **Interruptor:**
   * Usa una variable booleana que actúe como un interruptor para terminar el juego después de que el usuario decida no continuar. El juego debe preguntar al usuario si desea lanzar nuevamente al final de cada ronda. Asegúrate de que el usuario introduzca una opción válida.

1. **Sentencias Condicionales y Ciclos:**
   * Utiliza un bucle while que se mantenga activo mientras el usuario quiera seguir jugando.
   * Emplea sentencias if, elif y else para determinar el ganador de cada ronda y actualizar el acumulador de puntos según corresponda.

1. **Resultados:**
   * Después de cada ronda, muestra el resultado de quién ganó y cuál fue el resultado de los dados.
   * Al finalizar el juego, muestra el total de puntos acumulados por el jugador y por el ordenador indicando quién ha ganado.

**Ejemplo de Interacción:**
~~~
Presiona Intro para lanzar tu dado: [Usuario presiona Intro]
Tu dado: 4
Dado del ordenador: 3
¡Ganaste la ronda!
Puntos acumulados por ti: 4
Puntos acumulados por el ordenador: 0

¿Quieres lanzar de nuevo? (sí/no): sí

Presiona Intro para lanzar tu dado: [Usuario presiona Intro]
Tu dado: 2
Dado del ordenador: 5
El ordenador gana la ronda.
Puntos acumulados por ti: 4
Puntos acumulados por el ordenador: 5

Presiona Intro para lanzar tu dado: [Usuario presiona Intro]

Tu dado: 6

Dado del ordenador: 6

¡EMPATE!

Puntos acumulados por ti: 4

Puntos acumulados por el ordenador: 5

¿Quieres lanzar de nuevo? (sí/no): no

Fin del juego.

Gana el ordenador 5 a 4.
~~~