# Integrantes:
# - HERNANDEZ AMADA
# - SOLIS BRIGGITTE
# - CARRERA EDUARDO
# - ZAMBRANO KELY

class Libro:
    """
    Representa un libro de la biblioteca.
    """

    def __init__(self, titulo: str, autor: str, isbn: str, disponible: bool = True):
        self._titulo = None
        self._autor = None
        self._isbn = None
        self._disponible = None

        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = disponible

    @property
    def titulo(self):
        return self._titulo

    @titulo.setter
    def titulo(self, v):
        if not isinstance(v, str) or not v.strip():
            raise ValueError("titulo no válido")
        self._titulo = v.strip()

    @property
    def autor(self):
        return self._autor

    @autor.setter
    def autor(self, v):
        if not isinstance(v, str) or not v.strip():
            raise ValueError("autor no válido")
        self._autor = v.strip()

    @property
    def isbn(self):
        return self._isbn

    @isbn.setter
    def isbn(self, v):
        if not isinstance(v, str) or not v.strip():
            raise ValueError("isbn no válido")
        self._isbn = v.strip()

    @property
    def disponible(self):
        return self._disponible

    @disponible.setter
    def disponible(self, v):
        if not isinstance(v, bool):
            raise ValueError("disponible debe ser booleano")
        self._disponible = v

    def __str__(self):
        disp = "sí" if self._disponible else "no"
        return f"Libro('{self._titulo}' by {self._autor}, ISBN={self._isbn}, disponible={disp})"