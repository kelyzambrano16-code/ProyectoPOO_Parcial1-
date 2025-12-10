# Integrantes:
# - HERNANDEZ AMADA
# - SOLIS BRIGGITTE
# - CARRERA EDUARDO
# - ZAMBRANO KELY

from libro import Libro
from cliente import Cliente
from prestamo import Prestamo
from consulta import Consulta
from gestor_servicios import GestorServicios

def main():
    # Crear algunos libros
    libro1 = Libro("Cien años de soledad", "Gabriel García Márquez", "978-3-16-148410-0", True)
    libro2 = Libro("La biblioteca perdida", "Autor Ejemplo", "123-4-56-789012-3", True)

    # Crear clientes
    cliente1 = Cliente(1, "María Pérez", es_socio=True)
    cliente2 = Cliente(2, "Juan López", es_socio=False)

    # Crear servicios (subclases de Servicio)
    prestamo1 = Prestamo(id_servicio=1, precio=0.0, descripcion="Préstamo estándar",
                         libro=libro1, dias=0, penalidad_por_dia=0.75)
    prestamo2 = Prestamo(id_servicio=2, precio=0.0, descripcion="Préstamo con demora",
                         libro=libro2, dias=3, penalidad_por_dia=0.75)

    consulta1 = Consulta(id_servicio=3, precio=10.0, descripcion="Consulta bibliotecaria (tarifa por hora)",
                         duracion_minutos=30)

    consulta2 = Consulta(id_servicio=4, precio=10.0, descripcion="Consulta extendida",
                         duracion_minutos=90)

    servicios = [prestamo1, prestamo2, consulta1, consulta2]

    gestor = GestorServicios()
    for s in servicios:
        gestor.agregar_servicio(s)

    # Mostrar reporte (polimorfismo en acción)
    reporte = gestor.generar_reporte(gestor.listar_servicios())
    print(reporte)
    print()

    # Calcular total y aplicar descuento según cliente
    total = gestor.sumar_costos(servicios)
    print(f"Total bruto: {total}")

    total_cliente1 = cliente1.aplicar_descuento(total)
    total_cliente2 = cliente2.aplicar_descuento(total)
    print(f"Total para {cliente1.nombre} (socio): {total_cliente1}")
    print(f"Total para {cliente2.nombre} (no socio): {total_cliente2}")

    # Imprimir objetos con _str_ para evidencias
    print()
    print("Evidencias de impresión (_str_):")
    for s in servicios:
        print(s)

if __name__ == "__main__":
    main()