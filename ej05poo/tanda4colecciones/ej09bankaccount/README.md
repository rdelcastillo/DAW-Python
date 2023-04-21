# Ampliación de la clase Cuenta Bancaria de la tanda 3

## Versión 1

Guardaremos los movimientos de la cuenta en una lista de cadenas de texto con la información de la transacción efectuada.

## Versión 2

Guardaremos los movimientos de la cuenta en una lista de diccionarios con información de cada movimiento:

* Tipo de movimiento (Ingreso, Cargo, Transferencia Recibida, Transferencia Emitida).
* Importe.
* En caso de las transferencias, la cuenta asociada.

El saldo ya no será un atributo, se calculará.

## Versión 3

Guardaremos los movimientos de la cuenta en una lista de objetos que representen movimientos bancarios.

## Versión 4

Mejora de la versión anterior, donde la clase para el movimiento es abstracta y se crean clases especializadas para los distintos tipos de movimiento. 