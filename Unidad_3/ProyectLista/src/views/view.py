import tkinter as tk
from tkinter import messagebox, simpledialog

class VistaGrafica:
    def __init__(self):
        # Crear la ventana principal
        self.root = tk.Tk()
        self.root.title("🎵 Mi Biblioteca Musical 🎵")
        self.root.geometry("600x450")
        self.root.config(padx=20, pady=20)
        
        # Título
        tk.Label(self.root, text="Biblioteca Musical", font=("Helvetica", 16, "bold")).pack(pady=5)
        
        # Cuadro de lista para mostrar las canciones
        self.listbox_canciones = tk.Listbox(self.root, width=70, height=15, font=("Courier", 10))
        self.listbox_canciones.pack(pady=10)
        
        # Contenedor para los botones
        frame_botones = tk.Frame(self.root)
        frame_botones.pack(pady=10)
        
        # Botones (sus acciones se asignarán desde el controlador)
        self.btn_anadir = tk.Button(frame_botones, text="Añadir Canción", width=15)
        self.btn_anadir.grid(row=0, column=0, padx=5, pady=5)
        
        self.btn_buscar = tk.Button(frame_botones, text="Buscar Canción", width=15)
        self.btn_buscar.grid(row=0, column=1, padx=5, pady=5)
        
        self.btn_eliminar = tk.Button(frame_botones, text="Eliminar Canción", width=15)
        self.btn_eliminar.grid(row=0, column=2, padx=5, pady=5)
        
        self.btn_mostrar = tk.Button(frame_botones, text="Mostrar Biblioteca", width=15)
        self.btn_mostrar.grid(row=1, column=0, padx=5, pady=5)
        
        self.btn_playlist = tk.Button(frame_botones, text="Crear Playlist", width=15)
        self.btn_playlist.grid(row=1, column=1, padx=5, pady=5)
        
        self.btn_salir = tk.Button(frame_botones, text="Salir", width=15, command=self.root.quit)
        self.btn_salir.grid(row=1, column=2, padx=5, pady=5)

    def conectar_eventos(self, controlador):
        # Este método enlaza los clics de los botones con las funciones del controlador
        self.btn_anadir.config(command=controlador._agregar_cancion)
        self.btn_buscar.config(command=controlador._buscar_cancion)
        self.btn_eliminar.config(command=controlador._eliminar_cancion)
        self.btn_mostrar.config(command=controlador._mostrar_biblioteca)
        self.btn_playlist.config(command=controlador._crear_playlist)

    # --- Métodos de Interacción con el Usuario mediante Ventanas Emergentes ---

    def obtener_datos_cancion(self):
        titulo = simpledialog.askstring("Añadir", "Ingresa el Título:")
        if not titulo: return None, None, None  # Si el usuario cancela
        
        artista = simpledialog.askstring("Añadir", "Ingresa el Artista:")
        duracion = simpledialog.askstring("Añadir", "Ingresa la Duración (ej. 3:45):")
        return titulo, artista, duracion

    def obtener_termino_busqueda(self):
        return simpledialog.askstring("Buscar", "Ingresa el título o artista a buscar:")

    def obtener_titulo_eliminar(self):
        return simpledialog.askstring("Eliminar", "Ingresa el título exacto a eliminar:")

    def obtener_titulos_playlist(self):
        messagebox.showinfo("Crear Playlist", "Agrega las canciones de tu playlist.\nDeja el texto en blanco y presiona OK para terminar.")
        titulos = []
        while True:
            titulo = simpledialog.askstring("Playlist", "Añadir título (en blanco para terminar):")
            if not titulo: # Si cancela o deja en blanco
                break
            titulos.append(titulo.strip())
        return titulos

    def mostrar_canciones(self, canciones, titulo_seccion="Canciones"):
        self.listbox_canciones.delete(0, tk.END) # Limpia la lista actual
        self.listbox_canciones.insert(tk.END, f"--- {titulo_seccion} ---")
        
        if not canciones:
            self.listbox_canciones.insert(tk.END, "No hay canciones para mostrar.")
        else:
            for idx, cancion in enumerate(canciones, 1):
                texto = f"{idx}. {cancion['titulo']} - {cancion['artista']} ({cancion['duracion']})"
                self.listbox_canciones.insert(tk.END, texto)

    def mostrar_mensaje(self, mensaje):
        messagebox.showinfo("Notificación", mensaje)

    def iniciar(self):
            # Mantiene la ventana abierta y escuchando clics
            self.root.mainloop()