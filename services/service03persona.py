from models import persona


def getPersona():
    person = persona.Persona()
    person.nombre = "Sussie"
    person.edad = 51
    person.email = 'sussie.derkins@mail.com'
    return person
