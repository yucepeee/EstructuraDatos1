""" ADT Listas simple
Ejemplo de implementación de una Lista simple enlazada en Python.

Autor: Gabriel Romulo Arnez Joven

Registro: 220000417

Materia: Estructura de Datos 1

Profesor: Ing. Juan Carlos Peinado Pereira

"""

class Nodo():
    """Clase Nodo para la lista enlazada"""

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class Lista():
    """Clase Lista para la lista enlazada"""

    def __init__(self):
        self.cabeza = None
        self.tamano = 0

    def esta_vacia(self):
        """Verifica si la lista está vacía"""
        
        return self.cabeza is None

    def tamano(self):
        """Devuelve el tamaño de la lista"""

        return self.tamano

    def agregar(self, dato):
        """Agrega un nuevo nodo al final de la lista"""

        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.tamano += 1

    def eliminar(self, dato):
        """Elimina un nodo de la lista por su valor"""

        if self.esta_vacia():
            return False
        if self.cabeza.dato == dato:
            self.cabeza = self.cabeza.siguiente
            self.tamano -= 1
            return True
        actual = self.cabeza
        while actual.siguiente:
            if actual.siguiente.dato == dato:
                actual.siguiente = actual.siguiente.siguiente
                self.tamano -= 1
                return True
            actual = actual.siguiente
        return False

    def buscar(self, dato):
        """Busca un nodo en la lista por su valor"""

        actual = self.cabeza
        while actual:
            if actual.dato == dato:
                return True
            actual = actual.siguiente
        return False

    def imprimir(self):
        """Imprime los elementos de la lista"""

        elementos = []
        actual = self.cabeza
        while actual:
            elementos.append(actual.dato)
            actual = actual.siguiente
        print("Lista:", elementos)

    def tamano(self):
        """Devuelve el tamaño de la lista"""

        return self.tamano
    def insertar(self, dato, posicion):
        """Inserta un nuevo nodo en una posición específica de la lista"""

        if posicion < 0 or posicion > self.tamano:
            raise IndexError("Posición fuera de rango")
        nuevo_nodo = Nodo(dato)
        if posicion == 0:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            for _ in range(posicion - 1):
                actual = actual.siguiente
            nuevo_nodo.siguiente = actual.siguiente
            actual.siguiente = nuevo_nodo
        self.tamano += 1

    def get_index(self, posicion):
        """Obtiene el valor de un nodo en una posición específica de la lista"""

        if posicion < 0 or posicion >= self.tamano:
            raise IndexError("Posición fuera de rango")
        actual = self.cabeza
        for _ in range(posicion):
            actual = actual.siguiente
        return actual.dato

    def eliminar_index(self, posicion):
        """Elimina un nodo en una posición específica de la lista"""

        if posicion < 0 or posicion >= self.tamano:
            raise IndexError("Posición fuera de rango")
        if posicion == 0:
            self.cabeza = self.cabeza.siguiente
        else:
            actual = self.cabeza
            for _ in range(posicion - 1):
                actual = actual.siguiente
            actual.siguiente = actual.siguiente.siguiente
        self.tamano -= 1

    def display(self):
        """Imprime los elementos de la lista enlazada."""
        current = self.cabeza
        while current:
            print(current.dato, end=" -> ")
            current = current.siguiente
        print("None")

# Ejemplo de uso de la clase Lista
if __name__ == "__main__":
    lista = Lista()
    lista.agregar(1)
    lista.agregar(2)
    lista.agregar(3)
    lista.imprimir()  # Lista: [1, 2, 3]
    lista.display()  # Muestra la lista enlazada: 1 -> 2 -> 3 -> None
    print(lista.buscar(2))  # Buscar 2: True
    print(lista.eliminar(2))  # Eliminar 2: True
    lista.imprimir()  # Lista: [1, 3]
    print(lista.tamano)  # Tamaño de la lista: 2
    lista.insertar(4, 1)
    lista.imprimir()  # Lista: [1, 4, 3]
    print(lista.get_index(1))  # Obtener valor en posición 1: 4
    lista.eliminar_index(1)
    lista.imprimir()  # Lista: [1, 3]