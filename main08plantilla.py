# from services.service08sqlserverplantilla import ServicePlantilla as servicio
from services.service08mysqlplantilla import ServicePlantilla as servicio
# from services.service08oracleplantilla import ServicePlantilla as servicio
from models.plantilla import Plantilla
from os import system

miServicio = servicio()
ctrlWhile = ""
while ctrlWhile != "X":
    system("clear")
    print(">>>>>>>>>  Servicios para plantillas  <<<<<<<<<\n")
    print("1. Mostrar todos los empleados de la plantilla")
    print("2. Actualizar el salario de los empleados de un hospital\n")
    print("Seleccione una opción")
    opcion = int(input())
    match opcion:
        case 1:
            # Mostrar todos los empleados
            system("clear")
            print("EMPL APELLIDO             FUNCION               SALARIO    HOSP")
            print("---- -------------------- --------------------  ---------- ----")
            empleados = miServicio.getPlantilla()
            for emp in empleados:
                print(f"{emp.idPlantilla:4} "
                      f"{emp.apellido.title():20} "
                      f"{emp.funcion.title():20} "
                      f"{emp.salario:10}€ "
                      f"{emp.hospital:4}")
            print("\n")
        case 2:
            # Actualizar salario plantilla
            system("clear")
            print("Introduzca un código de hospital")
            hospital = int(input())
            print("Introduzca el incremento de salario")
            incremento = int(input())
            modificados = miServicio.updateSalarioPlantilla(incremento, hospital)
            print(f"Se ha incrementado el salario de {modificados} empleados.")
    print("Pulse X para salir o cualquier tecla para volver al menú")
    ctrlWhile = input().upper()
