# 🗼 Torres de Hanoi - Python (MVC)

Aplicación de escritorio desarrollada en **Python** utilizando **CustomTkinter**, que permite jugar de forma interactiva al clásico problema de las **Torres de Hanoi**.

El proyecto fue desarrollado siguiendo el patrón de arquitectura **MVC (Modelo - Vista - Controlador)**, separando la lógica del juego, la interfaz gráfica y el control de eventos.

---

## 📸 Características

- Interfaz gráfica moderna con **CustomTkinter**.
- Selección del número de discos.
- Movimiento manual de discos mediante clics.
- Validación automática de movimientos.
- Contador de movimientos.
- Cronómetro de partida.
- Ventana emergente al completar el juego.
- Código organizado utilizando el patrón MVC.

---

# Tecnologías utilizadas

- Python 3
- CustomTkinter
- Tkinter (Canvas)

---

# Estructura del proyecto

```
Proyecto2_Pilas_Colas/
│
├── src/
│   ├── controllers/
│   │      controller.py
│   │
│   ├── models/
│   │      model.py
│   │
│   ├── views/
│   │      view.py
│   │
│   └── main.py
│
├── README.md
└── requirements.txt
```

---

# Arquitectura MVC

## Modelo (Model)

Se encarga exclusivamente de almacenar la información del juego y aplicar sus reglas.

Responsabilidades:

- Crear las tres torres.
- Inicializar los discos.
- Validar movimientos.
- Mover discos.
- Comprobar cuándo el juego termina.

No conoce absolutamente nada de la interfaz gráfica.

---

## Vista (View)

Es toda la interfaz gráfica.

Responsabilidades:

- Mostrar botones.
- Mostrar el Canvas.
- Dibujar torres.
- Dibujar discos.
- Mostrar contador.
- Mostrar cronómetro.
- Mostrar la ventana de victoria.

La Vista **no contiene lógica del juego**.

---

## Controlador (Controller)

Es el intermediario entre la Vista y el Modelo.

Responsabilidades:

- Detectar clics del usuario.
- Interpretar qué torre fue seleccionada.
- Pedir al Modelo mover discos.
- Actualizar la Vista.
- Controlar el cronómetro.
- Contar movimientos.
- Detectar cuándo termina el juego.

---

# Funcionamiento del juego

1. El usuario escribe el número de discos.
2. Presiona **Iniciar**.
3. Se crean todas las torres.
4. Comienza el cronómetro.
5. El usuario selecciona una torre de origen.
6. Luego selecciona una torre destino.
7. El Modelo valida el movimiento.
8. Si es válido:
   - mueve el disco
   - incrementa el contador
   - redibuja las torres
9. Si todos los discos llegan a la torre C:
   - se detiene el cronómetro
   - aparece una ventana de felicitación.

---

# Flujo de información

```
Usuario

   ↓

Canvas (click)

   ↓

View.click()

   ↓

Controller.on_click()

   ↓

Model.mover_disco()

   ↓

Controller

   ↓

View.actualizar_torre()

   ↓

Canvas vuelve a dibujar todo
```

---

# Validaciones implementadas

- No mover desde una torre vacía.
- No colocar un disco grande sobre uno pequeño.
- No seleccionar dos veces la misma torre.
- No permitir movimientos fuera de las torres.
- Finalización automática al completar el juego.

---

# Cronómetro

El cronómetro comienza al iniciar una partida.

Se actualiza cada segundo utilizando:

```python
after(1000, actualizar_cronometro)
```

Al finalizar el juego se detiene automáticamente.

---

# Contador de movimientos

Cada movimiento válido incrementa un contador.

Los movimientos inválidos no son contabilizados.

---

# Reglas del juego

- Solo puede moverse un disco a la vez.
- Solo puede moverse el disco superior.
- Nunca puede colocarse un disco grande sobre uno pequeño.
- El objetivo es mover todos los discos desde la Torre A hasta la Torre C.

---

# Instalación

Clonar el repositorio:

```bash
git clone https://github.com/yucepeee/EstructuraDatos1/tree/main/Proyecto2_Pilas_Colas
```

Entrar al proyecto:

```bash
cd Proyecto2_Pilas_Colas
```

Instalar dependencias:

```bash
pip install -r requirements.txt
```

Ejecutar:

```bash
python src/main.py
```

---

# Dependencias

Instalar:

```bash
pip install customtkinter
```

o utilizando:

```bash
pip install -r requirements.txt
```

---

# Posibles mejoras futuras

- Resolver automáticamente el problema utilizando recursividad.
- Historial de partidas.
- Guardar mejores tiempos.
- Selector de dificultad.
- Animaciones de movimiento.
- Sonidos.
- Modo oscuro/claro.
- Reiniciar partida.
- Mostrar el número mínimo de movimientos (2ⁿ−1).

---

# Gabriel Romulo Arnez Joven

Proyecto desarrollado para la materia **Estructura de Datos I** utilizando Python y el patrón de arquitectura MVC.