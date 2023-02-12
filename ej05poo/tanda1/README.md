# Ejercicios tanda 1

1. Crea una clase "Dado" (`Dice`) que simule el funcionamiento de un dado con caras del 1 al 6 que tienen la misma probabilidad de salir y un programa de prueba.

2. Implementa una clase "Punto" (`Point`) con sus atributos x e y. La clase debe contener: su constructor, los getters y setters (propiedades), un `invert_coordinates()` que invierta las coordenadas x e y del punto. Además la clase debe tener un `__str__()` para poder imprimir los puntos en formato “(x,y)”. Implementa un test donde crees un punto, lo imprimas utilizando de manera implícita el método `__str__()`, imprimas su coordenada x, asignes 0 a su coordenada x, y vuelvas a imprimir el punto.

3. Implementa una clase "Rectángulo" (`Rectangle`) determinada por dos objetos `Point`, que además de su constructor, tendrá dos métodos para calcular su área y su perímetro que tienes que transformar en propiedades. Implementa también un test que cree dos puntos y un rectángulo a partir de estos dos puntos y que muestre el área y perímetro de dicho rectángulo.

4. Implementar otra clase "Dado". Por defecto el dado tendrá 6 caras. Tendremos tres formar de construir un dado (uno al que no se le pasa nada e inicializa el dado al azar, otro al que sólo se le pasa que número tiene el dado en la cara superior y otro con el número del dado en la cara superior y el número de caras del dado). Implementa los getters, el método roll() que tirará el dado al azar y el `__str__(). Implementa un tester que tenga un vector de 4 dados y los lance una serie de veces.