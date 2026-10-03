class NodoCancion:
    def __init__(self, titulo, artista, duracion):
        # Almacenamos los datos en un diccionario como pide el requerimiento
        self.datos = {
            "titulo": titulo,
            "artista": artista,
            "duracion": duracion
        }
        self.siguiente = None  # Puntero a la siguiente canción


class BibliotecaMusical:
    def __init__(self):
        self.cabeza = None  # Inicio de la lista enlazada principal

    def anadir_cancion(self, titulo, artista, duracion):
        nuevo_nodo = NodoCancion(titulo, artista, duracion)
        
        if self.cabeza is None:
            self.cabeza = nuevo_nodo
        else:
            actual = self.cabeza
            while actual.siguiente is not None:
                actual = actual.siguiente
            actual.siguiente = nuevo_nodo

    def buscar_cancion(self, termino):
        resultados = []
        actual = self.cabeza
        
        while actual is not None:
            titulo_actual = actual.datos["titulo"].lower()
            artista_actual = actual.datos["artista"].lower()
            
            # Busca coincidencias parciales por título o artista
            if termino.lower() in titulo_actual or termino.lower() in artista_actual:
                resultados.append(actual.datos)
            
            actual = actual.siguiente
            
        return resultados

    def eliminar_cancion(self, titulo):
        actual = self.cabeza
        anterior = None

        while actual is not None:
            if actual.datos["titulo"].lower() == titulo.lower():
                # Si es el primer nodo
                if anterior is None:
                    self.cabeza = actual.siguiente
                else:
                    anterior.siguiente = actual.siguiente
                return True  # Retorna True si se eliminó con éxito
            
            anterior = actual
            actual = actual.siguiente
            
        return False  # Retorna False si no encontró la canción

    def obtener_biblioteca(self):
        canciones = []
        actual = self.cabeza
        while actual is not None:
            canciones.append(actual.datos)
            actual = actual.siguiente
        return canciones

    def crear_playlist(self, lista_titulos):
        # Crea una nueva instancia de BibliotecaMusical para usarla como playlist (nueva lista enlazada)
        playlist = BibliotecaMusical()
        
        for titulo in lista_titulos:
            actual = self.cabeza
            while actual is not None:
                if actual.datos["titulo"].lower() == titulo.lower():
                    # Si encuentra la canción, la añade a la nueva lista enlazada
                    playlist.anadir_cancion(
                        actual.datos["titulo"], 
                        actual.datos["artista"], 
                        actual.datos["duracion"]
                    )
                    break # Pasa al siguiente título una vez encontrada
                actual = actual.siguiente
                
        return playlist