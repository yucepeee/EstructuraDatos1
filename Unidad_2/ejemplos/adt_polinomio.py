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
        actual = self.cabeza
        resultado = ""
        while actual is not None:
            if actual.coeficiente != 0:
                if actual.coeficiente > 0 and resultado != "":
                    resultado += " + "
                elif actual.coeficiente < 0:
                    resultado += " - "
                resultado += f"{abs(actual.coeficiente)}x^{actual.exponente}"
            actual = actual.siguiente
        return resultado

    # Conversor de expresiones a notación prefija y postfija

    def prefija(self):
        """Devuelve el polinomio usando notación prefija."""
        if self.cabeza is None:
            return "0"

        terminos = []
        actual = self.cabeza
        while actual is not None:
            if actual.coeficiente != 0:
                if actual.exponente == 0:
                    terminos.append(str(actual.coeficiente))
                else:
                    terminos.append(
                        f"* {actual.coeficiente} x^{actual.exponente}"
                    )
            actual = actual.siguiente

        if not terminos:
            return "0"

        resultado = terminos[0]
        for termino in terminos[1:]:
            resultado = f"+ {resultado} {termino}"
        return resultado

    def postfija(self):
        """Devuelve el polinomio usando notación postfija."""
        if self.cabeza is None:
            return "0"

        terminos = []
        actual = self.cabeza
        while actual is not None:
            if actual.coeficiente != 0:
                if actual.exponente == 0:
                    terminos.append(str(actual.coeficiente))
                else:
                    terminos.append(
                        f"{actual.coeficiente} x^{actual.exponente} *"
                    )
            actual = actual.siguiente

        if not terminos:
            return "0"

        resultado = terminos[0]
        for termino in terminos[1:]:
            resultado = f"{resultado} {termino} +"
        return resultado

# Ejemplo de uso

if __name__ == "__main__":
    p = Polinomio()
    p.agregar_termino(2, 3)
    p.agregar_termino(-1, 2)
    p.agregar_termino(5, 0)
    print(p)
    print(p.prefija())
    print(p.postfija())