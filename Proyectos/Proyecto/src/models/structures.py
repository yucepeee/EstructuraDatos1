class Node:
    """Clase para representar un nodo en una lista enlazada."""
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    """Clase para representar una lista doblemente enlazada."""
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0

    # Inserción al final 
    def append(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.prev = self.tail
            self.tail.next = new_node
            self.tail = new_node
        self._size += 1

    # Inserción al inicio 
    def prepend(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self._size += 1

    # Eliminación por valor 
    def remove(self, data):
        current = self.head
        while current:
            if current.data == data:
                if current.prev:
                    current.prev.next = current.next
                else:
                    self.head = current.next
                if current.next:
                    current.next.prev = current.prev
                else:
                    self.tail = current.prev
                self._size -= 1
                return True
            current = current.next
        return False

    # Búsqueda 
    def search(self, data):
        current = self.head
        while current:
            if current.data == data:
                return current
            current = current.next
        return None

class Stack:
    """Clase para representar una pila utilizando una lista enlazada."""
    def __init__(self):
        self.top = None
        self._size = 0

    def push(self, data):
        """Agrega un elemento a la pila."""
        new_node = Node(data)
        if self.top:
            new_node.next = self.top
        self.top = new_node
        self._size += 1

    def pop(self):
        """Elimina y devuelve el elemento superior de la pila."""
        if not self.top:
            return None
        value = self.top.data
        self.top = self.top.next
        self._size -= 1
        return value

    def is_empty(self):
        """Verifica si la pila está vacía."""
        return self.top is None

class UndoRedoManager:
    """Clase para gestionar las operaciones de deshacer y rehacer."""
    def __init__(self):
        self.undo_stack = Stack()
        self.redo_stack = Stack()

    def record_action(self, action_data):
        """Registra una nueva acción y limpia la pila de rehacer."""
        self.undo_stack.push(action_data)
        self.redo_stack = Stack() # Se reinicia el historial de 'redo' al realizar una nueva acción

    def undo(self):
        """Deshace la última acción y la mueve a la pila de rehacer."""
        if not self.undo_stack.is_empty():
            action = self.undo_stack.pop()
            self.redo_stack.push(action)
            return action
        return None

    def redo(self):
        """Rehace la última acción deshecha y la mueve de vuelta a la pila de deshacer."""
        if not self.redo_stack.is_empty():
            action = self.redo_stack.pop()
            self.undo_stack.push(action)
            return action
        return None


class CircularQueue:
    """Clase para representar una cola circular utilizando una lista enlazada."""
    def __init__(self):
        self.tail = None 
        self._size = 0

    def enqueue(self, data):
        """Agrega un elemento a la cola circular."""
        new_node = Node(data)
        if not self.tail:
            self.tail = new_node
            self.tail.next = self.tail # Apunta a sí mismo cerrando el círculo
        else:
            new_node.next = self.tail.next # El nuevo nodo apunta al primero
            self.tail.next = new_node      # El último actual apunta al nuevo
            self.tail = new_node           # El nuevo nodo es ahora el último
        self._size += 1

    def dequeue(self):
        """Elimina y devuelve el elemento al frente de la cola circular."""
        if not self.tail:
            return None
        
        head = self.tail.next # El primero es el siguiente del último
        value = head.data
        
        if self.tail == head: # Si solo hay un elemento
            self.tail = None
        else:
            self.tail.next = head.next # El último ahora apunta al segundo nodo
            self.tail = head.next      # El segundo nodo es ahora el último
        self._size -= 1
        return value

class PriorityQueue:
    """Clase para representar una cola de prioridad utilizando una lista enlazada."""
    def __init__(self):
        self.head = None
        self._size = 0

    def enqueue(self, data, priority):
        """Agrega un elemento a la cola de prioridad según su prioridad."""
        new_node = Node({"data": data, "priority": priority})
        if not self.head or priority > self.head.data["priority"]:
            new_node.next = self.head
            self.head = new_node
        else:
            current = self.head
            while current.next and current.next.data["priority"] >= priority:
                current = current.next
            new_node.next = current.next
            current.next = new_node
        self._size += 1

    def dequeue(self):
        """Elimina y devuelve el elemento con la mayor prioridad."""
        if not self.head:
            return None
        value = self.head.data["data"]
        self.head = self.head.next
        self._size -= 1
        return value