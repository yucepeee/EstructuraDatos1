# Unidad II: ADT Polinomio y ADT Conjuntos


## ADT Polinomio

Un polinomio se expresa como una suma de términos:

\[
P(x) = a_nx^n + a_{n-1}x^{n-1} + \cdots + a_1x + a_0
\]

Cada término está compuesto por:

| Elemento | Descripción | Ejemplo en `7x³` |
|---|---|---|
| Coeficiente | Número que multiplica a la variable | `7` |
| Variable | Símbolo utilizado para representar la incógnita | `x` |
| Exponente | Potencia de la variable | `3` |

### Representación computacional

Una representación común es almacenar cada término como un par **(coeficiente, exponente)**. Por ejemplo:

```text
P(x) = 4x^3 - 2x + 5
P = [(4, 3), (-2, 1), (5, 0)]
```

También puede utilizarse un arreglo, donde el índice representa el exponente:

```text
P = [5, -2, 0, 4]
	 |   |  |  |
	x^0 x^1 x^2 x^3
```

La representación por términos suele ser más eficiente cuando el polinomio es disperso, es decir, cuando contiene muchos exponentes sin término asociado.

### Ejemplo

Sean:

```text
P(x) = 3x^2 + 2x + 1
Q(x) = x^2 - 4
```

Una suma término a término produce:

```text
P(x) + Q(x) = (3 + 1)x^2 + 2x + (1 - 4)
			 = 4x^2 + 2x - 3
```

### Operaciones del ADT Polinomio

| Operación | Descripción | Ejemplo | Resultado |
|---|---|---|---|
| `crear()` | Crea un polinomio vacío | `P = crear()` | `P = 0` |
| `insertar(c, e)` | Agrega el término `c·x^e`; si el exponente existe, combina coeficientes | `insertar(3, 2)` | `3x²` |
| `eliminar(e)` | Elimina el término cuyo exponente es `e` | `P = 3x² + 2x + 1`, `eliminar(2)` | `2x + 1` |
| `consultar(e)` | Obtiene el coeficiente del exponente indicado | `consultar(2)` en `P` | `3` |
| `grado()` | Devuelve el exponente mayor con coeficiente distinto de cero | `grado(3x² + 2x + 1)` | `2` |
| `evaluar(v)` | Calcula el valor del polinomio para `x = v` | `evaluar(2)` en `x² + 1` | `5` |
| `sumar(P, Q)` | Suma los términos con exponentes iguales | `3x² + 2x + 1` y `x² - 4` | `4x² + 2x - 3` |
| `restar(P, Q)` | Resta dos polinomios | `3x² - (x² - 4)` | `2x² + 4` |
| `multiplicar(P, Q)` | Multiplica cada término de `P` por cada término de `Q` | `x · (x + 2)` | `x² + 2x` |
| `derivar()` | Calcula la derivada del polinomio | `derivar(3x² + 2x + 1)` | `6x + 2` |
| `mostrar()` | Devuelve el polinomio en formato legible | `mostrar(P)` | `3x² + 2x + 1` |

---

## ADT Conjuntos

Un conjunto es una colección de elementos **únicos**. El orden de los elementos no modifica el conjunto:

```text
A = {1, 2, 3}
B = {3, 4, 5}
```

En un conjunto no se permiten elementos repetidos, por lo que `{1, 1, 2}` equivale a `{1, 2}`.

### Representación computacional

Un conjunto puede implementarse mediante:

- **Arreglo o lista:** sencillo, pero puede requerir recorrer todos los elementos para buscar.
- **Lista enlazada:** facilita inserciones y eliminaciones según la implementación.
- **Tabla hash:** permite búsquedas rápidas en promedio.
- **Árbol de búsqueda:** mantiene los elementos ordenados y permite recorridos ordenados.

La implementación debe garantizar que un elemento no se inserte dos veces.

### Ejemplo

Dados los conjuntos:

```text
A = {1, 2, 3, 4}
B = {3, 4, 5, 6}
```

Sus operaciones principales son:

```text
A ∪ B = {1, 2, 3, 4, 5, 6}
A ∩ B = {3, 4}
A - B = {1, 2}
```

### Operaciones del ADT Conjuntos

| Operación | Descripción | Ejemplo | Resultado |
|---|---|---|---|
| `crear()` | Crea un conjunto vacío | `A = crear()` | `{}` |
| `agregar(e)` | Inserta un elemento si todavía no pertenece al conjunto | `A.agregar(3)` | `{3}` |
| `eliminar(e)` | Quita un elemento del conjunto | `{1, 2, 3}.eliminar(2)` | `{1, 3}` |
| `pertenece(e)` | Comprueba si un elemento está incluido | `pertenece(2)` en `{1, 2, 3}` | `Verdadero` |
| `tamaño()` | Devuelve el número de elementos | `tamaño({a, b, c})` | `3` |
| `unión(A, B)` | Forma un conjunto con los elementos de ambos conjuntos | `{1, 2} ∪ {2, 3}` | `{1, 2, 3}` |
| `intersección(A, B)` | Obtiene los elementos comunes | `{1, 2, 3} ∩ {2, 3, 4}` | `{2, 3}` |
| `diferencia(A, B)` | Obtiene los elementos de `A` que no están en `B` | `{1, 2, 3} - {2, 4}` | `{1, 3}` |
| `diferenciaSimétrica(A, B)` | Obtiene los elementos que pertenecen a un solo conjunto | `{1, 2} △ {2, 3}` | `{1, 3}` |
| `subconjunto(A, B)` | Comprueba si todos los elementos de `A` están en `B` | `{1, 2} ⊆ {1, 2, 3}` | `Verdadero` |
| `igual(A, B)` | Comprueba si ambos conjuntos tienen los mismos elementos | `{1, 2} = {2, 1}` | `Verdadero` |
| `vacío()` | Comprueba si el conjunto no contiene elementos | `vacío({})` | `Verdadero` |
| `mostrar()` | Devuelve los elementos en formato de conjunto | `mostrar(A)` | `{1, 2, 3}` |

### Propiedades importantes

| Propiedad | Expresión | Significado |
|---|---|---|
| Conmutativa | `A ∪ B = B ∪ A` | El orden de los conjuntos no cambia la unión. |
| Conmutativa | `A ∩ B = B ∩ A` | El orden de los conjuntos no cambia la intersección. |
| Idempotente | `A ∪ A = A` | Un conjunto unido consigo mismo permanece igual. |
| Idempotente | `A ∩ A = A` | La intersección consigo mismo es el mismo conjunto. |
| Elemento neutro | `A ∪ ∅ = A` | La unión con el conjunto vacío no agrega elementos. |
| Elemento absorbente | `A ∩ ∅ = ∅` | La intersección con el conjunto vacío siempre es vacía. |

---

## Comparación rápida

| Característica | ADT Polinomio | ADT Conjuntos |
|---|---|---|
| Elementos | Términos con coeficiente y exponente | Elementos únicos |
| Orden | Normalmente se ordena por exponente | No es relevante |
| Repeticiones | Se combinan términos con igual exponente | No se permiten |
| Operaciones principales | Suma, resta, multiplicación, evaluación y derivación | Unión, intersección, diferencia y pertenencia |
| Resultado típico | Otro polinomio o un valor numérico | Otro conjunto o un valor lógico |

