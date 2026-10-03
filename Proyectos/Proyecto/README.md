# Simulador de logística y estructuras de datos

Proyecto educativo de Estructuras de Datos 1 que busca evolucionar hacia un
simulador de logística y despacho de recursos. Este README describe el estado
del código disponible actualmente; la propuesta completa todavía no está
implementada.

## Estado actual

La interfaz existente es una ventana de escritorio hecha con **Tkinter**. Muestra
una etiqueta y un botón que cambia el texto de la etiqueta. No es todavía una
interfaz de simulación logística y el proyecto **no utiliza Flet**.

En `src/models/structures.py` están implementadas manualmente con nodos:

- Lista doblemente enlazada, con inserción al inicio y al final, búsqueda y
  eliminación por valor.
- Pila enlazada (`Stack`), con operaciones `push` y `pop`.
- Gestor de deshacer y rehacer (`UndoRedoManager`), basado en dos pilas.
- Cola circular enlazada, con operaciones `enqueue` y `dequeue`.
- Cola de prioridad enlazada, que atiende primero el elemento con el número de
  prioridad más alto.

Estas estructuras todavía no están integradas en la interfaz. Tampoco se
encuentran implementados el motor logístico, las rutas de despacho, las listas
simplemente enlazadas ni una cola FIFO convencional.

## Estructura del proyecto

```text
src/
├── main.py
├── controllers/
│   └── app_controller.py
├── models/
│   ├── logistic_engine.py
│   └── structures.py
├── views/
│   ├── desktop_view.py
│   └── responsive_components.py
└── test_structures.py
requirements.txt
```

La organización separa archivos en modelos, vistas y controladores, pero el
flujo MVC aún no está conectado funcionalmente. `logistic_engine.py` y
`responsive_components.py` no contienen implementación actualmente.

## Requisitos y ejecución

- Python 3.
- Tkinter, incluido normalmente con las distribuciones de Python para
  escritorio.
- `requirements.txt` no declara dependencias externas.

La aplicación aún no puede iniciarse correctamente tal como está: `main.py`
importa `DataModel` desde `models.structures`, pero esa clase no existe. Además,
la creación del controlador y las interfaces esperadas por `Controller` no
coinciden con las definidas en la vista actual. Es necesario resolver esa
integración antes de ejecutar `main.py`.

## Pruebas

Las pruebas existentes cubren la eliminación en la lista doblemente enlazada y
el orden de atención de la cola de prioridad y la cola circular. Para ejecutarlas
desde la carpeta `src`:

```bash
python -m unittest test_structures
```

## Objetivo del proyecto

La propuesta es desarrollar un simulador educativo de un centro logístico que
permita aplicar estructuras de datos lineales implementadas desde cero,
arquitectura MVC y operaciones de deshacer/rehacer. La meta planteada contempla
una interfaz multiplataforma con Flet; su implementación, así como el análisis
de complejidad de las operaciones, queda pendiente en el código actual.

## Autor

- **Nombre:** Gabriel Romulo Arnez Joven
- **Registro:** 220000417
- **Materia:** Estructura de Datos 2
- **Docente:** Ing. Juan Carlos Peinado Pereira