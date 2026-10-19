# Simulador de logística y estructuras de datos

Proyecto educativo desarrollado para aplicar estructuras de datos lineales en un
simulador de centro logístico. La aplicación combina una interfaz gráfica con
Flet y una implementación manual de varios tipos de estructuras enlazadas.

## Estado actual

La versión actual ya incluye una interfaz funcional de escritorio con **Flet**
para simular operaciones de recepción, despacho, almacenamiento y carga de
vehículos.

### Estructuras implementadas

En `src/models/structures.py` se desarrollan manualmente con nodos:

- Lista doblemente enlazada (`DoublyLinkedList`)
- Pila enlazada (`Stack`)
- Gestor de deshacer y rehacer (`UndoRedoManager`)
- Cola circular (`CircularQueue`)
- Cola de prioridad (`PriorityQueue`)

Estas estructuras se usan en el motor del sistema para modelar:

- Almacenes (lista doblemente enlazada)
- Pedidos pendientes (cola de prioridad)
- Flota de vehículos (cola circular)
- Carga de cada vehículo (pila LIFO)
- Historial de acciones (deshacer/rehacer)

## Arquitectura del proyecto

```text
Proyecto/
├── README.md
├── requirements.txt
├── src/
│   ├── main.py
│   ├── test_structures.py
│   ├── controllers/
│   │   └── app_controller.py
│   ├── models/
│   │   ├── logistic_engine.py
│   │   └── structures.py
│   └── views/
│       ├── desktop_view.py
│       └── responsive_components.py
└── .venv/
```

### Componentes principales

- `src/main.py`: punto de entrada de la aplicación
- `src/models/logistic_engine.py`: motor lógico del simulador
- `src/models/structures.py`: implementaciones de estructuras de datos
- `src/controllers/app_controller.py`: coordinación entre la vista y el motor
- `src/views/desktop_view.py`: interfaz principal con Flet
- `src/views/responsive_components.py`: componentes visuales de cada estructura

## Requisitos

- Python 3.10 o superior
- Flet

### Instalación

Se recomienda usar un entorno virtual e instalar las dependencias necesarias:

```bash
python -m venv .venv
.venv\Scripts\activate
pip install flet
```

## Ejecución

Desde la raíz del proyecto:

```bash
python src/main.py
```

También es posible ejecutarlo con Flet directamente:

```bash
python -m flet run src/main.py
```

## Pruebas

Las pruebas actuales validan el comportamiento de las estructuras implementadas.
Para ejecutarlas:

```bash
cd src
python -m unittest test_structures
```

Resultado esperado:

```text
Ran 3 tests in 0.000s

OK
```

## Funcionalidades del simulador

- Agregar almacenes a la red logística
- Registrar vehículos en la flota
- Crear paquetes con prioridad
- Encolar pedidos según nivel de prioridad
- Despachar el siguiente pedido con atención por prioridad
- Cargar paquetes en cada vehículo mediante una pila
- Deshacer y rehacer operaciones de despacho

## Objetivo pedagógico

El proyecto tiene un enfoque académico y permite visualizar cómo se aplican:

- listas enlazadas,
- colas,
- pilas,
- prioridad,
- deshacer/rehacer,
- arquitectura MVC en una aplicación de escritorio.

## Autor

- **Nombre:** Gabriel Romulo Arnez Joven
- **Registro:** 220000417
- **Materia:** Estructura de Datos 1
- **Docente:** Ing. Juan Carlos Peinado Pereira