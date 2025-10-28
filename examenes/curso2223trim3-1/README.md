Vamos a crear la clase **CashRegister** que simula el comportamiento de una caja registradora como la que tiene cualquier comercio. Nuestra caja tendrá las siguientes operaciones:

- **Entrada y salida de efectivo**. Tenemos que registrar la cantidad que entra o sale, la fecha y hora de la operación y el concepto. Esta operación tiene un identificador numérico que se crea automáticamente y por defecto es el de la operación anterior incrementado en 1. No se puede añadir un movimiento con fecha y hora o identificador anterior al último. Si la fecha y hora no se indica se toma la actual.

- **Borrado del último movimiento**. El resto de movimientos no se pueden borrar porque descuadrarían los saldos de la caja.

- **Obtención de los movimientos de la caja**.

- **Guardar la caja en un archivo csv**.

Esta clase tiene que tener, al menos, los siguientes métodos:

- add()
  - recibe la cantidad (positiva o negativa), el concepto y la fecha y hora (**datetime**) y lo añade a la lista de movimientos.
  - lanza una **excepción personalizada** si la fecha y hora del movimiento es anterior al último.
  - lanza una **excepción personalizada** si el identificador del movimiento creado es anterior o igual al último almacenado.
  - lanza una **excepción personalizada** si el saldo que resulte después de aplicar este movimiento es negativo.
  - si la fecha y hora no se indican se toma la actual.
- delete\_last()
  - borra el último movimiento de la lista.
  - lanza **excepción personalizada** si no hay movimientos.
- save(filename)
  - guarda los movimientos de la caja en un fichero csv (*filename*), en caso de no indicar nombre de fichero este será:
    - cash\_register\_*\<fecha actual en formato aaaa-mm-dd>*.csv
- \_\_str\_\_()
  - devuelve una cadena con todos los movimientos y su saldo al final, si se imprime tiene que ser visualmente aceptable.
- balance()
  - devuelve el saldo de la caja.
  - debe ser una propiedad.

El **constructor** de esta clase puede recibir como parámetro el nombre de un **fichero csv** con los movimientos de la caja que deben estar ordenados tanto por fecha y hora como por el número de movimiento (un movimiento no puede tener una fecha anterior o código inferior o igual al movimiento anterior). En caso de que sea así se lanzará una **excepción personalizada**. También se lanzará si el código de alguno de los movimientos es **superior** al último asignado que está almacenado en un fichero (ver apartado siguiente).

En caso de no pasar nada al constructor se creará la **lista de movimientos vacía**.

Los movimientos de caja se guardarán en una lista y serán objetos de la clase **Movement**. Esta clase tendrá los siguientes atributos:

- number
  - identificador numérico del movimiento, será el último asignado incrementado en 1.
- date\_time
  - fecha y hora del movimiento
- amount
  - importe del movimiento, será positivo si es una entrada y negativo en caso contrario
- concept
  - concepto asignado al movimiento

El **constructor** de esta clase obtendrá el último movimiento asignado que se encontrará en el fichero <a name="__ddelink__190_2237127989"></a>**last\_number\_movement.txt**. Una vez construido el objeto se debe cambiar el contenido de este fichero para que tenga de nuevo el último asignado. En caso de no existir el archivo o no tener un valor entero se debe lanzar una **excepción personalizada**.

Los objetos de esta clase serán inmutables.

Por último hay que hacer un programa con un menú (usando la clase realizada en prácticas) para gestionar una caja registradora. Las opciones del menú serán:

1. Entrada de caja (con la fecha y hora actual).
1. Salida de caja (con la fecha y hora actual).
1. Borrado del último movimiento de la caja.
1. Impresión de la caja.
1. Guardar la caja. Si el fichero en el que se guarda existe hay que confirmar.
1. Cargar los movimientos desde un fichero CSV.
1. Salir.

P.D.- Ejemplo de fichero CSV:

<pre>
1,100,"Primer ingreso","8:00:00 26/04/2023"
2,-10,"Primer gasto","8:01:00 26/04/2023"
3,-20,"Segundo gasto","8:10:00 26/04/2023"
4,50,"Segundo ingreso","9:00:00 26/04/2023"
5,100,"Tercer ingreso","9:05:00 26/04/2023"
</pre>
Para crear un objeto datetime desde una cadena formateada como la del fichero csv podemos hacer algo como el ejemplo siguiente:

from datetime import datetime
<pre>
fecha = datetime.strptime('09:44:08 10/04/2023', '%H:%M:%S %d/%m/%Y')
</pre>
Obtenemos: datetime.datetime(2023, 4, 10, 9, 44, 8)



