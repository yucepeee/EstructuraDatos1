from tkinter import Tk, Label, Button, Frame

class View:
    def __init__(self, master):
        self.master = master
        master.title("MVC Tkinter App")

        self.frame = Frame(master)
        self.frame.pack()

        self.label = Label(self.frame, text="Hello, MVC!")
        self.label.pack()

        self.button = Button(self.frame, text="Click Me", command=self.on_button_click)
        self.button.pack()

    def on_button_click(self):
        self.label.config(text="Button Clicked!")

    def update_label(self, text):
        """Update the label with the given text."""
        self.label.config(text=text)