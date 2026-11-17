""" Colas Circulares en Python
Ejemplo de implementación de una Cola Circular en Python.

Autor: Gabriel Romulo Arnez Joven

Registro: 220000417

Materia: Estructura de Datos 1

Profesor: Ing. Juan Carlos Peinado Pereira

"""

class Nodo():
    """Clase Nodo para la cola circular"""

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None

class ColaCircular():
    """Clase Cola para la cola circular"""

    def __init__(self, tamano):
        self.tamano = tamano
        self.cola = [None] * tamano
        self.frente = 0
        self.final = -1
        self.cantidad = 0

    def esta_vacia(self):
        """Verifica si la cola está vacía"""
        
        return self.cantidad == 0

    def esta_llena(self):
        """Verifica si la cola está llena"""
        
        return self.cantidad == self.tamano

    def encolar(self, dato):
        """Agrega un nuevo elemento a la cola"""

        if self.esta_llena():
            raise Exception("La cola está llena")
        self.final = (self.final + 1) % self.tamano
        self.cola[self.final] = dato
        self.cantidad += 1

    def desencolar(self):
        """Elimina el elemento frontal de la cola"""

        if self.esta_vacia():
            raise Exception("La cola está vacía")
        dato = self.cola[self.frente]
        self.cola[self.frente] = None
        self.frente = (self.frente + 1) % self.tamano
        self.cantidad -= 1
        return dato

    def ver_frente(self):
        """Devuelve el elemento frontal de la cola sin eliminarlo"""

        if self.esta_vacia():
            raise Exception("La cola está vacía")
        return self.cola[self.frente]

    def ver_final(self):
        """Devuelve el elemento final de la cola sin eliminarlo"""

        if self.esta_vacia():
            raise Exception("La cola está vacía")
        return self.cola[self.final]

    def tamano(self):
        """Devuelve el tamaño de la cola"""

        return self.cantidad

    def mostrar(self):
        """Muestra los elementos de la cola"""

        if self.esta_vacia():
            print("La cola está vacía")
            return
        print("Elementos de la cola:")
        for i in range(self.cantidad):
            indice = (self.frente + i) % self.tamano
            print(self.cola[indice], end=" ")
        print()


# Ejemplo de uso de la Cola Circular

if __name__ == "__main__":
    cola = ColaCircular(5)
    cola.encolar(1)
    cola.encolar(2)
    cola.encolar(3)
    cola.mostrar()
    print("Frente:", cola.ver_frente())
    print("Final:", cola.ver_final())
    cola.desencolar()
    cola.mostrar()