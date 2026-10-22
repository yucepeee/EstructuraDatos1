# Simulador de centro logístico

Aplicación de escritorio educativa para visualizar operaciones de un centro
logístico y el uso de estructuras de datos enlazadas. Está desarrollada en
Python con Flet.

## Funcionalidades

- Registrar almacenes y visualizarlos como una ruta circular.
- Registrar vehículos en una flota circular.
- Recibir pedidos y ordenarlos por prioridad numérica, de mayor a menor. Los
  pedidos con la misma prioridad conservan el orden de llegada.
- Despachar el pedido más urgente al primer vehículo disponible que tenga
  capacidad suficiente.
- Ver los pedidos pendientes y la carga de cada vehículo.
- Deshacer y rehacer operaciones de despacho.
- Avanzar el vehículo por la ruta. Cuando completa una vuelta, los vehículos
  que estén llenos descargan sus paquetes.
- Ejecutar una demostración guiada y consultar métricas aproximadas de
  operaciones, nodos y tiempo de ejecución.

### Capacidad de los vehículos

Cada vehículo tiene una capacidad máxima de 10 unidades. El peso asignado a
cada paquete depende de su prioridad:

| Prioridad | Espacio ocupado |
| --- | ---: |
| Menor que 5 | 1 unidad |
| De 5 a 9 | 2 unidades |
| 10 o más | 10 unidades |

La interfaz muestra de 1 a 10 como rango de referencia y admite prioridades
enteras positivas. Los pedidos de mayor prioridad se procesan primero; los de
prioridad 10 o superior ocupan toda la capacidad del vehículo.

## Estructuras de datos

Las implementaciones manuales se encuentran en `src/models/structures.py`:

- `DoublyLinkedList`: almacenes en el modelo del motor.
- `CircularDoublyLinkedList`: ruta de almacenes que muestra la interfaz.
- `PriorityQueue`: pedidos pendientes, ordenados por prioridad.
- `CircularQueue`: flota de vehículos.
- `Stack`: carga LIFO de cada vehículo y pilas internas del historial.
- `UndoRedoManager`: almacenamiento de acciones para deshacer y rehacer.

El deshacer y rehacer disponible en la interfaz está implementado para los
despachos. La aplicación presenta las estructuras y sus operaciones; no incluye
persistencia de datos, por lo que los datos se reinician al cerrar el programa.

## Estructura del proyecto

```text
Proyecto/
├── README.md
├── requirements.txt
└── src/
    ├── main.py
    ├── test_engine.py
    ├── test_structures.py
    ├── controllers/
    │   └── app_controller.py
    ├── models/
    │   ├── logistic_engine.py
    │   └── structures.py
    └── views/
        ├── desktop_view.py
        └── responsive_components.py
```

### Componentes principales

- `src/main.py`: inicia la aplicación Flet.
- `src/models/logistic_engine.py`: define paquetes, vehículos, almacenes y
  lógica de recepción y despacho.
- `src/models/structures.py`: implementa las estructuras de datos enlazadas.
- `src/controllers/app_controller.py`: coordina la interfaz, el motor, la ruta
  y las acciones de deshacer/rehacer.
- `src/views/desktop_view.py`: construye la interfaz y los controles.
- `src/views/responsive_components.py`: dibuja las estructuras y el panel de
  métricas.
- `src/test_engine.py` y `src/test_structures.py`: pruebas del motor y las
  estructuras.

## Requisitos e instalación

- Python 3.10 o superior.
- Flet.

El archivo `requirements.txt` está vacío actualmente; instala Flet directamente:

```bash
python -m venv .venv
```

En Windows:

```powershell
.\.venv\Scripts\Activate.ps1
python -m pip install flet
```

En macOS o Linux:

```bash
source .venv/bin/activate
python -m pip install flet
```

## Ejecución

Desde la raíz del proyecto:

```bash
python src/main.py
```

La interfaz incluye el botón **Ejecutar Demo**, que carga datos de ejemplo y
recorre las operaciones de la simulación.

## Pruebas

Los módulos de prueba importan los paquetes desde `src`, por lo que se ejecutan
desde ese directorio:

```bash
cd src
python -m unittest test_structures test_engine
```

## Objetivo pedagógico

El proyecto permite observar la inserción y recorrido de nodos, la atención por
prioridad, el comportamiento LIFO de una pila, la asignación circular de
vehículos y el costo aproximado de algunas operaciones.

## Autoría

- **Nombre:** Gabriel Romulo Arnez Joven
- **Registro:** 220000417
- **Materia:** Estructura de Datos 1
- **Docente:** Ing. Juan Carlos Peinado Pereira
