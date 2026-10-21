from models.logistic_engine import LogisticEngine
from models.structures import CircularDoublyLinkedList
import flet as ft
import time 

class AppController:
    def __init__(self, page):
        self.page = page
        self.engine = LogisticEngine()
        self.engine.warehouses = CircularDoublyLinkedList()
        self.current_truck_node = None 
        self.operation_count = 0 
        
        self.last_action_type = None 
        self.last_exec_time = 0.0 
        self.last_steps = 0 
        
    def show_message(self, message, is_error=False):
        color = ft.Colors.RED_700 if is_error else ft.Colors.GREEN_700
        snack = ft.SnackBar(content=ft.Text(message, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD), bgcolor=color)
        try:
            self.page.open(snack)
        except AttributeError:
            self.page.snack_bar = snack
            self.page.snack_bar.open = True
            self.page.update()
            
    def _measure_time(self, action_type, steps_taken, func, *args):
        start = time.perf_counter()
        result = func(*args)
        end = time.perf_counter()
        
        self.last_exec_time = (end - start) * 1000 
        self.last_action_type = action_type
        self.last_steps = steps_taken 
        self.operation_count += 1
        return result

    def add_warehouse(self, name):
        if name:
            self._measure_time("insert", 1, self.engine.warehouses.append, name)
            if not self.current_truck_node:
                self.current_truck_node = self.engine.warehouses.head
            self.show_message(f"Almacén '{name}' agregado.")
            
    # NUEVO: Verifica si hay al menos un vehículo despachado
    def has_dispatched_vehicles(self):
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

    # NUEVO: Vacía la pila de carga simulando la entrega
    def _empty_dispatched_vehicles(self):
        if not self.engine.vehicle_fleet.tail: 
            return
        curr = self.engine.vehicle_fleet.tail.next
        start = curr
        while True:
            vehicle = curr.data
            if vehicle.current_load_weight() >= vehicle.max_capacity:
                # Extraemos todos los paquetes de la pila hasta que quede vacía
                while vehicle.cargo.top:
                    vehicle.cargo.pop()
            curr = curr.next
            if curr == start:
                break
        self.show_message("¡Vuelta completa! Los vehículos entregaron su carga y vuelven a la base.", is_error=False)

    def advance_route(self):
        # 1. Validamos que haya camiones con carga
        if not self.has_dispatched_vehicles():
            self.show_message("No hay vehículos despachados (con carga máxima) para avanzar en la ruta.", is_error=True)
            return

        if self.current_truck_node and self.current_truck_node.next:
            start_time = time.perf_counter()
            
            # Avanzamos el puntero al siguiente almacén
            self.current_truck_node = self.current_truck_node.next
            
            # 2. Si el camión regresó al inicio (head), dio una vuelta completa
            if self.current_truck_node == self.engine.warehouses.head:
                self._empty_dispatched_vehicles()
                
            self.last_exec_time = (time.perf_counter() - start_time) * 1000
            self.last_action_type = "traverse"
            self.last_steps = 1
            self.operation_count += 1

    def add_vehicle(self, plate_number):
        if plate_number:
            self._measure_time("insert", 1, self.engine.register_vehicle, plate_number)
            self.show_message(f"Vehículo '{plate_number}' registrado.")

    def add_order(self, tracking_id, priority):
        if tracking_id and priority:
            current_size = self.engine.pending_orders._size
            pasos_estimados = current_size + 1 if current_size > 0 else 1
            self._measure_time("insert", pasos_estimados, self.engine.receive_order, tracking_id, int(priority))

    def dispatch_order(self):
        pasos_estimados = self.engine.vehicle_fleet._size + 1 if self.engine.vehicle_fleet._size > 0 else 1
        result = self._measure_time("stack", pasos_estimados, self.engine.dispatch_next_order)
        
        if result:
            if result.get("status") == "error":
                self.show_message(result["message"], is_error=True)
            else:
                pkg_id = result["package"].tracking_id
                veh_plate = result["vehicle"].plate_number
                self.show_message(f"Paquete {pkg_id} cargado en {veh_plate}.")

    def undo_action(self):
        self._measure_time("stack", 2, self._undo_logic)

    def _undo_logic(self):
        action_dict = self.engine.action_manager.undo()
        if action_dict and action_dict.get("action") == "dispatch":
            vehicle = action_dict.get("vehicle")
            popped_pkg = vehicle.cargo.pop()
            if popped_pkg:
                self.engine.pending_orders.enqueue(popped_pkg, popped_pkg.priority)
                self.show_message(f"Deshecho: Paquete {popped_pkg.tracking_id} devuelto.", is_error=True)

    def redo_action(self):
        pasos = self.engine.pending_orders._size + 1
        self._measure_time("stack", pasos, self._redo_logic)

    def _redo_logic(self):
        action_dict = self.engine.action_manager.redo()
        if action_dict and action_dict.get("action") == "dispatch":
            package = action_dict.get("package")
            vehicle = action_dict.get("vehicle")
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
            vehicle.cargo.push(package)
            self.show_message(f"Rehecho: Paquete {package.tracking_id} reasignado.")