# filepath: /tkinter-mvc-app/tkinter-mvc-app/src/main.py

import tkinter as tk
from views.view import View
from controllers.controller import Controller
from models.model import DataModel as Model

def main():
    root = tk.Tk()
    root.title("Tkinter MVC App")
    
    root.geometry("400x320")  # Tamaño de la ventana
    root.update_idletasks()  # Actualiza la ventana antes de centrarla

    # Centrar la ventana en la pantalla
    ancho = root.winfo_width()      
    alto = root.winfo_height()

    pantalla_ancho = root.winfo_screenwidth()       
    pantalla_alto = root.winfo_screenheight()

    x = (pantalla_ancho // 2) - (ancho // 2)
    y = (pantalla_alto // 2) - (alto // 2)

    root.geometry(f"+{x}+{y}")

    model = Model()
    model.add_data("Sample Data option 1")
    view = View(root)
    controller = Controller(view,model)
    
    root.mainloop()

if __name__ == "__main__":
    main()