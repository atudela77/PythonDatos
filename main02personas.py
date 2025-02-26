from services import service03persona as servicio
from models import persona

psn = servicio.getPersona()
print(f"Nombre: {psn.nombre}  Edad: {psn.edad}  Email: {psn.email}")
