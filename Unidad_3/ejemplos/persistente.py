""" Estructura de datos persistente en Python.

Autor: Gabriel Romulo Arnez Joven

Registro: 220000417

Materia: Estructura de Datos 1

Profesor: Ing. Juan Carlos Peinado Pereira

"""
import json

class Nodo():
    """Clase Nodo para la estructura de datos persistente"""

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class PilaPersistente():
    """Clase Pila para la estructura de datos persistente"""

    def __init__(self):
        self.tope = None

    def esta_vacia(self):
        """Verifica si la pila está vacía"""
        return self.tope is None

    def apilar(self, dato):
        """Agrega un nuevo elemento a la pila"""
        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.tope
        self.tope = nuevo_nodo

    def desapilar(self):
        """Elimina el elemento superior de la pila"""
        if self.esta_vacia():
            raise Exception("La pila está vacía")
        dato = self.tope.dato
        self.tope = self.tope.siguiente
        return dato

    def ver_tope(self):
        """Devuelve el elemento superior de la pila sin eliminarlo"""
        if self.esta_vacia():
            raise Exception("La pila está vacía")
        return self.tope.dato

    def guardar_en_archivo(self, nombre_archivo):
        """Guarda la pila en un archivo JSON para persistencia"""
        pila_lista = []
        nodo_actual = self.tope
        while nodo_actual is not None:
            pila_lista.append(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente
        with open(nombre_archivo, 'w') as archivo:
            json.dump(pila_lista, archivo)

    def cargar_desde_archivo(self, nombre_archivo):
        """Carga la pila desde un archivo JSON para persistencia"""
        with open(nombre_archivo, 'r') as archivo:
            pila_lista = json.load(archivo)
        self.tope = None
        for dato in reversed(pila_lista):
            self.apilar(dato)

    def _datos_pila(self):
        datos = []
        nodo_actual = self.tope
        while nodo_actual is not None:
            datos.append(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente
        return datos

    def __str__(self) -> str:
        if self.esta_vacia():
            return "Pila(vacía)"
        return f"Pila({self._datos_pila()})"


class ColaPersistente():
    """Clase Cola para la estructura de datos persistente"""

    def __init__(self):
        self.frente = None
        self.final = None

    def esta_vacia(self):
        """Verifica si la cola está vacía"""
        return self.frente is None

    def encolar(self, dato):
        """Agrega un nuevo elemento a la cola"""
        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.frente = nuevo_nodo
            self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo

    def desencolar(self):
        """Elimina el elemento frontal de la cola"""
        if self.esta_vacia():
            raise Exception("La cola está vacía")
        dato = self.frente.dato
        self.frente = self.frente.siguiente
        if self.frente is None:
            self.final = None
        return dato

    def ver_frente(self):
        """Devuelve el elemento frontal de la cola sin eliminarlo"""
        if self.esta_vacia():
            raise Exception("La cola está vacía")
        return self.frente.dato

    def guardar_en_archivo(self, nombre_archivo):
        """Guarda la cola en un archivo JSON para persistencia"""
        cola_lista = []
        nodo_actual = self.frente
        while nodo_actual is not None:
            cola_lista.append(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente
        with open(nombre_archivo, 'w') as archivo:
            json.dump(cola_lista, archivo)

    def cargar_desde_archivo(self, nombre_archivo):
        """Carga la cola desde un archivo JSON para persistencia"""
        with open(nombre_archivo, 'r') as archivo:
            cola_lista = json.load(archivo)
        self.frente = None
        self.final = None
        for dato in cola_lista:
            self.encolar(dato)

    def _datos_cola(self):
        datos = []
        nodo_actual = self.frente
        while nodo_actual is not None:
            datos.append(nodo_actual.dato)
            nodo_actual = nodo_actual.siguiente
        return datos

    def __str__(self) -> str:
        if self.esta_vacia():
            return "Cola(vacía)"
        return f"Cola({self._datos_cola()})"

# Ejemplo de uso
if __name__ == "__main__":
    # Crear una pila persistente
    pila = PilaPersistente()
    pila.apilar(10)
    pila.apilar(20)
    pila.apilar(30)
    print("Pila antes de guardar:", pila)

    # Guardar la pila en un archivo
    pila.guardar_en_archivo("pila.json")

    # Crear una nueva instancia de la pila y cargar desde el archivo
    nueva_pila = PilaPersistente()
    nueva_pila.cargar_desde_archivo("pila.json")
    print("Pila después de cargar:", nueva_pila)

    # Crear una cola persistente
    cola = ColaPersistente()
    cola.encolar(1)
    cola.encolar(2)
    cola.encolar(3)
    print("Cola antes de guardar:", cola)

    # Guardar la cola en un archivo
    cola.guardar_en_archivo("cola.json")

    # Crear una nueva instancia de la cola y cargar desde el archivo
    nueva_cola = ColaPersistente()
    nueva_cola.cargar_desde_archivo("cola.json")
    print("Cola después de cargar:", nueva_cola)