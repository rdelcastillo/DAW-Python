# Múltiples constructores en Python

A veces necesitamos escribir una clase de Python que proporcione múltiples formas de construir objetos y para ello desearíamos que nuestra clase implemente múltiples constructores, pero de manera nativa no lo podemos hacer en Python.

Este tipo de clase es útil cuando necesitamos crear instancias utilizando diferentes tipos o números de argumentos. En Python, hay varias técnicas y herramientas que podemos usar para simular de algún modo múltiples constructores a través de argumentos opcionales o la personalización de la creación de instancias a través de métodos de clase y el envío especial con decoradores. 

En los siguientes ejemplos veremos cómo: 

  * Usar parámetros opcionales y verificación de tipos para simular múltiples constructores.
  * Escribir múltiples constructores usando el decorador integrado @classmethod.
  * Sobrecargar los constructores de su clase usando el decorador @singledispatchmethod.

Fuente: [Real Python](https://realpython.com/python-multiple-constructors/)