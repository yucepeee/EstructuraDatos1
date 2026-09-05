""" ADT Conjunto Estático
Ejemplo de implementación de un conjunto estático en Python.

Autor: Gabriel Romulo Arnez Joven

Registro: 220000417

Materia: Estructura de Datos 1

Profesor: Ing. Juan Carlos Peinado Pereira

Fecha: 30/08/2026 """


class Conjunto:
    """ADT conjunto respaldado por un arreglo de capacidad fija."""

    def __init__(self, capacidad):
        """Inicializa un conjunto vacío con una capacidad fija."""

        if not isinstance(capacidad, int) or capacidad < 0:
            raise ValueError("La capacidad debe ser un entero mayor o igual a cero")

        self.capacidad = capacidad
        self.elementos = []

    def agregar(self, elemento):
        """Agrega un elemento al conjunto si no está presente y hay capacidad."""

        if elemento in self.elementos:
            return
        if len(self.elementos) >= self.capacidad:
            raise OverflowError("El conjunto alcanzó su capacidad máxima")
        self.elementos.append(elemento)

    def eliminar(self, elemento):
        """Elimina un elemento del conjunto si está presente."""

        if elemento in self.elementos:
            self.elementos.remove(elemento)

    def union(self, otro):
        """Devuelve un nuevo conjunto con los elementos de ambos conjuntos."""

        resultado = Conjunto(self.capacidad + otro.capacidad)
        for elemento in self.elementos + otro.elementos:
            resultado.agregar(elemento)
        return resultado

    def interseccion(self, otro):
        """Devuelve un nuevo conjunto con los elementos comunes."""

        resultado = Conjunto(min(self.capacidad, otro.capacidad))
        for elemento in self.elementos:
            if elemento in otro.elementos:
                resultado.agregar(elemento)
        return resultado

    def diferencia(self, otro):
        """Devuelve los elementos de este conjunto que no están en otro."""

        resultado = Conjunto(self.capacidad)
        for elemento in self.elementos:
            if elemento not in otro.elementos:
                resultado.agregar(elemento)
        return resultado

    def diferencia_simetrica(self, otro):
        """Devuelve los elementos que pertenecen a un solo conjunto."""

        return self.diferencia(otro).union(otro.diferencia(self))

    def subconjunto(self, otro):
        """Devuelve True si todos los elementos de este conjunto están en otro."""

        return all(elemento in otro.elementos for elemento in self.elementos)

    def igual(self, otro):
        """Devuelve True si ambos conjuntos contienen los mismos elementos."""

        return len(self) == len(otro) and self.subconjunto(otro)

    def vacio(self):
        """Devuelve True si el conjunto no contiene elementos."""

        return len(self.elementos) == 0

    def tamaño(self):
        """Devuelve la cantidad de elementos del conjunto."""

        return len(self.elementos)

    def pertenece(self, elemento):
        """Devuelve True si el elemento pertenece al conjunto."""

        return elemento in self.elementos

    def contiene(self, elemento):
        """Devuelve True si el conjunto contiene el elemento."""

        return self.pertenece(elemento)

    def __len__(self):
        return len(self.elementos)

    def __str__(self):
        """Devuelve una representación en cadena del conjunto."""

        return "{" + ", ".join(str(e) for e in self.elementos) + "}"

if __name__ == "__main__":

    # Ejemplo de uso del ADT Conjunto Estático
    
    conjunto_1 = Conjunto(5)
    conjunto_1.agregar(1)
    conjunto_1.agregar(2)
    conjunto_1.agregar(3)

    conjunto_2 = Conjunto(5)
    conjunto_2.agregar(3)
    conjunto_2.agregar(4)
    conjunto_2.agregar(5)

    print("A:", conjunto_1)
    print("B:", conjunto_2)
    print("A unión B:", conjunto_1.union(conjunto_2))
    print("A intersección B:", conjunto_1.interseccion(conjunto_2))
    print("A diferencia B:", conjunto_1.diferencia(conjunto_2))