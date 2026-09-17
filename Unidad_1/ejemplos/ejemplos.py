"""
Unidad I - Representación de Datos
---------------------------
Implementación de una lista enlazada simple en Python

Autor:     Gabriel Romulo Arnez Joven

Registro: 220000417

Materia:   Estructura de Datos 1

Profesor:  Ing. Juan Carlos Peinado Pereira

Fecha:     
"""

class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            raise IndexError("pop from empty stack")

# --- Prueba del Alumno ---
mi_pila = Stack()
mi_pila.push("A")
mi_pila.push("B")

print("¿Está vacía?", mi_pila.is_empty())
print("Elemento sacado:", mi_pila.pop())


class Automovil:
    def __init__(self, marca, modelo, color):
        self.marca = marca
        self.modelo = modelo
        self.color = color

    def __str__(self):
        return f"{self.color} {self.marca} {self.modelo}"

class Garaje:
    def __init__(self):
        self.automoviles = []

    def agregar_automovil(self, auto):
        self.automoviles.append(auto)

    def mostrar_automoviles(self):
        print("Automóviles en el garaje:")
        for i, auto in enumerate(self.automoviles):
            print(f"  {i+1}. {auto}")

# --- Prueba del Alumno ---
mi_garaje = Garaje()

# Crear dos automóviles distintos para comprobar que el garaje no reutiliza la misma instancia
mi_garaje.agregar_automovil(Automovil("Toyota", "Corolla", "Rojo"))
mi_garaje.agregar_automovil(Automovil("Honda", "Civic", "Azul"))

mi_garaje.mostrar_automoviles()


class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self):
        return f"({self.x}, {self.y})"

class Linea:
    def __init__(self, inicio, fin):
        self.inicio = Punto(inicio.x, inicio.y)
        self.fin = Punto(fin.x, fin.y)

    def __str__(self):
        return f"Línea de {self.inicio} a {self.fin}"

# --- Prueba del Alumno ---
punto_a = Punto(0, 0)
punto_b = Punto(5, 5)

mi_linea = Linea(punto_a, punto_b)
print(f"Línea original: {mi_linea}")

# El alumno modifica uno de los puntos originales
punto_a.x = 10
punto_a.y = 10

print(f"Línea después de modificar el punto 'A': {mi_linea}")