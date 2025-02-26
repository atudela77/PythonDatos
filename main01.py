from services import service02prueba as service
from models import mascota

# saludo = service01prueba.getSaludo()
saludo = service.getSaludo()
print(f"Todo ok - {saludo}")

# primera = mascota.Mascota()
# pet1 = service01prueba.getMascota1()
# pet2 = service01prueba.getMascota2()
pet1 = service.getMascota1()
pet2 = service.getMascota2()
print(f"La mascota {pet1.nombre} es de un/a {pet1.raza.lower()}"
      f" y tiene {pet1.edad} años.")
print(f"La mascota {pet2.nombre} es de un/a {pet2.raza.lower()}"
      f" y tiene {pet2.edad} años.")
