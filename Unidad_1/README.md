# Unidad I: Modelos de Representación de Datos

Un **dato** es una representación de un hecho, objeto o valor que puede ser almacenada y procesada. Por sí solo puede tener poco significado; al organizarlo y relacionarlo con otros datos, se convierte en información útil.

### Ejemplo

```python
nombre = "Ana"
edad = 20
estudiante_activa = True

print(nombre, edad, estudiante_activa)
```

En este caso, `"Ana"`, `20` y `True` son datos de distintos tipos: texto, entero y booleano.

## 2. 🧩 Datos abstractos (ADT)

Un **tipo de dato abstracto** (*Abstract Data Type*, ADT) describe qué operaciones se pueden realizar sobre los datos, sin indicar cómo se implementan internamente.

Por ejemplo, una **pila** sigue la regla **LIFO** (*Last In, First Out*): el último elemento que entra es el primero que sale. Sus operaciones principales son:

- `apilar`: agregar un elemento.
- `desapilar`: retirar el último elemento.
- `tope`: consultar el último elemento sin retirarlo.

### Ejemplo

```python
pila = []

pila.append("A")  # apilar
pila.append("B")
elemento = pila.pop()  # desapilar: sale "B"

print(elemento)
print(pila)
```

El ADT define el comportamiento de la pila; la lista de Python es solo una posible implementación.

## 3. 📦 Datos estáticos

Los **datos estáticos** tienen un tamaño definido desde el inicio y no cambian automáticamente durante la ejecución. Son útiles cuando conocemos de antemano cuántos elementos necesitamos manejar.

### Ejemplo

```python
calificaciones = [8.5, 9.0, 7.5, 10.0]

cantidad = 4  # tamaño definido para este ejemplo
promedio = sum(calificaciones) / cantidad

print(f"Promedio: {promedio}")
```

En una estructura estática real, intentar guardar más elementos que su capacidad produciría un error o requeriría crear otra estructura.

## 4. 🔄 Datos dinámicos

Los **datos dinámicos** pueden aumentar o reducir su tamaño mientras el programa está ejecutándose. Esto permite adaptarse a cantidades de información que no conocemos previamente.

### Ejemplo

```python
pendientes = []

pendientes.append("Estudiar listas")
pendientes.append("Resolver ejercicios")
pendientes.pop(0)  # elimina la primera tarea
pendientes.append("Repasar conceptos")

print(pendientes)
```

La lista se ajusta según las operaciones realizadas, por lo que no es necesario reservar una cantidad fija de posiciones al comenzar.

## 5. 🎲 Datos simulados

Los **datos simulados** son valores generados artificialmente para representar una situación real. Se usan para practicar, hacer pruebas o modelar escenarios sin utilizar información real.

### Ejemplo

```python
import random

temperaturas = [random.randint(18, 30) for _ in range(5)]

print("Temperaturas simuladas:", temperaturas)
print("Máxima:", max(temperaturas))
```

Cada ejecución puede generar valores diferentes, pero todos pertenecen al rango definido.

## 6. 💾 Datos persistentes

Los **datos persistentes** sobreviven después de cerrar el programa porque se guardan en un medio externo, como un archivo o una base de datos.

### Ejemplo

```python
import json

usuario = {"nombre": "Ana", "semestre": 1}

with open("usuario.json", "w", encoding="utf-8") as archivo:
	json.dump(usuario, archivo, ensure_ascii=False, indent=2)

with open("usuario.json", "r", encoding="utf-8") as archivo:
	usuario_guardado = json.load(archivo)

print(usuario_guardado)
```

El archivo `usuario.json` conserva la información para que pueda recuperarse en otra ejecución.

## 7. 📊 Resumen comparativo

| Concepto | Característica principal | Ejemplo común | ¿Sobrevive al cerrar el programa? |
| --- | --- | --- | --- |
| Dato | Valor que puede procesarse | `20`, `"Ana"`, `True` | No necesariamente |
| ADT | Define operaciones y comportamiento | Pila o cola | Depende de su implementación |
| Estático | Tamaño definido previamente | Arreglo de tamaño fijo | No |
| Dinámico | Cambia de tamaño durante la ejecución | Lista enlazada o lista de Python | No |
| Simulado | Representa datos generados artificialmente | Temperaturas aleatorias | No, salvo que se guarde |
| Persistente | Se almacena fuera de la memoria temporal | Archivo JSON o base de datos | Sí |

### Idea clave

> **Los conceptos se pueden combinar.** Una lista dinámica puede contener datos simulados y después guardarse como datos persistentes en un archivo JSON.

---

## Ejecución

Los ejemplos pueden copiarse y ejecutarse con Python 3:

```bash
python ejemplos.py
```

> Nota: el archivo `ejemplos.py` está reservado para reunir los ejemplos prácticos de esta unidad.