""" Pilas (Stack) en Python
Ejemplo de implementación de una Pila estática y dinámica en Python.

Autor: Gabriel Romulo Arnez Joven

Registro: 220000417

Materia: Estructura de Datos 1

Profesor: Ing. Juan Carlos Peinado Pereira

"""
class Nodo():
    """Clase Nodo para la pila dinámica"""

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None
        
class PilaEstatica():
    """Clase Pila para la pila estática"""

    def __init__(self, tamano):
        self.tamano = tamano
        self.pila = [None] * tamano
        self.tope = -1

    def esta_vacia(self):
        """Verifica si la pila está vacía"""
        
        return self.tope == -1

    def esta_llena(self):
        """Verifica si la pila está llena"""
        
        return self.tope == self.tamano - 1

    def apilar(self, dato):
        """Agrega un nuevo elemento a la pila"""

        if self.esta_llena():
            raise Exception("La pila está llena")
        self.tope += 1
        self.pila[self.tope] = dato

    def desapilar(self):
        """Elimina el elemento superior de la pila"""

        if self.esta_vacia():
            raise Exception("La pila está vacía")
        dato = self.pila[self.tope]
        self.pila[self.tope] = None
        self.tope -= 1
        return dato

    def ver_tope(self):
        """Devuelve el elemento superior de la pila sin eliminarlo"""

        if self.esta_vacia():
            raise Exception("La pila está vacía")
        return self.pila[self.tope]

class PilaDinamica():
    """Clase Pila para la pila dinámica"""

    def __init__(self):
        self.cabeza = None
        self.tamano = 0

    def esta_vacia(self):
        """Verifica si la pila está vacía"""
        
        return self.cabeza is None

    def tamano(self):
        """Devuelve el tamaño de la pila"""

        return self.tamano

    def apilar(self, dato):
        """Agrega un nuevo elemento a la pila"""

        nuevo_nodo = Nodo(dato)
        nuevo_nodo.siguiente = self.cabeza
        self.cabeza = nuevo_nodo
        self.tamano += 1

    def desapilar(self):
        """Elimina el elemento superior de la pila"""

        if self.esta_vacia():
            raise Exception("La pila está vacía")
        dato = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        self.tamano -= 1
        return dato

    def ver_tope(self):
        """Devuelve el elemento superior de la pila sin eliminarlo"""

        if self.esta_vacia():
            raise Exception("La pila está vacía")
        return self.cabeza.dato

if __name__ == "__main__":
    # Ejemplo de uso de la pila estática
    pila_estatica = PilaEstatica(5)
    pila_estatica.apilar(1)
    pila_estatica.apilar(2)
    pila_estatica.apilar(3)
    print("Tope de la pila estática:", pila_estatica.ver_tope())
    print("Desapilando:", pila_estatica.desapilar())
    print("Tope de la pila estática después de desapilar:", pila_estatica.ver_tope())

    # Ejemplo de uso de la pila dinámica
    pila_dinamica = PilaDinamica()
    pila_dinamica.apilar(1)
    pila_dinamica.apilar(2)
    pila_dinamica.apilar(3)
    print("Tope de la pila dinámica:", pila_dinamica.ver_tope())
    print("Desapilando:", pila_dinamica.desapilar())
    print("Tope de la pila dinámica después de desapilar:", pila_dinamica.ver_tope())