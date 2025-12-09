 Proyecto POO - Primer Parcial  
## Tema: Gestión de Servicios de Biblioteca (Grupo 1)

### Integrantes del grupo:
- HERNANDEZ SOTOMAYOR AMADA DAYANNA  
- SOLIS MACIAS BRIGGITTE LILIBETH  
- ZAMBRANO ALVARADO KELY TATIANA
- CARRERA CAISE EDUARDO JOSUE
-------------------
Explicación del proyecto

Este proyecto simula un sistema sencillo de gestión de servicios dentro de una biblioteca.

- Encapsulamiento  
- Herencia  
- Polimorfismo  
- Abstracción  
- Modularidad
- Organización del código en módulos  

El sistema maneja dos tipos de servicios:

- *Préstamo de libros*  
- *Consulta bibliotecaria*  

Cada servicio calcula su costo de forma diferente, esto permite demostrar polimorfismo.

---------------------
## Estructura del repositorio
ProyectoPOO_Parcial1

│── servicio.py

│── prestamo.py

│── consulta.py

│── libro.py

│── cliente.py

│── gestor_servicios.py

│── main.py

└── README.md

--------------------
#  Explicación de las clases
<img width="816" height="544" alt="image" src="https://github.com/user-attachments/assets/a9a26f79-8457-4df2-b468-d5d1c8b479f9" />

## Superclase
### *Servicio*
Define:
- id del servicio  
- descripción  
- precio base  
- método abstracto calcular_costo() 

Aplicamos encapsulamiento usando:
- atributos privados _atributo
- @property y @setter para validaciones
---

## Subclases (Herencia aplicada)

### *Prestamo*
Representa un préstamo de libro.
- Tiene un libro asociado
- Maneja días de retraso
- Calcula costo = penalidad × días de retraso

### *Consulta*
Servicio de consulta bibliotecaria por tiempo.
- Recibe duración en minutos
- Costo = tarifa por hora × horas consumidas
---

## Clases adicionales

### *Libro*
Contiene:
- título  
- autor  
- ISBN  
- disponibilidad  

### *Cliente*
- Puede ser socio (20% de descuento)
- Método: aplicar_descuento()

### *GestorServicios*
Contiene métodos polimórficos que funcionan con cualquier objeto que herede de Servicio:

1. sumar_costos(lista_servicios)
2. generar_reporte(lista_servicios)

---

Esto mostrará:
- Lista de servicios
- Costos individuales
- Total acumulado
- Descuentos por cliente
- Evidencias __str__

---
# Conceptos POO implementados

### Encapsulamiento
Todos los atributos son privados.  
Acceso solo mediante getters/setters con validaciones.

### Herencia
Prestamo y Consulta heredan de Servicio.

### Polimorfismo
El gestor usa:
s.calcular_costo()
---
*Ejecución del programa*

<img width="1355" height="763" alt="image" src="https://github.com/user-attachments/assets/087c8424-2db5-4b6a-a022-244d26a4c279" />
