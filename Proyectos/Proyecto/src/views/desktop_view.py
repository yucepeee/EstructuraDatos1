import flet as ft
import time
import asyncio
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
    
    # NUEVO: Separamos en dos contenedores distintos
    available_fleet_container = ft.Row(wrap=True, spacing=20, vertical_alignment=ft.CrossAxisAlignment.START)
    dispatched_fleet_container = ft.Row(wrap=True, spacing=20, vertical_alignment=ft.CrossAxisAlignment.START)

    def refresh_views():
        pending_orders_view.update_view()
        warehouses_view.update_view()
        metrics_view.update_view()
        
        # Limpiamos ambos contenedores
        available_fleet_container.controls.clear()
        dispatched_fleet_container.controls.clear()
        
        current = controller.engine.vehicle_fleet.tail
        if current:
            head = current.next
            temp = head
            while True:
                vehicle = temp.data
                
                # Verificamos si el vehículo está lleno (Capacidad máxima)
                is_full = vehicle.current_load_weight() >= vehicle.max_capacity
                
                # Creamos la vista del vehículo
                vehicle_ui = ft.Column([
                    ft.Text(f"🚚 Vehículo: {vehicle.plate_number}", weight=ft.FontWeight.BOLD),
                    StackView(vehicle.cargo)
                ], alignment=ft.MainAxisAlignment.START)
                
                # Lo asignamos a la sección correspondiente según su carga
                if is_full:
                    dispatched_fleet_container.controls.append(vehicle_ui)
                else:
                    available_fleet_container.controls.append(vehicle_ui)
                    
                if temp == current:
                    break
                temp = temp.next
        
        pending_orders_view.update()
        warehouses_view.update()
        metrics_view.update() 
        available_fleet_container.update()
        dispatched_fleet_container.update()
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

    async def on_run_demo(e):
        # 1. Añadir 5 almacenes uno por uno (más pausado)
        for i in range(1, 6):
            controller.add_warehouse(f"Almacén {i}")
            refresh_views()
            await asyncio.sleep(0.8) 
            
        await asyncio.sleep(0.5)

        # 2. Añadir 3 camiones uno por uno
        for i in range(1, 4):
            controller.add_vehicle(f"CAM-00{i}")
            refresh_views()
            await asyncio.sleep(0.8)

        await asyncio.sleep(0.5)

        # 3. Añadir paquetes (1 Alta, 6 Media, 8 Baja)
        controller.add_order("PKG-URGENTE-1", 10)
        refresh_views()
        await asyncio.sleep(0.6)
        
        for i in range(1, 7):
            controller.add_order(f"PKG-MED-{i}", 5)
            refresh_views()
            await asyncio.sleep(0.6)
            
        for i in range(1, 9):
            controller.add_order(f"PKG-BAJA-{i}", 1)
            refresh_views()
            await asyncio.sleep(0.6)

        await asyncio.sleep(1.5) # Pausa antes de iniciar el despacho

        # 4. Cargar los camiones (Despachar)
        # 1.2 segundos por despacho para apreciar cómo salen de la cola y entran a la pila del vehículo
        for _ in range(15):
            controller.dispatch_order()
            refresh_views()
            await asyncio.sleep(1.2)

        await asyncio.sleep(1.5) # Pausa antes de mover el camión en la ruta

        # 5. Animación de "Avanzar Ruta" mientras haya vehículos despachados
        # 1.5 segundos por salto para ver claramente el recorrido circular y la descarga final
        if controller.has_dispatched_vehicles():
            for _ in range(5):
                controller.advance_route()
                refresh_views()
                await asyncio.sleep(1.5)

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
            ft.Button(content=ft.Text("Rehacer"), on_click=on_redo, bgcolor=ft.Colors.BLUE_200),
            # NUEVO BOTÓN DE DEMOSTRACIÓN:
            ft.Button(content=ft.Text("🤖 Ejecutar Demo"), on_click=on_run_demo, bgcolor=ft.Colors.PURPLE_200)
        ], wrap=True),
        ft.Divider(),
        
        # NUEVO: Layout dividido para los vehículos
        ft.Text("Carga de Vehículos (Disponibles):", weight=ft.FontWeight.BOLD),
        available_fleet_container,
        ft.Divider(),
        
        ft.Text("Vehículos Despachados (Carga Completa):", weight=ft.FontWeight.BOLD, color=ft.Colors.RED_600),
        dispatched_fleet_container
        
    ], expand=2, scroll=ft.ScrollMode.AUTO)

    main_layout = ft.Row([
        main_simulator_col,
        ft.VerticalDivider(width=20, color=ft.Colors.GREY_300),
        ft.Column([metrics_view], expand=1) 
    ], expand=True)

    page.add(main_layout)