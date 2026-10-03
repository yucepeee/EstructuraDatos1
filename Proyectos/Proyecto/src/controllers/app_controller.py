class Controller:
    def __init__(self, model, view):
        self.model = model
        self.view = view
        
        # Bind view events to controller methods
        self.view.some_button_command = self.handle_button_click

    def handle_button_click(self):
        # Example of handling a button click
        data = self.model.get_data()
        self.view.update_display(data)

    def update_model(self, new_data):
        self.model.set_data(new_data)
        self.view.update_display(new_data)
    
    def update_view(self):
        """Update the view with data from the model."""
        data = self.model.get_data()  # Supongamos que el modelo tiene un método get_data()
        self.view.update_label(data)