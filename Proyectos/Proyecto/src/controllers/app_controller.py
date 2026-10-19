from models.logistic_engine import LogisticEngine
from models.structures import CircularDoublyLinkedList
import flet as ft

class AppController:
    def __init__(self, page):
        self.page = page
        self.engine = LogisticEngine()
        self.engine.warehouses = CircularDoublyLinkedList()
        self.current_truck_node = None 
        self.operation_count = 0 
        
    def show_message(self, message, is_error=False):
        """Muestra un Snackbar emergente en la parte inferior de la pantalla."""
        color = ft.Colors.RED_700 if is_error else ft.Colors.GREEN_700
        snack = ft.SnackBar(content=ft.Text(message, color=ft.Colors.WHITE, weight=ft.FontWeight.BOLD), bgcolor=color)
        
        # Compatibilidad con las nuevas versiones de Flet
        try:
            self.page.open(snack)
        except AttributeError:
            self.page.snack_bar = snack
            self.page.snack_bar.open = True
            self.page.update()
            
    def add_warehouse(self, name):
        if name:
            self.engine.warehouses.append(name) 
            if not self.current_truck_node:
                self.current_truck_node = self.engine.warehouses.head
            self.operation_count += 1
            self.show_message(f"Almacén '{name}' agregado a la ruta.")
            
    def advance_route(self):
        if self.current_truck_node and self.current_truck_node.next:
            self.current_truck_node = self.current_truck_node.next
            self.operation_count += 1

    def add_vehicle(self, plate_number):
        if plate_number:
            self.engine.register_vehicle(plate_number)
            self.operation_count += 1
            self.show_message(f"Vehículo '{plate_number}' registrado en la flota.")

    def add_order(self, tracking_id, priority):
        if tracking_id and priority:
            self.engine.receive_order(tracking_id, int(priority))
            self.operation_count += 1

    def dispatch_order(self):
        result = self.engine.dispatch_next_order()
        if result:
            if result.get("status") == "error":
                self.show_message(result["message"], is_error=True)
            else:
                pkg_id = result["package"].tracking_id
                veh_plate = result["vehicle"].plate_number
                self.show_message(f"Paquete {pkg_id} cargado en Vehículo {veh_plate}.")
        self.operation_count += 1

    def undo_action(self):
        action_dict = self.engine.action_manager.undo()
        if action_dict:
            if action_dict.get("action") == "dispatch":
                package = action_dict.get("package")
                vehicle = action_dict.get("vehicle")
                
                popped_pkg = vehicle.cargo.pop()
                if popped_pkg:
                    self.engine.pending_orders.enqueue(popped_pkg, popped_pkg.priority)
                    self.show_message(f"Deshecho: Paquete {popped_pkg.tracking_id} devuelto a cola.", is_error=True)
        self.operation_count += 1

    def redo_action(self):
        action_dict = self.engine.action_manager.redo()
        if action_dict:
            if action_dict.get("action") == "dispatch":
                package = action_dict.get("package")
                vehicle = action_dict.get("vehicle")
                
                # Eliminamos el paquete de la cola
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
                
                # Lo reinsertamos en el vehículo
                vehicle.cargo.push(package)
                self.show_message(f"Rehecho: Paquete {package.tracking_id} reasignado al Vehículo {vehicle.plate_number}.")
        self.operation_count += 1