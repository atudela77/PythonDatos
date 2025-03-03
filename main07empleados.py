# from services.service07oracleempleados import ServiceBBDDEmpleados as servicio
# from services.service07mysqlempleados import ServiceBBDDEmpleados as servicio
from services.service07sqlserverempleados import ServiceBBDDEmpleados as servicio

from models.empleado import Empleado

print("Probando servicios varios de base de datos")

miServicio = servicio()
empleados = miServicio.getAllEmpleados()
for emp in empleados:
    print(f"Apellido: {emp.apellido}, "
          f"Oficio: {emp. oficio}, "
          f"Salario: {emp.salario}")

print("Introduzca un salario para buscar")
salario = int(input())
empleados = miServicio.getAllEmpleadosSalario(salario)
for emp in empleados:
    print(f"Apellido: {emp.apellido}, "
          f"Oficio: {emp. oficio}, "
          f"Salario: {emp.salario}")

print("Fin de programa")
