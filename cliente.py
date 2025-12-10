# Integrantes:
# - HERNANDEZ AMADA
# - SOLIS BRIGGITTE
# - CARRERA EDUARDO
# - ZAMBRANO KELY

class Cliente:
    """
    Representa un usuario/cliente de la biblioteca.
    """
    def __init__(self, id_cliente: int, nombre: str, es_socio: bool = False):
        self._id_cliente = None
        self._nombre = None
        self._es_socio = None

        self.id_cliente = id_cliente
        self.nombre = nombre
        self.es_socio = es_socio

    @property
    def id_cliente(self):
        return self._id_cliente

    @id_cliente.setter
    def id_cliente(self, v):
        if not isinstance(v, int) or v <= 0:
            raise ValueError("id_cliente debe ser entero positivo")
        self._id_cliente = v

    @property
    def nombre(self):
        return self._nombre

    @nombre.setter
    def nombre(self, v):
        if not isinstance(v, str) or not v.strip():
            raise ValueError("nombre no válido")
        self._nombre = v.strip()

    @property
    def es_socio(self):
        return self._es_socio

    @es_socio.setter
    def es_socio(self, v):
        if not isinstance(v, bool):
            raise ValueError("es_socio debe ser booleano")
        self._es_socio = v

    def aplicar_descuento(self, monto: float) -> float:
        """
        Los socios tienen 20% de descuento sobre el costo del servicio.
        """
        if not isinstance(monto, (int, float)) or monto < 0:
            raise ValueError("monto no válido")
        if self.es_socio:
            return round(monto * 0.8, 2)
        return round(monto, 2)

    def __str__(self):
        return f"Cliente(id={self.id_cliente}, nombre='{self.nombre}', socio={self.es_socio})"