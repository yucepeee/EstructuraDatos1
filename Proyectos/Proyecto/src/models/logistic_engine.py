from models.structures import DoublyLinkedList, Stack, PriorityQueue, CircularQueue, UndoRedoManager

class Package:
    """Clase que representa un paquete o pedido individual que ingresa al sistema logístico."""
    def __init__(self, tracking_id, priority):
        self.tracking_id = tracking_id  # Identificador único de seguimiento del paquete
        self.priority = priority        # Nivel de urgencia o prioridad numérica del pedido

    def get_weight(self):
        """Calcula y retorna el peso espacial o volumen que ocupa el paquete según su prioridad."""
        if self.priority >= 10: 
            return 10  # Prioridad máxima: Ocupa todo el camión por completo (cabe 1)
        elif self.priority >= 5: 
            return 2   # Prioridad media: Ocupa 2 espacios (caben hasta 5 paquetes)
        else: 
            return 1   # Prioridad baja: Ocupa 1 espacio (caben hasta 10 paquetes)

class Vehicle:
    """Clase para representar un camión de transporte que traslada la carga de paquetes."""
    def __init__(self, plate_number):
        self.plate_number = plate_number  # Número de placa identificador del vehículo
        self.cargo = Stack()              # Pila (LIFO) interna para apilar físicamente los paquetes
        self.max_capacity = 10            # Capacidad tope de peso soportada por el camión

    def current_load_weight(self):
        """Recorre la pila de carga para calcular cuánto espacio está ocupado actualmente en el camión."""
        weight = 0
        curr = self.cargo.top
        while curr:
            weight += curr.data.get_weight()
            curr = curr.next
        return weight

class Warehouse:
    """Clase para representar un centro de distribución o almacén en la red logística."""
    def __init__(self, name):
        self.name = name                # Nombre identificador del almacén
        self.inventory = DoublyLinkedList()  # Lista doblemente enlazada para el inventario activo

class LogisticEngine:
    """Clase principal (Modelo) que centraliza las estructuras de datos y la lógica del negocio."""
    def __init__(self):
        self.warehouses = DoublyLinkedList()  # Red de almacenes mediante lista doblemente enlazada
        self.pending_orders = PriorityQueue() # Cola de prioridad para procesar pedidos urgentes primero
        self.vehicle_fleet = CircularQueue()  # Cola circular para la gestión equitativa de camiones (Round-Robin)
        self.action_manager = UndoRedoManager() # Gestor de historial basado en dos pilas para deshacer/rehacer

    def add_warehouse(self, name):
        """Crea un nuevo almacén y lo agrega al final de la lista de almacenes."""
        warehouse = Warehouse(name)
        self.warehouses.append(warehouse)
        self.action_manager.record_action({"action": "add_warehouse", "data": name})

    def register_vehicle(self, plate_number):
        """Registra un nuevo vehículo y lo encola al final de la flota circular."""
        vehicle = Vehicle(plate_number)
        self.vehicle_fleet.enqueue(vehicle)

    def receive_order(self, tracking_id, priority):
        """Recibe un nuevo pedido, crea el paquete y lo encola ordenadamente según su prioridad."""
        package = Package(tracking_id, priority)
        self.pending_orders.enqueue(package, priority)
        self.action_manager.record_action({"action": "receive_order", "data": tracking_id})

    def dispatch_next_order(self):
        """Extrae el pedido más urgente y lo asigna al primer vehículo disponible con espacio suficiente."""
        package = self.pending_orders.dequeue()
        if not package:
            return {"status": "error", "message": "No hay paquetes en cola."}
        
        if self.vehicle_fleet._size == 0:
            self.pending_orders.enqueue(package, package.priority)
            return {"status": "error", "message": "No hay vehículos registrados."}

        suitable_vehicle = None  # Almacenará el camión apto seleccionado
        package_weight = package.get_weight()

        # Recorremos la cola circular mediante punteros para inspeccionar la flota completa
        current_node = self.vehicle_fleet.tail.next  # Apunta al inicio (head) de la cola circular
        start_node = current_node
        
        while True:
            vehicle = current_node.data
            
            # Verificamos si la carga actual sumada al nuevo paquete no excede el límite
            if vehicle.current_load_weight() + package_weight <= vehicle.max_capacity:
                suitable_vehicle = vehicle
                break
                
            current_node = current_node.next
            if current_node == start_node:
                # Dimos la vuelta completa al círculo y ningún camión tiene espacio
                break

        if suitable_vehicle:
            # Apilamos el paquete en la carga del vehículo seleccionado
            suitable_vehicle.cargo.push(package)
            
            # Rotamos el puntero 'tail' de la cola circular para aplicar el turno Round-Robin
            while self.vehicle_fleet.tail.data != suitable_vehicle: 
                self.vehicle_fleet.tail = self.vehicle_fleet.tail.next
            
            # Registramos la acción en el historial de deshacer/rehacer
            self.action_manager.record_action({"action": "dispatch", "package": package, "vehicle": suitable_vehicle
            })
            return {"status": "success", "package": package, "vehicle": suitable_vehicle}
        else:
            # Si ningún camión tiene espacio, devolvemos el paquete a la cola de pendientes
            self.pending_orders.enqueue(package, package.priority)
            return {"status": "error", "message": "Todos los vehículos están llenos o no tienen capacidad para este paquete."}