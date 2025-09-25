from persona import Persona

class Heroe(Persona):

    def __init__ (self, nombre, apellidos, fecha_nacimiento, identificador):
        super().__init__(nombre, apellidos, fecha_nacimiento, identificador)
        self.codigo_limpio = 0
        self.bien_documentado = 0
        self.GITGod = 0
        self.arquitecto = 0
        self.detallista = 0
        self.calcular_puntuacion()

    def calcular_puntuacion(self):
        self.puntuacion_total = (self.codigo_limpio + self.bien_documentado +
                                 self.GITGod + self.arquitecto + self.detallista) / 5