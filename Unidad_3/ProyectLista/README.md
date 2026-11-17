# Biblioteca Musical con Listas Enlazadas

Aplicación de escritorio desarrollada en Python para administrar una biblioteca musical mediante una lista simplemente enlazada. El proyecto aplica conceptos de estructuras de datos y organiza el código con el patrón Modelo-Vista-Controlador (MVC).

## Funcionalidades

- Agregar canciones con título, artista y duración.
- Buscar canciones por coincidencia parcial en el título o el artista.
- Eliminar una canción por su título exacto, sin distinguir mayúsculas y minúsculas.
- Mostrar las canciones de la biblioteca.
- Crear y mostrar una playlist a partir de títulos ingresados.
- Interactuar con la aplicación mediante una interfaz gráfica de Tkinter.

## Estructura del proyecto

```text
ProyectLista/
├── src/
│   ├── controllers/
│   │   └── controller.py
│   ├── models/
│   │   └── model.py
│   ├── views/
│   │   └── view.py
│   └── main.py
├── README.md
└── requirements.txt
```

### Componentes principales

- `src/models/model.py`: define los nodos y las operaciones de la lista enlazada.
- `src/views/view.py`: implementa la interfaz gráfica y los diálogos de usuario con Tkinter.
- `src/controllers/controller.py`: conecta las acciones de la interfaz con la lógica del modelo.
- `src/main.py`: crea e inicia los componentes de la aplicación.

## Requisitos

- Python 3.
- Tkinter, incluido habitualmente con Python. En algunas distribuciones de Linux puede ser necesario instalarlo por separado.

El archivo `requirements.txt` no declara paquetes externos: la aplicación utiliza módulos de la biblioteca estándar de Python.

## Ejecución

Desde la carpeta `ProyectLista`, ejecuta:

```bash
python src/main.py
```

En Windows también puedes usar el lanzador de Python:

```powershell
py src/main.py
```

Se abrirá la ventana principal. Usa los botones para gestionar canciones; los datos solicitados se ingresan en cuadros de diálogo.

## Funcionamiento de la lista

Cada canción se almacena en un nodo con sus datos (título, artista y duración) y una referencia al nodo siguiente. La biblioteca mantiene una referencia al primer nodo y recorre los enlaces para buscar, mostrar o eliminar canciones. Las playlists se construyen como nuevas listas enlazadas a partir de los títulos indicados.

## Alcance

Los datos se mantienen en memoria y no se guardan en archivos ni en una base de datos. Al cerrar la aplicación, la biblioteca y las playlists creadas dejan de estar disponibles.

## Información académica

- **Autor:** Gabriel Romulo Arnez Joven
- **Registro:** 220000417
- **Materia:** Estructura de Datos 1
- **Docente:** Ing. Juan Carlos Peinado Pereira

Proyecto realizado con fines educativos para estudiar la implementación y el uso de listas simplemente enlazadas en Python.