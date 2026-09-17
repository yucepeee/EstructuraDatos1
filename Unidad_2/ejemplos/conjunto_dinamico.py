""" ADT Conjunto Estático
Ejemplo de implementación de un conjunto estático en Python.

Autor: Gabriel Romulo Arnez Joven

Registro: 220000417

Materia: Estructura de Datos 1

Profesor: Ing. Juan Carlos Peinado Pereira

Fecha: 30/08/2026 """

class Conjunto_Dinamico:
    """ADT conjunto respaldado por una lista dinámica."""

    def __init__(self):
        """Inicializa un conjunto vacío con capacidad dinámica."""
        self.elementos = []

    def agregar(self, elemento):
        """Agrega un elemento al conjunto si no está presente."""
        if elemento not in self.elementos:
            self.elementos.append(elemento)

    def eliminar(self, elemento):
        """Elimina un elemento del conjunto si está presente."""
        if elemento in self.elementos:
            self.elementos.remove(elemento)

    def union(self, otro):
        """Devuelve un nuevo conjunto con los elementos de ambos conjuntos."""
        resultado = Conjunto_Dinamico()
        for elemento in self.elementos + otro.elementos:
            resultado.agregar(elemento)
        return resultado

    def interseccion(self, otro):
        """Devuelve un nuevo conjunto con los elementos comunes."""
        resultado = Conjunto_Dinamico()
        for elemento in self.elementos:
            if elemento in otro.elementos:
                resultado.agregar(elemento)
        return resultado

    def diferencia(self, otro):
        """Devuelve los elementos de este conjunto que no están en otro."""
        resultado = Conjunto_Dinamico()
        for elemento in self.elementos:
            if elemento not in otro.elementos:
                resultado.agregar(elemento)
        return resultado

    def __str__(self):
        """Devuelve una representación en cadena del conjunto."""
        return "{" + ", ".join(str(e) for e in self.elementos) + "}"

if __name__ == "__main__":

    # Ejemplo de uso del ADT Conjunto Dinámico
    
    conjunto1 = Conjunto_Dinamico()
    conjunto1.agregar(1)
    conjunto1.agregar(2)
    conjunto1.agregar(3)

    conjunto2 = Conjunto_Dinamico()
    conjunto2.agregar(3)
    conjunto2.agregar(4)
    conjunto2.agregar(5)

    print("Conjunto 1:", conjunto1)
    print("Conjunto 2:", conjunto2)

    union = conjunto1.union(conjunto2)
    print("Unión:", union)

    interseccion = conjunto1.interseccion(conjunto2)
    print("Intersección:", interseccion)

    diferencia = conjunto1.diferencia(conjunto2)
    print("Diferencia (conjunto1 - conjunto2):", diferencia)