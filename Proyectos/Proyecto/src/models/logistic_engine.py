from models.structures import DoublyLinkedList, Stack, PriorityQueue, CircularQueue, UndoRedoManager

class Package:
    def __init__(self, tracking_id, priority):
        self.tracking_id = tracking_id
        self.priority = priority

class Vehicle:
    def __init__(self, plate_number):
        self.plate_number = plate_number
        # El apilamiento físico de carga utiliza una Pila (LIFO)
        self.cargo = Stack()

class Warehouse:
    def __init__(self, name):
        self.name = name
        # El inventario activo permite navegación bidireccional
        self.inventory = DoublyLinkedList()

class LogisticEngine:
    def __init__(self):
        self.warehouses = DoublyLinkedList()
        self.pending_orders = PriorityQueue()
        self.vehicle_fleet = CircularQueue()
        self.action_manager = UndoRedoManager()

    def add_warehouse(self, name):
        warehouse = Warehouse(name)
        self.warehouses.append(warehouse)
        self.action_manager.record_action({"action": "add_warehouse", "data": name})

    def register_vehicle(self, plate_number):
        vehicle = Vehicle(plate_number)
        self.vehicle_fleet.enqueue(vehicle)

    def receive_order(self, tracking_id, priority):
        package = Package(tracking_id, priority)
        self.pending_orders.enqueue(package, priority)
        self.action_manager.record_action({"action": "receive_order", "data": tracking_id})

    def dispatch_next_order(self):
        # 1. Obtener el paquete con mayor prioridad
        package = self.pending_orders.dequeue()
        if not package:
            return None
        
        # 2. Obtener el siguiente vehículo disponible (Round-Robin)
        vehicle = self.vehicle_fleet.dequeue()
        if not vehicle:
            self.pending_orders.enqueue(package, package.priority)
            return None
        
        # 3. Cargar el paquete en el vehículo (LIFO) y devolver el vehículo a la flota
        vehicle.cargo.push(package)
        self.vehicle_fleet.enqueue(vehicle)
        
        # CORRECCIÓN: Guardamos los objetos "package" y "vehicle" completos, no solo sus nombres
        self.action_manager.record_action({
            "action": "dispatch", 
            "package": package, 
            "vehicle": vehicle
        })
        
        return package, vehicle