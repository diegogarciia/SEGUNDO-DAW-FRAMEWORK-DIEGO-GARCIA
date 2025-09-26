from clases.heroe import Heroe
from clases.villano import Villano

def crear_personaje(tipo, nombre, apellidos, fecha_nacimiento, identificador):
    if tipo == "heroe":
        return Heroe(nombre, apellidos, fecha_nacimiento, identificador)
    elif tipo == "villano":
        return Villano(nombre, apellidos, fecha_nacimiento, identificador)
    else:
        raise ValueError("Tipo no válido. Usa 'heroe' o 'villano'")