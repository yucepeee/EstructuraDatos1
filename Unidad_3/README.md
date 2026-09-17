# Unidad III: ADT Listas Simples Enlazadas

Este proyecto presenta una implementación básica de una lista simplemente enlazada en Python, desarrollada como ejemplo académico para la unidad de estructuras de datos.

## Descripción

Una lista enlazada es una estructura de datos lineal compuesta por nodos. Cada nodo almacena:

- un valor o dato
- una referencia al siguiente nodo

Esto permite agregar, eliminar y recorrer elementos de forma dinámica sin necesidad de reservar un arreglo fijo.

## Objetivo

El objetivo de este ejemplo es enseñar cómo se implementa una lista simple enlazada y cómo funcionan las operaciones básicas sobre ella.

## Funcionalidades implementadas

- Crear nodos
- Agregar elementos al final
- Eliminar elementos por valor
- Buscar un dato
- Insertar un elemento en una posición determinada
- Obtener un dato por posición
- Recorrer e imprimir la lista
- Consultar el tamaño actual de la lista

## Estructura del código

El archivo principal contiene dos clases principales:

- `Nodo`: representa cada elemento de la lista
- `Lista`: maneja la lógica de la estructura y sus operaciones

## Ejemplo de uso

```python
if __name__ == "__main__":
    lista = Lista()
    lista.agregar(1)
    lista.agregar(2)
    lista.agregar(3)
    lista.imprimir()  # Lista: [1, 2, 3]
    print(lista.buscar(2))  # True
    print(lista.eliminar(2))  # True
    lista.imprimir()  # Lista: [1, 3]
    print(lista.tamano)  # 2
    lista.insertar(4, 1)
    lista.imprimir()  # Lista: [1, 4, 3]
```

## Resultado esperado

```python
Lista: [1, 2, 3]
True
True
Lista: [1, 3]
2
Lista: [1, 4, 3]
```

## Autor

- Gabriel Romulo Arnez Joven
- Registro: 220000417

## Materia

- Estructura de Datos 1

## Profesor

- Ing. Juan Carlos Peinado Pereira

## Nota

Este repositorio tiene un enfoque académico y sirve como material de estudio para comprender el funcionamiento de listas enlazadas en Python.