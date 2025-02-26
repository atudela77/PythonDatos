# Importamos la clase de servicio y le ponemos un alias
from services import service04oracledepartamentos as servicio
from models import departamento
from os import system
system("clear")
print("------ Servicio Oracle Departamentos ------")
# Creamos un objeto de tipo servicio para tener la conexión
miServicio = servicio.ServiceOracleDepartamentos()
# Solicitamos toda la información necesaria al usuario
print("1. Insertar departamento")
print("2. Buscar departamento")
print("3. Eliminar departamento")
print("Seleccione una opción")
opcion = int(input())
if (opcion == 1):
    system("clear")
    print(">>>>> Insertar departamento <<<<<")
    print("Id del departamento")
    numero = int(input())
    print("Nombre del departamento")
    nombre = input()
    print("Localidad")
    localidad = input()
    # Ejecutamos le método correspondiente de nuestro objeto
    insertados = miServicio.insertarDepartamento(numero, nombre, localidad)
    # Mostramos el resultado del insert
    print(f"Departamentos insertados: {insertados}")
elif (opcion == 2):
    system("clear")
    print(">>>>> Buscar departamento <<<<<")
    print("Id del departamento")
    numero = int(input())
    dept = miServicio.buscarDepartamento(numero)
    print(f"Id: {dept.numero}  Nombre: {dept.nombre} "
          f"Localidad: {dept.localidad}")
elif (opcion == 3):
    system("clear")
    print(">>>>> Eliminar departamento <<<<<")
    print("Id del departamento")
    numero = int(input())
    eliminados = miServicio.eliminarDepartamento(numero)
    print(f"Departamentos eliminados: {eliminados}")

print("Fin del programa")
