class ControladorBiblioteca:
    def __init__(self, modelo, vista):
        self.modelo = modelo
        self.vista = vista
        
        # Le decimos a la vista qué métodos de este controlador ejecutar al hacer clic
        self.vista.conectar_eventos(self)

    def iniciar(self):
        # Arrancamos la interfaz gráfica
        self.vista.iniciar()

    def _agregar_cancion(self):
        titulo, artista, duracion = self.vista.obtener_datos_cancion()
        
        # Validamos que el usuario no haya presionado "Cancelar"
        if titulo and artista and duracion:
            self.modelo.anadir_cancion(titulo, artista, duracion)
            self.vista.mostrar_mensaje(f"Canción '{titulo}' añadida con éxito.")
            self._mostrar_biblioteca() # Refresca la lista automáticamente

    def _buscar_cancion(self):
        termino = self.vista.obtener_termino_busqueda()
        if termino:
            resultados = self.modelo.buscar_cancion(termino)
            self.vista.mostrar_canciones(resultados, f"Resultados para '{termino}'")

    def _eliminar_cancion(self):
        titulo = self.vista.obtener_titulo_eliminar()
        if titulo:
            exito = self.modelo.eliminar_cancion(titulo)
            if exito:
                self.vista.mostrar_mensaje(f"La canción '{titulo}' ha sido eliminada.")
                self._mostrar_biblioteca()
            else:
                self.vista.mostrar_mensaje(f"No se encontró '{titulo}'.")

    def _mostrar_biblioteca(self):
        canciones = self.modelo.obtener_biblioteca()
        self.vista.mostrar_canciones(canciones, "Biblioteca Principal")

    def _crear_playlist(self):
        titulos = self.vista.obtener_titulos_playlist()
        if titulos:
            playlist = self.modelo.crear_playlist(titulos)
            canciones_playlist = playlist.obtener_biblioteca()
            self.vista.mostrar_canciones(canciones_playlist, "Tu Nueva Playlist")