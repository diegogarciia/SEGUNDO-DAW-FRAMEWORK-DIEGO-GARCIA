import random

from clases.persona import Persona

class Villano(Persona):

    def __init__(self, nombre, apellidos, fecha_nacimiento, identificador):
        super().__init__(nombre, apellidos, fecha_nacimiento, identificador)
        self.chagepeteador = random.randint(0, 100)
        self.entregador_tardio = random.randint(0, 100)
        self.ausencias = random.randint(0, 100)
        self.hablador = random.randint(0, 100)
        self.calcular_puntuacion()

    def calcular_puntuacion(self):
        self.puntuacion_total = (self.chagepeteador + self.entregador_tardio + self.ausencias + self.hablador) / 4