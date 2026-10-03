# filepath: /tkinter-mvc-app/tkinter-mvc-app/src/main.py

import tkinter as tk
from views.view import VistaGrafica
from controllers.controller import ControladorBiblioteca
from models.model import BibliotecaMusical

def main(): 
    
    model = BibliotecaMusical()
    view = VistaGrafica()
    controller = ControladorBiblioteca(model, view)
    controller.iniciar()

if __name__ == "__main__":
    main()