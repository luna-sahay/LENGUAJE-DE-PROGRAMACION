class Material:
    def __init__(self, titulo, autor):
        self.titulo = titulo
        self.autor = autor

    def obtener_detalle(self):
        return f"{self.titulo} - {self.autor}"

class Libro(Material):
    def __init__(self, titulo, autor, genero, nota):
        super().__init__(titulo, autor)
        self.genero = genero
        self.nota = nota

    def obtener_detalle(self): # Polimorfismo
        return f"[{self.genero.upper()}] {self.titulo} | Autor: {self.autor} | Nota: {self.nota}"
