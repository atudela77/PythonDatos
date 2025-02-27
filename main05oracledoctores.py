from services import service05oracledoctores as servicio
# from models import doctor
from os import system
system("clear")

ctrlWhile = ""
# Creamos un objeto de tipo servicio para tener la conexión
miServicio = servicio.ServiceOracleDoctores()
while (ctrlWhile != "X"):
    system("clear")
    print("----------- CRUD  Doctores -----------")
    print("------ Servicio Oracle Doctores ------\n")
    # Solicitamos toda la información necesaria al usuario
    print("1. Insertar doctor")
    print("2. Buscar doctor")
    print("3. Eliminar doctor")
    print("4. Modificar doctor")
    print("5. Mostrar todos los doctores" + "\n")
    print("Seleccione una opción")
    opcion = int(input())
    if (opcion == 1):
        system("clear")
        print(">>>>>> Insertar doctor <<<<<<"+"\n")
        print("Introduzca el id del doctor: ")
        idDoctor = int(input())
        print("Introduzca el apellido del doctor: ")
        apellido = input()
        print("Introduzca la especialidad del doctor: ")
        especialidad = input()
        print("Introduzca el salario del doctor: ")
        salario = int(input())
        print("Introduzca el hospital del doctor: ")
        hospital = input()
        insertados = miServicio.insertarDoctor(idDoctor, apellido,
                                               especialidad, salario,
                                               hospital)
        print(f"Doctores insertados:{insertados}")
    elif (opcion == 2):
        system("clear")
        print(">>>>>> Buscar doctor <<<<<<"+"\n")
        print("Introduzca el id del doctor: ")
        idDoctor = int(input())
        doc = miServicio.buscarDoctor(idDoctor)
        system("clear")
        print("DOC APELLIDO     ESPECIALIDAD SALARIO   HP")
        print("--- ------------ ------------ --------- --")
        print(f"{doc.idDoctor:3} {doc.apellido:12} "
              f"{doc.especialidad:12} {doc.salario:8,}€ "
              f"{doc.hospital:2} \n")
    elif (opcion == 3):
        system("clear")
        print(">>>>>> Eliminar doctor <<<<<<"+"\n")
        print("Introduzca el id del doctor: ")
        idDoctor = int(input())
        eliminados = miServicio.eliminarDoctor(idDoctor)
        print(f"Doctores eliminados: {eliminados}")
    elif (opcion == 4):
        system("clear")
        print(">>>>>> Modificar doctor <<<<<<"+"\n")
        print("Introduzca el id del doctor: ")
        idDoctor = int(input())
        print("Introduzca el nuevo apellido del doctor: ")
        apellido = input()
        print("Introduzca la nueva especialidad del doctor: ")
        especialidad = input()
        print("Introduzca el nuevo salario del doctor: ")
        salario = int(input())
        print("Introduzca el nuevo hospital del doctor: ")
        hospital = input()
        modificados = miServicio.modificarDoctor(idDoctor, apellido,
                                                 especialidad, salario,
                                                 hospital)
        print(f"Doctores modificados: {modificados}")
    elif (opcion == 5):
        system("clear")
        print(">>>>>> Todos los doctores <<<<<<"+"\n")
        print("DOC APELLIDO     ESPECIALIDAD SALARIO   HP")
        print("--- ------------ ------------ --------- --")
        doctores = miServicio.getAllDoctores()
        for doc in doctores:
            print(f"{doc.idDoctor:3} {doc.apellido:12} "
                  f"{doc.especialidad:12} {doc.salario:8,}€ "
                  f"{doc.hospital:2} ")

    # match opcion:
    #     case 1:
    #         system("clear")
    #         print(">>>>>> Insertar doctor <<<<<<"+"\n")
    #         print("Introduzca el id del doctor: ")
    #         idDoctor = int(input())
    #         print("Introduzca el apellido del doctor: ")
    #         apellido = input()
    #         print("Introduzca la especialidad del doctor: ")
    #         especialidad = input()
    #         print("Introduzca el salario del doctor: ")
    #         salario = int(input())
    #         print("Introduzca el hospital del doctor: ")
    #         hospital = input()
    #         insertados = miServicio.insertarDoctor(idDoctor, apellido,
    #                                                especialidad, salario,
    #                                                hospital)
    #         print(f"Doctores insertados:{insertados}")
    #     case 2:
    #         system("clear")
    #     case 3:
    #         system("clear")
    #         print(">>>>>> Insertar doctor <<<<<<"+"\n")
    #         print("Introduzca el id del doctor: ")
    #         idDoctor = int(input())
    #         eliminados = miServicio.eliminarDoctor(idDoctor)
    #         print(f"Doctores eliminados: {eliminados}")
    #     case 4:
    #         system("clear")
    #         print(">>>>>> Insertar doctor <<<<<<"+"\n")
    #         print("Introduzca el id del doctor: ")
    #         idDoctor = int(input())
    #         print("Introduzca el nuevo apellido del doctor: ")
    #         apellido = input()
    #         print("Introduzca la nueva especialidad del doctor: ")
    #         especialidad = input()
    #         print("Introduzca el nuevo salario del doctor: ")
    #         salario = int(input())
    #         print("Introduzca el nuevo hospital del doctor: ")
    #         hospital = input()
    #         modificados = miServicio.modificarDoctor(idDoctor, apellido,
    #                                                 especialidad, salario,
    #                                                 hospital)
    #         print(f"Doctores modificados: {modificados}")
    #     case 5:
    #         system("clear")
    #         print("DOC APELLIDO     ESPECIALIDAD SALARIO   HP")
    #         print("--- ------------ ------------ --------- --")
    #         doctores = miServicio.getAllDoctores()
    #         for doc in doctores:
    #             print(f"{doc.idDoctor:3} {doc.apellido:12} "
    #                   f"{doc.especialidad:12} {doc.salario:8,}€ "
    #                   f"{doc.hospital:2} ")
    # Variable de control del bucle
    print("Pulsar X para salir o cualquier tecla para volver al menú.")
    ctrlWhile = input().upper()

system("clear")
print("\nFin de programa")
