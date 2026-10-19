import flet as ft
from controllers.app_controller import AppController
from views.responsive_components import PriorityQueueView, StackView, CircularRouteView, MetricsPanelView

def main_view(page: ft.Page):
    page.title = "Simulador de Centro Logístico"
    page.theme_mode = ft.ThemeMode.LIGHT
    page.padding = 20

    controller = AppController(page)

    tracking_input = ft.TextField(label="ID Paquete", width=150)
    priority_input = ft.TextField(label="Prioridad (1-10)", width=120)
    plate_input = ft.TextField(label="Placa Vehículo", width=200)
    warehouse_input = ft.TextField(label="Nombre Almacén", width=200)

    pending_orders_view = PriorityQueueView(controller.engine.pending_orders)
    warehouses_view = CircularRouteView(controller)
    metrics_view = MetricsPanelView(controller) 
    fleet_stack_container = ft.Row(wrap=True, spacing=20, vertical_alignment=ft.CrossAxisAlignment.START)

    def refresh_views():
        pending_orders_view.update_view()
        warehouses_view.update_view()
        metrics_view.update_view()
        
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
                    ], alignment=ft.MainAxisAlignment.START) # Añadir esta alineación
                )
                if temp == current:
                    break
                temp = temp.next
        
        pending_orders_view.update()
        warehouses_view.update()
        metrics_view.update() 
        fleet_stack_container.update()
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
            
    def on_advance_route(e):
        controller.advance_route()
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

    # Columna Izquierda: Simulador principal (expand=2 para que tome más espacio)
    main_simulator_col = ft.Column([
        ft.Text("Simulador Logístico", size=24, weight=ft.FontWeight.BOLD),
        ft.Divider(),
        
        ft.Row([
            warehouse_input, 
            ft.Button(content=ft.Text("Agregar Almacén"), on_click=on_add_warehouse),
            ft.Button(content=ft.Text("Avanzar Ruta 🚚"), on_click=on_advance_route, bgcolor=ft.Colors.AMBER_200)
        ], wrap=True),
        warehouses_view,
        ft.Divider(),
        
        ft.Row([
            tracking_input, priority_input, 
            ft.Button(content=ft.Text("Agregar Pedido"), on_click=on_add_order)
        ], wrap=True),
        pending_orders_view,
        ft.Divider(),
        
        ft.Row([
            plate_input, 
            ft.Button(content=ft.Text("Registrar Vehículo"), on_click=on_add_vehicle)
        ], wrap=True),
        ft.Row([
            ft.Button(content=ft.Text("Despachar Siguiente"), on_click=on_dispatch, bgcolor=ft.Colors.GREEN_200),
            ft.Button(content=ft.Text("Deshacer"), on_click=on_undo, bgcolor=ft.Colors.ORANGE_200),
            ft.Button(content=ft.Text("Rehacer"), on_click=on_redo, bgcolor=ft.Colors.BLUE_200)
        ], wrap=True),
        ft.Divider(),
        
        ft.Text("Carga de Vehículos :", weight=ft.FontWeight.BOLD),
        fleet_stack_container
    ], expand=2, scroll=ft.ScrollMode.AUTO)

    # Layout Principal: Fila que divide la pantalla responsivamente
    main_layout = ft.Row([
        main_simulator_col,
        ft.VerticalDivider(width=20, color=ft.Colors.GREY_300),
        ft.Column([metrics_view], expand=1) # expand=1 permite que se adapte al espacio sin aplastarse
    ], expand=True)

    page.add(main_layout)