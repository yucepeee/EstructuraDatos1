# views/responsive_components.py
import flet as ft

class StackView(ft.Column):
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
    def __init__(self, queue_model):
        super().__init__(wrap=True, spacing=10)
        self.queue_model = queue_model
        self.update_view()

    def get_color_by_priority(self, priority):
        if priority >= 10:
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

class DoublyLinkedListView(ft.Row):
    def __init__(self, dll_model):
        super().__init__(wrap=True, spacing=5, vertical_alignment=ft.CrossAxisAlignment.CENTER)
        self.dll_model = dll_model
        self.update_view()

    def update_view(self):
        self.controls.clear()
        current = self.dll_model.head
        while current:
            warehouse_name = current.data.name if hasattr(current.data, 'name') else str(current.data)
            
            # Caja del nodo
            self.controls.append(
                ft.Container(
                    content=ft.Text(f"🏢 {warehouse_name}", weight=ft.FontWeight.BOLD, color=ft.Colors.WHITE),
                    bgcolor=ft.Colors.PURPLE_600,
                    padding=15,
                    border_radius=8
                )
            )
            
            # Flecha bidireccional si hay un nodo siguiente
            if current.next:
                self.controls.append(ft.Text("↔️", size=24))
                
            current = current.next