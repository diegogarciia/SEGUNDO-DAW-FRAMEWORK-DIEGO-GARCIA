import random

from clases.persona import Persona

class Heroe(Persona):

    def __init__ (self, nombre, apellidos, fecha_nacimiento, identificador):
        super().__init__(nombre, apellidos, fecha_nacimiento, identificador)
        self.codigo_limpio = random.randint(0, 100)
        self.bien_documentado = random.randint(0, 100)
        self.GITGod = random.randint(0, 100)
        self.arquitecto = random.randint(0, 100)
        self.detallista = random.randint(0, 100)
        self.calcular_puntuacion()

    def calcular_puntuacion(self):
        self.puntuacion_total = (self.codigo_limpio + self.bien_documentado + self.GITGod + self.arquitecto + self.detallista) / 5