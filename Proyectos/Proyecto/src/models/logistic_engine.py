from models.structures import DoublyLinkedList, Stack, PriorityQueue, CircularQueue, UndoRedoManager

class Package:
    def __init__(self, tracking_id, priority):
        self.tracking_id = tracking_id
        self.priority = priority

    def get_weight(self):
        """Asigna un peso espacial al paquete según su prioridad."""
        if self.priority >= 10: 
            return 10 # Prioridad máxima: Ocupa todo el camión (Cabe 1)
        elif self.priority >= 5: 
            return 2  # Prioridad media: Ocupa 2 espacios (Caben 5)
        else: 
            return 1  # Prioridad baja: Ocupa 1 espacio (Caben 10)

class Vehicle:
    """Clase para representar un vehículo que transporta paquetes."""
    def __init__(self, plate_number):
        self.plate_number = plate_number
        self.cargo = Stack()
        self.max_capacity = 10 # Capacidad tope del vehículo

    def current_load_weight(self):
        """Calcula cuánto espacio está ocupado actualmente en la pila."""
        weight = 0
        curr = self.cargo.top
        while curr:
            weight += curr.data.get_weight()
            curr = curr.next
        return weight

class Warehouse:
    """Clase para representar un almacén que contiene paquetes."""
    def __init__(self, name):
        self.name = name
        self.inventory = DoublyLinkedList()

class LogisticEngine:
    """Clase principal que maneja la lógica de la aplicación logística."""
    def __init__(self):
        self.warehouses = DoublyLinkedList()
        self.pending_orders = PriorityQueue()
        self.vehicle_fleet = CircularQueue()
        self.action_manager = UndoRedoManager()

    def add_warehouse(self, name):
        """Agrega un nuevo almacén a la lista de almacenes."""
        warehouse = Warehouse(name)
        self.warehouses.append(warehouse)
        self.action_manager.record_action({"action": "add_warehouse", "data": name})

    def register_vehicle(self, plate_number):
        """Registra un nuevo vehículo en la flota de vehículos."""
        vehicle = Vehicle(plate_number)
        self.vehicle_fleet.enqueue(vehicle)

    def receive_order(self, tracking_id, priority):
        """Recibe un nuevo pedido y lo agrega a la cola de pedidos pendientes."""
        package = Package(tracking_id, priority)
        self.pending_orders.enqueue(package, priority)
        self.action_manager.record_action({"action": "receive_order", "data": tracking_id})

    def dispatch_next_order(self):
        """Despacha el siguiente pedido pendiente a un vehículo disponible."""
        package = self.pending_orders.dequeue()
        if not package:
            return {"status": "error", "message": "No hay paquetes en cola."}
        
        if self.vehicle_fleet._size == 0:
            self.pending_orders.enqueue(package, package.priority)
            return {"status": "error", "message": "No hay vehículos registrados."}

        suitable_vehicle = None # Variable para almacenar el vehículo adecuado
        package_weight = package.get_weight()

        # Recorremos la cola circular usando punteros en lugar de dequeue/enqueue para no desincronizar
        current_node = self.vehicle_fleet.tail.next # Empezamos por la cabeza (el que lleva más tiempo esperando)
        start_node = current_node
        
        while True:
            vehicle = current_node.data
            
            # Verificamos si este vehículo tiene espacio suficiente
            if vehicle.current_load_weight() + package_weight <= vehicle.max_capacity:
                suitable_vehicle = vehicle
                break
                
            current_node = current_node.next
            if current_node == start_node:
                # Dimos una vuelta completa y ningún camión tiene espacio
                break

        if suitable_vehicle:
            # Encontramos un vehículo con espacio, cargamos el paquete
            suitable_vehicle.cargo.push(package)
            
            # Para respetar el Round-Robin, hacemos que el vehículo que acaba de recibir carga
            # pase al final de la cola circular (moviendo el puntero 'tail' hacia él)
            # Esto asegura que el siguiente paquete se intente asignar al siguiente camión libre.
            while self.vehicle_fleet.tail.data != suitable_vehicle: 
                self.vehicle_fleet.tail = self.vehicle_fleet.tail.next
            
            self.action_manager.record_action({
                "action": "dispatch", 
                "package": package, 
                "vehicle": suitable_vehicle
            })
            return {"status": "success", "package": package, "vehicle": suitable_vehicle}
        else:
            # Ningún vehículo tiene espacio, devolvemos el paquete a la zona de pendientes
            self.pending_orders.enqueue(package, package.priority)
            return ({"status": "error", "message": "Todos los vehículos están llenos o no tienen capacidad para este paquete."})