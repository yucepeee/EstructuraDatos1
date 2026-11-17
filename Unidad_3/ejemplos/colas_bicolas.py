""" Colas y Bicolas (Queue) en Python
Ejemplo de implementación de una Cola estática y dinámica en Python.

Autor: Gabriel Romulo Arnez Joven

Registro: 220000417

Materia: Estructura de Datos 1

Profesor: Ing. Juan Carlos Peinado Pereira

"""
class Nodo():
    """Clase Nodo para la cola dinámica"""

    def __init__(self, dato):
        self.dato = dato
        self.siguiente = None


class ColaEstatica():
    """Clase Cola para la cola estática"""

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


class ColaDinamica():
    """Clase Cola para la cola dinámica"""

    def __init__(self):
        self.cabeza = None
        self.final = None
        self.tamano = 0

    def esta_vacia(self):
        """Verifica si la cola está vacía"""
        
        return self.cabeza is None

    def encolar(self, dato):
        """Agrega un nuevo elemento a la cola"""

        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo
        self.tamano += 1

    def desencolar(self):
        """Elimina el elemento frontal de la cola"""

        if self.esta_vacia():
            raise Exception("La cola está vacía")
        dato = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        if self.cabeza is None:
            self.final = None
        self.tamano -= 1
        return dato

    def ver_frente(self):
        """Devuelve el elemento frontal de la cola sin eliminarlo"""

        if self.esta_vacia():
            raise Exception("La cola está vacía")
        return self.cabeza.dato


class Bicolas():
    """Clase Bicolas para la bicolad dinámica"""

    def __init__(self):
        self.cabeza = None
        self.final = None
        self.tamano = 0

    def esta_vacia(self):
        """Verifica si la bicolad está vacía"""
        
        return self.cabeza is None

    def encolar_frente(self, dato):
        """Agrega un nuevo elemento al frente de la bicolad"""

        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.final = nuevo_nodo
        else:
            nuevo_nodo.siguiente = self.cabeza
            self.cabeza = nuevo_nodo
        self.tamano += 1

    def encolar_final(self, dato):
        """Agrega un nuevo elemento al final de la bicolad"""

        nuevo_nodo = Nodo(dato)
        if self.esta_vacia():
            self.cabeza = nuevo_nodo
            self.final = nuevo_nodo
        else:
            self.final.siguiente = nuevo_nodo
            self.final = nuevo_nodo
        self.tamano += 1

    def desencolar_frente(self):
        """Elimina el elemento frontal de la bicolad"""

        if self.esta_vacia():
            raise Exception("La bicolad está vacía")
        dato = self.cabeza.dato
        self.cabeza = self.cabeza.siguiente
        if self.cabeza is None:
            self.final = None
        self.tamano -= 1
        return dato

    def desencolar_final(self):
        """Elimina el elemento final de la bicolad"""

        if self.esta_vacia():
            raise Exception("La bicolad está vacía")
        if self.cabeza == self.final:
            dato = self.cabeza.dato
            self.cabeza = None
            self.final = None
        else:
            actual = self.cabeza
            while actual.siguiente != self.final:
                actual = actual.siguiente
            dato = self.final.dato
            actual.siguiente = None
            self.final = actual
        self.tamano -= 1
        return dato


if __name__ == "__main__":
    # Ejemplo de uso de la Cola Estática
    cola_estatica = ColaEstatica(5)
    cola_estatica.encolar(1)
    cola_estatica.encolar(2)
    cola_estatica.encolar(3)
    print("Frente de la cola estática:", cola_estatica.ver_frente())
    print("Desencolando:", cola_estatica.desencolar())
    print("Frente de la cola estática después de desencolar:", cola_estatica.ver_frente())

    # Ejemplo de uso de la Cola Dinámica
    cola_dinamica = ColaDinamica()
    cola_dinamica.encolar(10)
    cola_dinamica.encolar(20)
    print("Frente de la cola dinámica:", cola_dinamica.ver_frente())
    print("Desencolando:", cola_dinamica.desencolar())
    print("Frente de la cola dinámica después de desencolar:", cola_dinamica.ver_frente())

    # Ejemplo de uso de la Bicolad
    bicolad = Bicolas()
    bicolad.encolar_frente(100)
    bicolad.encolar_final(200)
    print("Frente de la bicolad:", bicolad.ver_frente())
    print("Desencolando del frente:", bicolad.desencolar_frente())
    print("Desencolando del final:", bicolad.desencolar_final())