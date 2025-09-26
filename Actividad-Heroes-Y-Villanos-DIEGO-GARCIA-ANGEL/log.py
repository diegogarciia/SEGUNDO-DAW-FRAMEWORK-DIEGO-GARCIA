'''En esta clase hacer toda la gestion del log'''
from datetime import datetime

fecha = datetime.now().strftime("%d%m%Y").lower()
nombre_fichero = f"log/{fecha}_HEROESYVILLANOS.log"

import logging
import os

os.makedirs("log", exist_ok=True)  # aseguramos la carpeta log

logging.basicConfig(
    filename=nombre_fichero,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class Log:
    def info(self, mensaje):
        logging.info(mensaje)

    def error(self, mensaje):
        logging.error(mensaje)

    def warning(self, mensaje):
        logging.warning(mensaje)