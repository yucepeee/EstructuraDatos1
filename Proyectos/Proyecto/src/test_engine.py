import unittest
from models.logistic_engine import LogisticEngine

class TestLogisticEngine(unittest.TestCase):
    def setUp(self):
        # Este método se ejecuta antes de cada prueba para darnos un motor "limpio"
        self.engine = LogisticEngine()

    def test_flujo_despacho_completo(self):
        # 1. Registrar vehículos
        self.engine.register_vehicle("CAMION-1")
        self.engine.register_vehicle("CAMION-2")
        
        # 2. Recibir pedidos con diferentes prioridades
        self.engine.receive_order("PKG-BAJA-1", 1)
        self.engine.receive_order("PKG-ALTA", 10)
        self.engine.receive_order("PKG-MEDIA", 5)

        # 3. Despachar el primer pedido
        result1 = self.engine.dispatch_next_order()
        self.assertEqual(result1["status"], "success")
        # El de prioridad 10 debió salir primero y asignarse al CAMION-1
        self.assertEqual(result1["package"].tracking_id, "PKG-ALTA")
        self.assertEqual(result1["vehicle"].plate_number, "CAMION-1")

        # 4. Despachar el segundo pedido
        result2 = self.engine.dispatch_next_order()
        self.assertEqual(result2["status"], "success")
        # El de prioridad 5 debió salir segundo y asignarse al CAMION-2 (Round-Robin)
        self.assertEqual(result2["package"].tracking_id, "PKG-MEDIA")
        self.assertEqual(result2["vehicle"].plate_number, "CAMION-2")

    def test_limite_peso_vehiculo(self):
        # Registramos un solo vehículo
        self.engine.register_vehicle("CAMION-SOLO")
        
        # Agregamos dos paquetes de prioridad máxima (ocupan 10 de espacio cada uno)
        self.engine.receive_order("PKG-MAX-1", 10)
        self.engine.receive_order("PKG-MAX-2", 10)

        # El primer paquete debe entrar sin problemas
        res1 = self.engine.dispatch_next_order()
        self.assertEqual(res1["status"], "success")

        # El segundo paquete debe ser rechazado porque el camión ya está lleno
        res2 = self.engine.dispatch_next_order()
        self.assertEqual(res2["status"], "error")
        self.assertIn("llenos", res2["message"])

    def test_deshacer_rehacer(self):
        self.engine.register_vehicle("CAMION-UNDO")
        self.engine.receive_order("PKG-1", 5)
        
        # Despachamos
        self.engine.dispatch_next_order()
        
        # Deshacemos (Simulando lo que hace el AppController en la interfaz)
        action = self.engine.action_manager.undo()
        self.assertIsNotNone(action)
        self.assertEqual(action["action"], "dispatch")
        
        # Extraemos el paquete del vehículo y lo devolvemos a la cola
        vehiculo = action["vehicle"]
        paquete_recuperado = vehiculo.cargo.pop()
        if paquete_recuperado:
            self.engine.pending_orders.enqueue(paquete_recuperado, paquete_recuperado.priority)
        
        # Verificamos que el paquete efectivamente volvió a la cola
        self.assertEqual(self.engine.pending_orders._size, 1)

if __name__ == '__main__':
    unittest.main()