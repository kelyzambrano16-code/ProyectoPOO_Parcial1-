# Integrantes:
# - HERNANDEZ AMADA
# - SOLIS BRIGGITTE
# - CARRERA EDUARDO
# - ZAMBRANO KELY

from abc import ABC, abstractmethod


class Servicio(ABC):
    """
    Superclase abstracta para servicios de la biblioteca.
    """

    def _init_(self, id_servicio: int, precio: float, descripcion: str):
        self._id = None
        self._precio = None
        self._descripcion = None

        self.id = id_servicio
        self.precio = precio
        self.descripcion = descripcion

    @property
    def id(self):
        return self._id

    @id.setter
    def id(self, value):
        if not isinstance(value, int) or value <= 0:
            raise ValueError("id debe ser entero positivo")
        self._id = value

    @property
    def precio(self):
        return self._precio

    @precio.setter
    def precio(self, value):
        if not isinstance(value, (int, float)) or value < 0:
            raise ValueError("precio debe ser número >= 0")
        self._precio = float(value)

    @property
    def descripcion(self):
        return self._descripcion

    @descripcion.setter
    def descripcion(self, value):
        if not isinstance(value, str) or not value.strip():
            raise ValueError("descripcion debe ser string no vacío")
        self._descripcion = value.strip()

    @abstractmethod
    def calcular_costo(self):
        """
        Método polimórfico que cada subclase implementa para calcular su costo.
        """
        pass

    def mostrar_info(self):
        return str(self)

    def __str__(self):
        return f"{self._class.name_}(id={self._id}, desc='{self._descripcion}', precio_base={self._precio})"