# Unidad 0 · Estándares y Buenas Prácticas de Codificación

## 🐍 Guía de estilo de código Python (PEP 8)

PEP 8 es la guía de estilo oficial para escribir código Python de forma limpia, legible y profesional. Siguiendo estos estándares, tu código será más fácil de leer tanto para ti como para cualquier otro desarrollador.

---

## 1. 📌 Convenciones de nombres

| Tipo | Convención de estilo | Ejemplo |
| :--- | :--- | :--- |
| **Variables y funciones** | `snake_case` (minúsculas con guiones bajos) | `total_suma`, `calcular_promedio()` |
| **Constantes** | `UPPER_SNAKE_CASE` (mayúsculas sostenidas) | `LIMITE_MAXIMO = 100`, `PI = 3.1416` |
| **Clases** | `PascalCase` / `CapWords` | `CuentaBancaria`, `NodoPila` |
| **Módulos / archivos** | `snake_case` corto | `mi_tarea.py`, `operaciones.py` |
| **Atributos protegidos / privados** | Guion bajo al inicio | `_variable_protegida`, `__variable_privada` |

---

## 2. 🧱 Indentación y espacio en blanco

- **Sangría:** usa 4 espacios por nivel. No uses tabulaciones ni mezcles espacios con tabs.
- **Líneas en blanco:** usa 2 líneas en blanco para separar funciones globales y clases; usa 1 línea para separar métodos dentro de una clase.
- **Operadores:** incluye un espacio a ambos lados de los operadores binarios (`+`, `-`, `=`, `==`, etc.). No uses espacios alrededor del `=` cuando se especifique un argumento por defecto en una función.

### Ejemplo:

```python
def funcion(parametro=10):
    resultado = parametro + 5
    return resultado
```

---

## 3. 📦 Estructura e importaciones

- Coloca todas las importaciones al inicio del archivo, inmediatamente después de los comentarios o docstrings del módulo.
- Realiza cada importación en su propia línea.

| Correcto | Incorrecto |
| :--- | :--- |
| `import os` | `import os, sys` |
| `import sys` |  |

### Ejemplo de organización:

```python
import os
import sys

import requests

from mi_modulo import operacion
```

- Agrupa los imports en tres bloques separados por una línea en blanco:
  1. Librerías estándar de Python.
  2. Librerías de terceros (instaladas vía `pip`).
  3. Módulos locales del proyecto.

---

## 4. ✍️ Longitud de línea y comentarios

- **Límite de línea:** procura que las líneas no superen los 79 caracteres. Para comentarios o docstrings, mantén el límite en 72 caracteres.
- **Comentarios:** escribe comentarios descriptivos enfocados en explicar por qué se toma una decisión en el código, no qué hace el código si es autoexplicativo.
- **Docstrings:** usa comillas dobles triples `"""` para definir docstrings en funciones, clases y módulos.

### Ejemplo:

```python
def calcular_promedio(numeros):
    """Calcula el promedio de una lista de números."""
    total = sum(numeros)
    return total / len(numeros)
```

---

## ✅ Resumen rápido

Sigue estas reglas básicas y tu código será más claro, uniforme y fácil de mantener:

- Usa nombres descriptivos.
- Mantén una indentación consistente.
- Ordena bien tus imports.
- Limita la longitud de las líneas.
- Documenta lo necesario con comentarios y docstrings.

> La consistencia en el estilo mejora la legibilidad y facilita la colaboración entre desarrolladores.