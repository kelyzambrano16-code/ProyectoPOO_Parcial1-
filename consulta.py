# Integrantes:
# - HERNANDEZ AMADA
# - SOLIS BRIGGITTE
# - CARRERA EDUARDO
# - ZAMBRANO KELY

from servicio import Servicio

class Consulta(Servicio):
    """
    Servicio de consulta (virtual o presencial corta). Se cobra por tiempo.
    """

    def __init__(self, id_servicio: int, precio: float, descripcion: str,
                 duracion_minutos: int):
        super()._init_(id_servicio, precio, descripcion)
        self._duracion_minutos = None
        self.duracion_minutos = duracion_minutos

    @property
    def duracion_minutos(self):
        return self._duracion_minutos

    @duracion_minutos.setter
    def duracion_minutos(self, v):
        if not isinstance(v, int) or v <= 0:
            raise ValueError("duracion_minutos debe ser entero > 0")
        self._duracion_minutos = v

    def calcular_costo(self):
        """
        Política: precio es tarifa por hora; costo proporcional a minutos.
        """
        horas = self.duracion_minutos / 60
        costo = self.precio * horas
        return round(costo, 2)

    def __str__(self):
        return (f"Consulta(id={self.id}, duracion={self.duracion_minutos}min, "
                f"costo={self.calcular_costo()})")