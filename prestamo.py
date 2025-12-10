# Integrantes:
# - HERNANDEZ AMADA
# - SOLIS BRIGGITTE
# - CARRERA EDUARDO
# - ZAMBRANO KELY

from servicio import Servicio
from libro import Libro


class Prestamo(Servicio):
    """
    Servicio de préstamo presencial de un libro.
    Calcula costo si hay días de retraso o tarifa por días especiales.
    """

    def __init__(self, id_servicio: int, precio: float, descripcion: str,
                 libro: Libro, dias: int, penalidad_por_dia: float = 0.5):
        super()._init_(id_servicio, precio, descripcion)
        self._libro = None
        self._dias = None
        self._penalidad_por_dia = None

        self.libro = libro
        self.dias = dias
        self.penalidad_por_dia = penalidad_por_dia

    @property
    def libro(self):
        return self._libro

    @libro.setter
    def libro(self, v):
        if not isinstance(v, Libro):
            raise ValueError("libro debe ser una instancia de Libro")
        self._libro = v

    @property
    def dias(self):
        return self._dias

    @dias.setter
    def dias(self, v):
        if not isinstance(v, int) or v < 0:
            raise ValueError("dias debe ser entero >= 0")
        self._dias = v

    @property
    def penalidad_por_dia(self):
        return self._penalidad_por_dia

    @penalidad_por_dia.setter
    def penalidad_por_dia(self, v):
        if not isinstance(v, (int, float)) or v < 0:
            raise ValueError("penalidad_por_dia debe ser >= 0")
        self._penalidad_por_dia = float(v)

    def calcular_costo(self):
        """
        Política simple: costo = precio base + (dias * penalidad_por_dia)
        (los dias aquí representan días de retraso; si 0, no hay penalidad)
        """
        costo = self.precio + (self.dias * self.penalidad_por_dia)
        return round(costo, 2)

    def __str__(self):
        return (f"Prestamo(id={self.id}, libro={self.libro.titulo}, dias_retraso={self.dias}, "
                f"costo={self.calcular_costo()})")