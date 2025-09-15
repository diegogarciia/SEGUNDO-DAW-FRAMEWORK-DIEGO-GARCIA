'''Empieza a hacerlo aquí'''

import datetime
import os

# 1. Nombre del archivo de salida con fecha actual
fecha_actual = datetime.datetime.now().strftime("%d%m%Y")
nombre_fichero = f"{fecha_actual}_Personas.log"

# 2. Función para leer el .txt (campos separados por tabuladores)
def leer_datos_txt(ruta_txt):
    datos = []
    with open(ruta_txt, "r", encoding="utf-8") as f:
        for linea in f:
            campos = linea.strip().split("\t")
            if len(campos) >= 7:
                datos.append(campos[:7])
    return datos

# 3. Función para generar los INSERT
def generar_inserts(datos):
    inserts = []
    for d in datos:
        nombre, apellidos, edad, calle, cp, numero, movil = d
        insert = (
            f"INSERT INTO Personas (id, Nombre, Apellidos, fecha_nacimiento, calle, codigo_postal, numero, movil) "
            f"VALUES (seq_personas.nextval, '{nombre}', '{apellidos}', '{edad}', '{calle}', '{cp}', '{numero}', '{movil}');"
        )
        inserts.append(insert)
    return inserts

# 4. Guardar en el fichero log
def guardar_en_log(nombre_fichero, inserts):
    with open(nombre_fichero, "w", encoding="utf-8") as f:
        for ins in inserts:
            f.write(ins + "\n")

# 5. Ejecución principal
if __name__ == "__main__":
    ruta_txt = "Libro2.txt"  # pon aquí la ruta correcta
    if os.path.exists(ruta_txt):
        datos = leer_datos_txt(ruta_txt)
        inserts = generar_inserts(datos)
        guardar_en_log(nombre_fichero, inserts)
        print(f"Archivo {nombre_fichero} creado con {len(inserts)} inserts.")
    else:
        print("El archivo de entrada no existe.")
