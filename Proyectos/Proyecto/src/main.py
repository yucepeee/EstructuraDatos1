# filepath: /tkinter-mvc-app/tkinter-mvc-app/src/main.py

import tkinter as tk
from views.desktop_view import View
from controllers.app_controller import Controller
from models.structures import DataModel as Model

def main():
    root = tk.Tk()
    root.title("Tkinter MVC App")
    
    model = Model()
    model.add_data("Sample Data option 1")
    view = View(root)
    controller = Controller(view,model)
    
    root.mainloop()

if __name__ == "__main__":
    main()