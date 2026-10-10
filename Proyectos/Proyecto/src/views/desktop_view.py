# views/desktop_view.py
import flet as ft
from controllers.app_controller import AppController
from views.responsive_components import PriorityQueueView, StackView, DoublyLinkedListView

def main_view(page: ft.Page):
    page.title = "Simulador de Centro Logístico"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20
    page.scroll = ft.ScrollMode.AUTO # Agregamos scroll por si la pantalla se llena

    controller = AppController(page)

    # Entradas de texto
    tracking_input = ft.TextField(label="ID Paquete (Ej. PKG-01)", width=200)
    priority_input = ft.TextField(label="Prioridad (1-10)", width=120)
    plate_input = ft.TextField(label="Placa del Vehículo", width=200)
    warehouse_input = ft.TextField(label="Nombre Almacén", width=200)

    # Vistas visuales de las estructuras
    pending_orders_view = PriorityQueueView(controller.engine.pending_orders)
    warehouses_view = DoublyLinkedListView(controller.engine.warehouses)
    
    # Contenedor dinámico para mostrar las pilas de los vehículos
    fleet_stack_container = ft.Row(wrap=True, spacing=20)

    def refresh_views():
        pending_orders_view.update_view()
        warehouses_view.update_view()
        
        # Actualizar las pilas de todos los vehículos en la cola circular
        fleet_stack_container.controls.clear()
        current = controller.engine.vehicle_fleet.tail
        if current:
            head = current.next
            temp = head
            while True:
                vehicle = temp.data
                fleet_stack_container.controls.append(
                    ft.Column([
                        ft.Text(f"🚚 Vehículo: {vehicle.plate_number}", weight=ft.FontWeight.BOLD),
                        StackView(vehicle.cargo)
                    ])
                )
                if temp == current:
                    break
                temp = temp.next
        
        page.update()

    def on_add_order(e):
        if tracking_input.value and priority_input.value.isdigit():
            controller.add_order(tracking_input.value, int(priority_input.value))
            tracking_input.value = ""
            priority_input.value = ""
            refresh_views()

    def on_add_vehicle(e):
        if plate_input.value:
            controller.add_vehicle(plate_input.value)
            plate_input.value = ""
            refresh_views()

    def on_add_warehouse(e):
        if warehouse_input.value:
            controller.add_warehouse(warehouse_input.value)
            warehouse_input.value = ""
            refresh_views()

    def on_dispatch(e):
        controller.dispatch_order()
        refresh_views()

    def on_undo(e):
        controller.undo_action()
        refresh_views()

    def on_redo(e):
        controller.redo_action()
        refresh_views()

    layout = ft.Column([
        ft.Text("Simulador de Logística y Despacho", size=24, weight=ft.FontWeight.BOLD),
        ft.Divider(),
        
        # Fila para Almacenes (Lista Doblemente Enlazada)
        ft.Row([
            warehouse_input, 
            ft.Button(content=ft.Text("Agregar Almacén"), on_click=on_add_warehouse)
        ]),
        ft.Text("Red de Almacenes (Lista Doblemente Enlazada):", weight=ft.FontWeight.BOLD),
        warehouses_view,
        ft.Divider(),
        
        # Fila para Pedidos (Cola de Prioridad)
        ft.Row([
            tracking_input, priority_input, 
            ft.Button(content=ft.Text("Agregar Pedido"), on_click=on_add_order)
        ]),
        ft.Text("Cola de Pedidos Pendientes (Prioridad):", weight=ft.FontWeight.BOLD),
        pending_orders_view,
        ft.Divider(),

        # Fila para Vehículos (Cola Circular)
        ft.Row([
            plate_input, 
            ft.Button(content=ft.Text("Registrar Vehículo"), on_click=on_add_vehicle)
        ]),
        
        ft.Divider(),
        
        # Controles Principales
        ft.Row([
            ft.Button(content=ft.Text("Despachar Siguiente"), on_click=on_dispatch, bgcolor=ft.Colors.GREEN_200),
            ft.Button(content=ft.Text("Deshacer"), on_click=on_undo, bgcolor=ft.Colors.ORANGE_200),
            ft.Button(content=ft.Text("Rehacer"), on_click=on_redo, bgcolor=ft.Colors.BLUE_200)
        ]),
        
        ft.Divider(),
        
        # Fila para Cargamentos (Pilas / Stacks)
        ft.Text("Carga de Vehículos (Pilas LIFO):", weight=ft.FontWeight.BOLD),
        fleet_stack_container
    ])

    page.add(layout)