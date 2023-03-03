# Clase Mobile

## Versión 1

Esta versión crea la clase *Mobile* de la manera más intuitiva para quienes tienen poca experiencia en programación orientada a objetos. Tiene un problema, le da más de una responsabilidad a esta clase:

  * La gestión de llamadas del móvil.
  * La gestión de las tarifas.

Incumple el primero de los [principios de SOLID](https://gustavopeiretti.com/principios-solid-con-ejemplos/), el de "responsabilidad única".

## Versión 2

Esta versión delega la responsabilidad de las tarifas a la clase Rates donde estas se guardan en un diccionario.

## Versión 3

Esta versión usa las tarifas como objetos, posiblemente la opción más adecuada desde el punto de vista de la programación orientada a objetos, pero quizás requiera un poco de experiencia para que se nos ocurra de forma espontánea.