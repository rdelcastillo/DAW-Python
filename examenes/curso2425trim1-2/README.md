# Examen de Programación  
Fecha: 16/12/2024

Haz un programa que utilice una **matriz de 3x3** y ofrezca un menú con las siguientes opciones:

---

### 1. Rellenar la matriz con números aleatorios entre 1 y 100.

- Llama a la función `fill()` que recibe como parámetros 1 y 100:
```python
fill(1, 100)
```

---

### 2. Rellenar la matriz con números aleatorios entre 1 y 100 **sin que se repitan**.

- Puedes reutilizar la función anterior con un tercer parámetro (por defecto `True`) que indique si los números pueden repetirse:
```python
fill(1, 100, False)
```

---

### 3. Desplazar todos los números una posición hacia la **derecha**.

- Llama a la función `shift_right()` sin parámetros.

#### Ejemplo:

Antes | Después
---|---
1 2 3<br>4 5 6<br>7 8 9 | 3 1 2<br>6 4 5<br>9 7 8

---

### 4. Desplazar todos los números una posición hacia **abajo**.

- Llama a la función `shift_down()` sin parámetros.

#### Ejemplo:

Antes | Después
---|---
1 2 3<br>4 5 6<br>7 8 9 | 7 8 9<br>1 2 3<br>4 5 6

---

### 5. Calcular la **suma de los elementos de una fila**.

- Llama a la función `show_sum_row()` sin parámetros.
- Pide una fila y controla que esté entre 1 y 3. Si no es así, muestra un mensaje de error.
- Llama a `sum_row(fila)` y muestra el resultado.

---

### 6. Modificar un **elemento de la matriz**.

- Llama a la función `update_element()` sin parámetros.
- Pide fila y columna (entre 1 y 3). Si no es válido, muestra mensaje de error.
- Muestra el valor actual de esa posición y pregunta si quiere cambiarlo (respuestas válidas: "Sí" o "No").
- Si responde "Sí", realiza el cambio. En caso contrario, no hagas nada.

---

### 7. Mostrar la matriz.

- Llama a la función `show()` sin parámetros.
- Muestra la matriz **alineada correctamente**.

✅ Correcto:
```
 10 100  9
100  85 100
  7   4  26
```

❌ Incorrecto:
```
10 100 9
100 85 100
7 4 26
```

---

### 8. Salir del programa.

---

## Requisitos adicionales:

- La matriz debe ser una **variable global** llamada `matrix`, creada antes del menú y rellena de ceros.
- Cada opción del menú (excepto salir) debe llamarse mediante una **función**.
  - Si no usas funciones, se penaliza con **2 puntos**.
- Si la opción 1 o 2 no se han ejecutado, **las demás no deben funcionar**, salvo la opción de salir.
- Controla que la opción del menú ingresada sea válida.
- **No se pueden usar slices** para operar con la matriz. Ejemplos prohibidos:

```python
# No permitido:
matrix[0][:] = ...
matrix[1][1:] = ...
```