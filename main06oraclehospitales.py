from services import service06oraclehospitales as servicio
# from models import hospital as model
from os import system


def print_cabecera(cad):
    linea0 = "++++++++++++++++++++++++++++++++++++++++++"
    linea1 = "------------ CRUD Hospitales -------------"
    linea2 = "------- Servicio Oracle Hospitales -------\n"
    linea3 = str(linea0[1:int((len(linea0) - len(cad))/2)]
                 + cad + linea0)[1:len(linea1) + 1] + "\n"
    system("clear")
    print(linea1)
    print(linea2)
    print(linea3)


def main():
    miServicio = servicio.ServiceOracleHospitales()
    ctrlWhile = ""
    while (ctrlWhile != "X"):
        print_cabecera(" Menú ")
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
                # Mostrar todos los hospitales de la tabla
                system("clear")
                print_cabecera(" Todos los hospitales ")
                print("HOSP NOMBRE              DIRECCION               "
                      "TELEFONO   CAMAS")
                print("---- ------------------- ----------------------- "
                      "---------- -----")
                hospitales = miServicio.getAllHospitales()
                for hospital in hospitales:
                    print(f"{hospital.idHospital:4} "
                          f"{hospital.nombre.title():20}"
                          f"{hospital.direccion.title():24} "
                          f"{hospital.telefono:10}"
                          f"{hospital.numeroCamas:5}")
                print("\n")
            case 2:
                # Buscar hospital por id
                print_cabecera(" Buscar hospital ")
                print("Introduzca un código de hospital: ")
                idHosp = int(input())
                print_cabecera(" Buscar hospital ")
                hospital = miServicio.buscarHospital(idHosp)
                if hospital is not None:
                    print("HOSP NOMBRE              DIRECCION              "
                          " TELEFONO   CAMAS")
                    print("---- ------------------- -----------------------"
                          " ---------- -----")
                    print(f"{hospital.idHospital:4} "
                          f"{hospital.nombre.title():20}"
                          f"{hospital.direccion.title():24} "
                          f"{hospital.telefono:10}"
                          f"{hospital.numeroCamas:5} \n")
                else:
                    print("No existe ningún hospital con ese código.\n")
            case 3:
                # Insertar nuevo registro de hospital
                print_cabecera(" Insertar hospital ")
                print("Introduzca un código de hospital: ")
                idHosp = int(input())
                print("Introduzca el nombre del nuevo hospital: ")
                nombre = input()
                print("Introduzca la dirección del nuevo hospital: ")
                direccion = input()
                print("Introduzca el teléfono del nuevo hospital: ")
                telefono = input()
                print("Introduzca el número de camas del nuevo hospital: ")
                numCamas = int(input())
                insertados = miServicio.insertarHospital(idHosp,
                                                         nombre,
                                                         direccion,
                                                         telefono,
                                                         numCamas)
                print_cabecera(" Insertar hospital ")
                print(f"Numero de registros insertados: {insertados}\n")
            case 4:
                # Modificar hospital
                print_cabecera(" Modificar hospital ")
                print("Introduzca un código de hospital: ")
                idHosp = int(input())
                print("Introduzca el nuevo nombre del hospital: ")
                nombre = input()
                print("Introduzca la nueva dirección del hospital: ")
                direccion = input()
                print("Introduzca el nuevo teléfono del hospital: ")
                telefono = input()
                print("Introduzca el nuevo número de camas del hospital: ")
                numCamas = int(input())
                modificados = miServicio.modificarHospital
                (idHosp, nombre, direccion, telefono, numCamas)
                print_cabecera(" Modificar hospital ")
                print(f"Numero de registros modificados: {modificados}")
            case 5:
                # Borrar hospital por id
                print_cabecera(" Borrar hospital ")
                print("Introduzca un código de hospital: ")
                idHosp = int(input())
                eliminados = miServicio.eliminarHospital(idHosp)
                print(f"Número de registros eliminados {eliminados}\n")
        print("Pulse X para salir u otra tecla cualquiera para volver al menú")
        ctrlWhile = input().upper()
    system("clear")
    print("Fin del programa")


main()
