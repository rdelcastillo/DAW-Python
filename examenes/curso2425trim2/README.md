# ⚔️ Examen de Programación: Objetos, Clases y Batallas en Python

**Duración sugerida:** 90 minutos  
**Temática:** ¡Prepárate para el combate! Vas a modelar guerreros, sus armas y sus habilidades para luchar en un sistema de combate orientado a objetos.

---

## Parte 1: Clase `Arma` (2 puntos)

Crea una clase `Arma` con los siguientes atributos:

- `nombre` (`str`)
- `daño_base` (`int`)
- `durabilidad` (`int`)

### Requisitos:

- Constructor con validación:
  - `nombre` no puede estar vacío.
  - `daño_base` y `durabilidad` deben ser mayores a 0.
- Los atributos deben ser del tipo de datos indicado.
- Los atributos son **privados** y se accede a ellos mediante **propiedades**.
- `daño_base` será 0 si la `durabilidad` es 0.
- Método `usar()` que disminuye la durabilidad en 1 cada vez que se use.
  - Si la durabilidad llega a 0, el arma ya no hace daño.
- Implementar el método mágico `__str__()`.

### Ejemplo:

```python
espada = Arma("Espada de Fuego", 25, 3)
espada.usar()
print(espada)  # Arma: Espada de Fuego, daño_base: 25, durabilidad: 2
```

---

## Parte 2: Clase `Guerrero` (5 puntos)

Crea una clase `Guerrero` con:

- `nombre` (`str`)
- `vida` (`int`)
- `arma` (objeto `Arma`)

### Requisitos:

- Constructor con validación:
  - `nombre` no puede estar vacío.
  - `vida` debe ser > 0 y <= 100.
- Los atributos deben ser del tipo de datos indicado.
- Método `atacar(otro_guerrero)`:
  - Usa su arma (llama a `usar()`).
  - Reduce la vida del otro guerrero según el daño del arma, pero no puede dejarla menor que 0.
  - No hace daño si el arma está rota (`durabilidad = 0`).
  - No puede atacar si su vida es 0.
- Sobrecarga de `==`, `!=`: dos guerreros son iguales si tienen el mismo nombre (ignora vida y arma).
- Método `__str__`: `"Guerrero Ragnar - Vida: 80 - Arma: Espada de Fuego"`
- Método `curar(cantidad)` que recupera puntos de vida, sin superar 100.
- Atributos privados accesibles mediante propiedades.
  - El atributo `arma` puede modificarse con un setter.

### Ejemplo:

```python
g1 = Guerrero("Ragnar", 80, espada)
g2 = Guerrero("Lagertha", 100, Arma("Hacha", 20, 5))
g1.atacar(g2)
print(g2.vida)  # 75 si arma hacía 25 de daño
```

---

## Parte 3: Sistema de combate (3 puntos)

Crea una función `duelo(guerrero1, guerrero2)` que simule un combate por turnos:

- Cada guerrero ataca al otro por turnos (empieza `guerrero1`).
- El combate continúa hasta que uno quede sin vida o ambos sin durabilidad en sus armas (empate).
- La función debe retornar el nombre del ganador, o `"Empate"` si ninguno puede vencer.

### Ejemplo:

```python
duelo(g1, g2)  # Retorna "Lagertha" o "Ragnar" o "Empate"
```

> Si `g1` tiene 10 de vida y un arma con daño 3, y `g2` tiene 7 de vida y un arma con daño 2, al tercer turno ganaría `g1` y terminaría con 6 de vida.  
> Si el arma de `g1` tiene durabilidad 2 y la de `g2` durabilidad 5, perdería `g1`.
> Si ambas tienen durabilidad 2, acabaría en empate.

---

**🔧 Requisito final:** Hacer un programa que **pruebe TODO**.