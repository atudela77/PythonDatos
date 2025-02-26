# Este servicio es el que tendrá métodos para ser utilizados en el main
from models import mascota


def getSaludo():
    return "Bienvenido a SQL Server"


def getMascota1():
    dato = mascota.Mascota()
    dato.nombre = "Patricio"
    dato.raza = "EStrella de mar"
    dato.edad = 8
    return dato


def getMascota2():
    dato = mascota.Mascota()
    dato.nombre = "Bob"
    dato.raza = "Esponja"
    dato.edad = 10
    return dato
