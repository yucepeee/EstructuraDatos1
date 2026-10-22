from models.logistic_engine import LogisticEngine
from models.structures import CircularDoublyLinkedList
import flet as ft
import time 

class AppController:
    def __init__(self, page):
        
        self.page = page
        self.engine = LogisticEngine()
        self.engine.warehouses = CircularDoublyLinkedList()
        
        self.current_truck_node = None # Puntero para rastrear en qué almacén está el camión actualmente en la animación
        
        # Contador total de operaciones 
        self.operation_count = 0 
        
        # Variables de rendimiento para el panel en tiempo real
        self.last_action_type = None  # Tipo de acción ("insert", "traverse", "stack")
        self.last_exec_time = 0.0     # Tiempo de CPU medido en milisegundos
        self.last_steps = 0           # Conteo de pasos algorítmicos ejecutados
        
    def _measure_time(self, action_type, steps_taken, func, *args):
        """
        Función envoltorio (wrapper) para medir el tiempo de ejecución en milisegundos 
        de cualquier operación sobre las estructuras de datos y actualizar las métricas.
        """
        start = time.perf_counter()
        result = func(*args)
        end = time.perf_counter()

        self.last_exec_time = (end - start) * 1000 
        self.last_action_type = action_type
        self.last_steps = steps_taken 
        self.operation_count += 1
        return result

    def add_warehouse(self, name):
        """
        Agrega un nuevo almacén a la lista circular de la red logística.
        """
        if name:
            self._measure_time("insert", 1, self.engine.warehouses.append, name)
            # Si es el primer almacén, posicionamos el camión de ruta allí
            if not self.current_truck_node:
                self.current_truck_node = self.engine.warehouses.head
            
    def has_dispatched_vehicles(self):
        """
        Método auxiliar que recorre la cola circular de vehículos para verificar 
        si al menos uno ha alcanzado su capacidad máxima (está despachado).
        """
        if not self.engine.vehicle_fleet.tail: 
            return False
        curr = self.engine.vehicle_fleet.tail.next
        start = curr
        while True:
            if curr.data.current_load_weight() >= curr.data.max_capacity:
                return True
            curr = curr.next
            if curr == start:
                break
        return False

    def _empty_dispatched_vehicles(self):
        """
        Vacía la carga (pila LIFO) de los vehículos despachados cuando completan 
        una vuelta entera a la ruta circular, simulando la entrega exitosa.
        """
        if not self.engine.vehicle_fleet.tail: 
            return
        curr = self.engine.vehicle_fleet.tail.next
        start = curr
        while True:
            vehicle = curr.data
            if vehicle.current_load_weight() >= vehicle.max_capacity:
                # Extraemos los paquetes uno por uno hasta vaciar la pila
                while vehicle.cargo.top:
                    vehicle.cargo.pop()
            curr = curr.next
            if curr == start:
                break

    def advance_route(self):
        """
        Avanza el camión al siguiente almacén en la lista circular. 
        Si no hay camiones con carga completa, el código no hace nada.
        """
        # Acción incorrecta: Intentar avanzar sin camiones despachados -> No hace nada
        if not self.has_dispatched_vehicles():
            return

        if self.current_truck_node and self.current_truck_node.next:
            start_time = time.perf_counter()
            
            # Movemos el puntero al nodo siguiente
            self.current_truck_node = self.current_truck_node.next
            
            # Si el puntero regresa al inicio (head), se completó una vuelta
            if self.current_truck_node == self.engine.warehouses.head:
                self._empty_dispatched_vehicles()
                
            self.last_exec_time = (time.perf_counter() - start_time) * 1000
            self.last_action_type = "traverse"
            self.last_steps = 1
            self.operation_count += 1

    def add_vehicle(self, plate_number):
        """
        Registra un nuevo vehículo en la cola circular de la flota.
        """
        if plate_number:
            self._measure_time("insert", 1, self.engine.register_vehicle, plate_number)

    def add_order(self, tracking_id, priority):
        """
        Ingresa un nuevo pedido a la cola de prioridad del motor.
        """
        if tracking_id and priority:
            current_size = self.engine.pending_orders._size
            pasos_estimados = current_size + 1 if current_size > 0 else 1
            self._measure_time("insert", pasos_estimados, self.engine.receive_order, tracking_id, int(priority))

    def dispatch_order(self):
        """
        Despacha el siguiente pedido urgente asignándolo al camión con espacio disponible. 
        Si falla (no hay paquetes o camiones llenos), el código no hace nada.
        """
        pasos_estimados = self.engine.vehicle_fleet._size + 1 if self.engine.vehicle_fleet._size > 0 else 1
        result = self._measure_time("stack", pasos_estimados, self.engine.dispatch_next_order)
        
        # Si el motor devuelve un error, simplemente ignoramos la acción (no hace nada)
        if result and result.get("status") == "error":
            return

    def undo_action(self):
        """
        Llama al gestor de historial para revertir la última acción de despacho.
        """
        self._measure_time("stack", 2, self._undo_logic)

    def _undo_logic(self):
        """
        Lógica interna que extrae el paquete de la pila del camión y lo devuelve a la cola.
        """
        action_dict = self.engine.action_manager.undo()
        if action_dict and action_dict.get("action") == "dispatch":
            vehicle = action_dict.get("vehicle")
            popped_pkg = vehicle.cargo.pop()
            if popped_pkg:
                self.engine.pending_orders.enqueue(popped_pkg, popped_pkg.priority)

    def redo_action(self):
        """
        Llama al gestor de historial para reaplicar un despacho deshecho.
        """
        pasos = self.engine.pending_orders._size + 1
        self._measure_time("stack", pasos, self._redo_logic)

    def _redo_logic(self):
        """
        Lógica interna que busca el paquete en la cola, lo desenlaza y lo vuelve a apilar en el camión.
        """
        action_dict = self.engine.action_manager.redo()
        if action_dict and action_dict.get("action") == "dispatch":
            package = action_dict.get("package")
            vehicle = action_dict.get("vehicle")
            
            # Buscamos y removemos el paquete de la cola de pendientes
            current = self.engine.pending_orders.head
            prev = None
            while current:
                if current.data["data"] == package:
                    if prev:
                        prev.next = current.next
                    else:
                        self.engine.pending_orders.head = current.next
                    self.engine.pending_orders._size -= 1
                    break
                prev = current
                current = current.next
                
            # Vuelve a empujar a la pila del camión
            vehicle.cargo.push(package)