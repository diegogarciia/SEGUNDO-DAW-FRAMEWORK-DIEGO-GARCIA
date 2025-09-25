from persona import Persona

class Jugador(Persona):
    def __init__(self, nombre, apellidos, fecha_nacimiento, identificador):
        super().__init__(nombre, apellidos, fecha_nacimiento, identificador)
        self.chagepeteador = 0
        self.entregador_tardio = 0
        self.ausencias = 0
        self.hablador = 0
        self.calcular_puntuacion()

    def calcular_puntuacion(self):
        self.puntuacion_total = (self.chagepeteador + self.entregador_tardio +
                                 self.ausencias + self.hablador) / 4