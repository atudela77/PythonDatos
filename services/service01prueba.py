# Este servicio es el que tendrá métodos para ser utilizados en el main
from models import mascota


def getSaludo():
    return "Bienvenido a Matrix"


def getMascota1():
    dato = mascota.Mascota()
    dato.nombre = "Flounder"
    dato.raza = "Pez"
    dato.edad = 22
    return dato


def getMascota2():
    dato = mascota.Mascota()
    dato.nombre = "Bobby"
    dato.raza = "Perro"
    dato.edad = 10
    return dato
