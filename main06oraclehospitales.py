from services import service06oraclehospitales as servicio
# from models import hospital as model
from os import system

miServicio = servicio.ServiceOracleHospitales()
ctrlWhile = ""
while (ctrlWhile != "X"):
    system("clear")
    print("------------ CRUD Hospitales -------------")
    print("------- Servicio Oracle Hospitales -------\n")
    # Solicitamos toda la información necesaria al usuario
    print("1. Mostrar todos los hospitales")
    print("2. Buscar hospital")
    print("3. Insertar nuevo hospital")
    print("4. Modificar hospital")
    print("5. Eliminar hospital\n")
    print("Seleccione una opción")
    opcion = int(input())

    match opcion:
        case 1:
            system("clear")
            print("")
            hospitales = miServicio.getAllHospitales()
            for hospital in hospitales:
                print(f"{hospital.idHospital:4} {hospital.nombre:12}"
                      f"{hospital.direccion:16} {hospital.telefono:10}"
                      f"{hospital.numeroCamas:4}")
        case 2:
            system("clear")
        case 3:
            system("clear")
        case 4:
            system("clear")
        case 5:
            system("clear")

    print("Pulse X para salir u otra tecla cualquiera para volver al menú")
    ctrlWhile = input().upper()
system("clear")
print("Fin del programa")
