import unittest
from models.structures import DoublyLinkedList, Stack, PriorityQueue, CircularQueue

class TestDataStructures(unittest.TestCase):

    def test_doubly_linked_list(self):
        dll = DoublyLinkedList()
        # Caso límite: lista vacía
        self.assertFalse(dll.remove("Inexistente"))
        
        # Inserción y validación de punteros
        dll.append("A")
        dll.append("B")
        dll.append("C")
        
        # Probar eliminación intermedia (verificando que no se pierdan referencias)
        dll.remove("B")
        self.assertEqual(dll.head.data, "A")
        self.assertEqual(dll.head.next.data, "C")
        self.assertEqual(dll.tail.prev.data, "A")

    def test_priority_queue(self):
        pq = PriorityQueue()
        # Mayor número = mayor prioridad
        pq.enqueue("Normal", 1)
        pq.enqueue("VIP", 5)
        pq.enqueue("Médico", 10)
        
        # Debe salir el de mayor prioridad primero
        self.assertEqual(pq.dequeue(), "Médico")
        self.assertEqual(pq.dequeue(), "VIP")
        self.assertEqual(pq.dequeue(), "Normal")

    def test_circular_queue(self):
        cq = CircularQueue()
        # Caso límite: cola vacía
        self.assertIsNone(cq.dequeue())
        
        cq.enqueue("Vehiculo 1")
        cq.enqueue("Vehiculo 2")
        
        # En una cola FIFO, debe salir el primero que entró
        self.assertEqual(cq.dequeue(), "Vehiculo 1")
        self.assertEqual(cq.dequeue(), "Vehiculo 2")

if __name__ == '__main__':
    unittest.main()