""" ADT Conjunto Estático
Ejemplo de implementación de un conjunto estático en Python.

Autor: Gabriel Romulo Arnez Joven

Registro: 220000417

Materia: Estructura de Datos 1

Profesor: Ing. Juan Carlos Peinado Pereira

Fecha: 30/08/2026 """

class NodoPolinomio:
    """Clase que representa un nodo de un polinomio."""

    def __init__(self, coeficiente: float, exponente: int):
        self.coeficiente = coeficiente
        self.exponente = exponente
        self.siguiente = None

class Polinomio:
    """ADT polinomio respaldado por una lista de coeficientes."""

    def __init__(self):
        self.cabeza = None

    def agregar_termino(self, coeficiente, exponente):
        """Agrega un término al polinomio."""
        nuevo_nodo = NodoPolinomio(coeficiente, exponente)
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            anterior = None
            while actual is not None and actual.exponente > exponente:
                anterior = actual
                actual = actual.siguiente
            if anterior is None:
                nuevo_nodo.siguiente = self.cabeza
                self.cabeza = nuevo_nodo
            else:
                anterior.siguiente = nuevo_nodo
                nuevo_nodo.siguiente = actual
        
    def __str__(self):
        """Devuelve una representación en cadena del polinomio."""
        if self.cabeza is None:
            return "0"

        resultado = ""
        actual = self.cabeza
        while actual is not None:
            if actual.coeficiente != 0: # Ignorar términos con coeficiente 0
                resultado += "+"
            if actual.coeficiente == -1 and actual.exponente != 0:
                resultado += "-"
            elif actual.coeficiente != 1 or actual.exponente == 0:
                resultado += str(actual.coeficiente)
            if actual.exponente > 0:
                resultado += "x"
                if actual.exponente > 1:
                    resultado += "^" + str(actual.exponente)
            actual = actual.siguiente
        return resultado if resultado else "0"
        
# Ejemplo de uso

if __name__ == "__main__":
    p = Polinomio()
    p.agregar_termino(2, 3)
    p.agregar_termino(-1, 2)
    p.agregar_termino(5, 0)
    print(p)

    