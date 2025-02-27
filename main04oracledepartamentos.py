# Importamos la clase de servicio y le ponemos un alias
from services import service04oracledepartamentos as servicio
# from models import departamento
from os import system
continuar = ""
while (continuar != "X"):
    system("clear")
    print("------ Servicio Oracle Departamentos ------"+"\n")
    # Creamos un objeto de tipo servicio para tener la conexión
    miServicio = servicio.ServiceOracleDepartamentos()
    # Solicitamos toda la información necesaria al usuario
    print("1. Insertar departamento")
    print("2. Buscar departamento")
    print("3. Eliminar departamento")
    print("4. Modificar departamento")
    print("5. Mostrar todos los departamentos" + "\n")
    print("Seleccione una opción")
    opcion = int(input())
    if (opcion == 1):
        system("clear")
        print(">>>>> Insertar departamento <<<<<" + "\n")
        print("Id del departamento")
        numero = int(input())
        print("Nombre del departamento")
        nombre = input()
        print("Localidad")
        localidad = input()
        # Ejecutamos le método correspondiente de nuestro objeto
        insertados = miServicio.insertarDepartamento(numero, nombre, localidad)
        # Mostramos el resultado del insert
        print(f"Departamentos insertados: {insertados}", "\n")
    elif (opcion == 2):
        system("clear")
        print(">>>>> Buscar departamento <<<<<", "\n")
        print("Id del departamento")
        numero = int(input())
        dept = miServicio.buscarDepartamento(numero)
        if dept is not None:
            print(f"Id: {dept.numero}  Nombre: {dept.nombre} "
                  f"Localidad: {dept.localidad}" + "\n")
        else:
            print(f"No existe el departamento con id {numero}", "\n")
    elif (opcion == 3):
        system("clear")
        print(">>>>> Eliminar departamento <<<<<", "\n")
        print("Id del departamento")
        numero = int(input())
        eliminados = miServicio.eliminarDepartamento(numero)
        print(f"Departamentos eliminados: {eliminados}", "\n")
    elif (opcion == 4):
        system("clear")
        print(">>>>> Modificar departamentos <<<<<", "\n")
        print("Id del departamento")
        numero = int(input())
        print("Nuevo nombre del departamento")
        nombre = input()
        print("Nueva localidad del departamento")
        localidad = input()
        actualizados = miServicio.modificarDepartamento(numero, nombre,
                                                        localidad)
        print(f"Departamentos actualizados: {actualizados}", "\n")
    elif (opcion == 5):
        system("clear")
        print(">>>>> Mostrar todos los departamentos <<<<<", "\n")
        print("ID  NOMBRE           LOCALIDAD")
        print("--- ---------------- ----------------")
        datos = miServicio.getAllDepartamentos()
        for dept in datos:
            print(f"{dept.numero:3} {dept.nombre:16} {dept.localidad:16}")
        print("\n")

    print("Pulse cualquier tecla para volver al menú o X para terminar")
    continuar = input().upper()
system("clear")
print("Fin del programa")
