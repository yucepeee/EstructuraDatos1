import flet as ft
import sys
from models.structures import Node

class StackView(ft.Column):
    """
    Vista para representar la pila de paquetes de un vehículo.
    """
    def __init__(self, stack_model):
        super().__init__(alignment=ft.MainAxisAlignment.END, spacing=5)
        self.stack_model = stack_model
        self.update_view()

    def update_view(self):
        self.controls.clear()
        current = self.stack_model.top
        while current:
            package_id = current.data.tracking_id if hasattr(current.data, 'tracking_id') else str(current.data)
            self.controls.append(
                ft.Container(
                    content=ft.Text(f"📦 Pkg: {package_id}", weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                    bgcolor=ft.Colors.BLUE_700,
                    padding=10,
                    border_radius=5,
                    width=150
                )
            )
            current = current.next

class PriorityQueueView(ft.Row):
    """
    Vista para representar la cola de prioridad de pedidos.
    """
    def __init__(self, queue_model):
        super().__init__(wrap=True, spacing=10)
        self.queue_model = queue_model
        self.update_view()

    def get_color_by_priority(self, priority):
        if priority > 10:
            return 
        if priority >= 10 :
            return ft.Colors.RED_600
        elif priority >= 5:
            return ft.Colors.ORANGE_500
        else:
            return ft.Colors.GREEN_500

    def update_view(self):
        self.controls.clear()
        current = self.queue_model.head
        while current:
            data_dict = current.data
            package = data_dict["data"]
            priority = data_dict["priority"]
            
            self.controls.append(
                ft.Card(
                    content=ft.Container(
                        content=ft.Column([
                            ft.Text(f"ID: {package.tracking_id}", weight=ft.FontWeight.BOLD),
                            ft.Text(f"Prioridad: {priority}"),
                        ]),
                        padding=10,
                        bgcolor=self.get_color_by_priority(priority),
                        border_radius=5,
                        width=120
                    )
                )
            )
            current = current.next

class CircularRouteView(ft.Row):
    """
    Vista para representar la ruta circular de almacenes.
    """
    def __init__(self, controller):
        super().__init__(wrap=True, spacing=5, vertical_alignment=ft.CrossAxisAlignment.CENTER)
        self.controller = controller
        self.update_view()

    def update_view(self):
        self.controls.clear()
        dll_model = self.controller.engine.warehouses
        current_truck = self.controller.current_truck_node
        
        if not dll_model.head:
            self.controls.append(ft.Text("Ruta vacía. Agrega almacenes."))
            return

        current = dll_model.head
        while True:
            warehouse_name = str(current.data)
            
            # Si el nodo actual es donde está el camión, lo pintamos de otro color
            is_active = (current == current_truck)
            bg_color = ft.Colors.AMBER_500 if is_active else ft.Colors.PURPLE_600
            text_color = ft.Colors.BLACK if is_active else ft.Colors.WHITE
            icon = "🚚 " if is_active else "🏢 "
            
            self.controls.append(
                ft.Container(
                    content=ft.Text(f"{icon}{warehouse_name}", weight=ft.FontWeight.BOLD, color=text_color),
                    bgcolor=bg_color,
                    padding=15,
                    border_radius=8
                )
            )
            
            self.controls.append(ft.Text("↔️", size=24))
                
            current = current.next
            if current == dll_model.head:
                # Indicador de que la ruta vuelve a empezar (Círculo)
                self.controls.append(ft.Text("🔁 (Vuelve al inicio)", color=ft.Colors.GREY_500))
                break

class MetricsPanelView(ft.Column):
    def __init__(self, controller):
        super().__init__(spacing=10)
        self.controller = controller
        
        import sys
        from models.structures import Node
        self.base_node_memory = sys.getsizeof(Node(None))
        
        self.op_count_text = ft.Text("Operaciones (Totales): 0", weight=ft.FontWeight.BOLD, color=ft.Colors.BLUE_600)
        self.memory_text = ft.Text("Memoria dinámica: 0 bytes", weight=ft.FontWeight.BOLD, color=ft.Colors.RED_500)
        self.time_text = ft.Text("Tiempo última acción: 0.000 ms", weight=ft.FontWeight.BOLD, color=ft.Colors.PURPLE_600)
        
        self.complexity_table = ft.DataTable(
            column_spacing=15,
            horizontal_margin=10,
            columns=[
                ft.DataColumn(ft.Text("Acción", weight=ft.FontWeight.BOLD)),
                ft.DataColumn(ft.Text("Tus Nodos", weight=ft.FontWeight.BOLD)),
            ],
            rows=[
                ft.DataRow(cells=[ft.DataCell(ft.Text("Insertar / Encolar")), ft.DataCell(ft.Text("O(1)", color=ft.Colors.GREEN))]),
                ft.DataRow(cells=[ft.DataCell(ft.Text("Recorrer Nodos")), ft.DataCell(ft.Text("O(n)", color=ft.Colors.RED))]),
                ft.DataRow(cells=[ft.DataCell(ft.Text("Push/Pop Pila")), ft.DataCell(ft.Text("O(1)", color=ft.Colors.GREEN))]),
            ]
        )
        
        self.controls = [
            ft.Text("Análisis y Rendimiento En Vivo", size=18, weight=ft.FontWeight.BOLD),
            self.op_count_text,
            self.memory_text,
            self.time_text,
            ft.Row([self.complexity_table], scroll=ft.ScrollMode.AUTO)
        ]

    def count_total_nodes(self):
        count = 0
        if self.controller.engine.warehouses.head:
            curr = self.controller.engine.warehouses.head
            while True:
                count += 1
                curr = curr.next
                if curr == self.controller.engine.warehouses.head: break
                    
        curr = self.controller.engine.pending_orders.head
        while curr:
            count += 1
            curr = curr.next
            
        if self.controller.engine.vehicle_fleet.tail:
            head = self.controller.engine.vehicle_fleet.tail.next
            curr = head
            while True:
                count += 1 
                cargo_curr = curr.data.cargo.top
                while cargo_curr:
                    count += 1
                    cargo_curr = cargo_curr.next
                if curr == self.controller.engine.vehicle_fleet.tail: break
                curr = curr.next
                
        return count

    def update_view(self):
        # Actualizar textos
        self.op_count_text.value = f"Operaciones (Totales): {self.controller.operation_count}"
        self.time_text.value = f"Tiempo de ejecución CPU: {self.controller.last_exec_time:.4f} ms"
        
        total_nodes = self.count_total_nodes()
        self.memory_text.value = f"Memoria RAM: ~{total_nodes * self.base_node_memory} bytes ({total_nodes} Nodos)"
        
        # Dinamismo visual en la tabla (Ejecuciones Algorítmicas Reales)
        last_action = getattr(self.controller, 'last_action_type', None)
        pasos_reales = getattr(self.controller, 'last_steps', 0)
        
        labels = ["Insertar / Encolar", "Recorrer Nodos", "Push/Pop Pila"]
        
        # Restaurar la tabla a su estado base
        for i in range(3):
            self.complexity_table.rows[i].cells[0].content.value = labels[i]
            self.complexity_table.rows[i].cells[0].content.color = ft.Colors.BLACK
            
            # Restaurar la columna 1 (Tus Nodos) a la teoría original
            textos_teoricos = ["O(1) o O(n)", "O(n)", "O(1)"]
            self.complexity_table.rows[i].cells[1].content.value = textos_teoricos[i]
            self.complexity_table.rows[i].cells[1].content.color = ft.Colors.GREY_700
            
        # Resaltar la fila correspondiente y mostrar LOS PASOS EXACTOS
        if last_action == "insert":
            self.complexity_table.rows[0].cells[0].content.value = f"👉 {labels[0]}"
            self.complexity_table.rows[0].cells[0].content.color = ft.Colors.BLUE_700
            self.complexity_table.rows[0].cells[1].content.value = f"{pasos_reales} Ejecuciones"
            self.complexity_table.rows[0].cells[1].content.color = ft.Colors.GREEN_600 if pasos_reales == 1 else ft.Colors.RED_600
            
        elif last_action == "traverse":
            self.complexity_table.rows[1].cells[0].content.value = f"👉 {labels[1]}"
            self.complexity_table.rows[1].cells[0].content.color = ft.Colors.BLUE_700
            self.complexity_table.rows[1].cells[1].content.value = f"{pasos_reales} Ejecuciones"
            self.complexity_table.rows[1].cells[1].content.color = ft.Colors.GREEN_600 if pasos_reales == 1 else ft.Colors.RED_600
            
        elif last_action == "stack":
            self.complexity_table.rows[2].cells[0].content.value = f"👉 {labels[2]}"
            self.complexity_table.rows[2].cells[0].content.color = ft.Colors.BLUE_700
            self.complexity_table.rows[2].cells[1].content.value = f"{pasos_reales} Ejecuciones"
            self.complexity_table.rows[2].cells[1].content.color = ft.Colors.GREEN_600 if pasos_reales <= 2 else ft.Colors.RED_600