# controllers/app_controller.py
from models.logistic_engine import LogisticEngine

class AppController:
    def __init__(self, page):
        self.page = page
        self.engine = LogisticEngine()
        
    def add_warehouse(self, name):
        if name:
            self.engine.add_warehouse(name)
            self.page.update()
        
    def add_vehicle(self, plate_number):
        if plate_number:
            self.engine.register_vehicle(plate_number)
            self.page.update()

    def add_order(self, tracking_id, priority):
        if tracking_id and priority:
            self.engine.receive_order(tracking_id, int(priority))
            self.page.update()

    def dispatch_order(self):
        result = self.engine.dispatch_next_order()
        # El motor ya registra la acción internamente en dispatch_next_order
        self.page.update()

    def undo_action(self):
        action_dict = self.engine.action_manager.undo()
        if action_dict:
            # Lógica real para revertir un despacho
            if action_dict.get("action") == "dispatch":
                package = action_dict.get("package")
                vehicle = action_dict.get("vehicle")
                
                # Revertimos: sacamos el paquete de la pila (LIFO) del vehículo
                popped_pkg = vehicle.cargo.pop()
                if popped_pkg:
                    # Lo devolvemos a la cola de prioridad
                    self.engine.pending_orders.enqueue(popped_pkg, popped_pkg.priority)
                    print(f"Deshecho: Paquete {popped_pkg.tracking_id} devuelto a la cola.")
            self.page.update()

    def redo_action(self):
        action_dict = self.engine.action_manager.redo()
        if action_dict:
            # Lógica real para rehacer un despacho
            if action_dict.get("action") == "dispatch":
                package = action_dict.get("package")
                vehicle = action_dict.get("vehicle")
                
                # 1. Eliminar el paquete de la cola de pedidos pendientes (PriorityQueue)
                current = self.engine.pending_orders.head
                prev = None
                while current:
                    # Comparamos si el nodo actual contiene el paquete que queremos rehacer
                    if current.data["data"] == package:
                        if prev:
                            prev.next = current.next
                        else:
                            self.engine.pending_orders.head = current.next
                        self.engine.pending_orders._size -= 1
                        break
                    prev = current
                    current = current.next
                
                # 2. Volver a cargar el paquete en la pila del vehículo
                vehicle.cargo.push(package)
                print(f"Rehecho: Paquete {package.tracking_id} cargado nuevamente.")
        self.page.update()