from log import Log
from factoria import crear_personaje
from clases.heroe import Heroe
from clases.villano import Villano

import random

log = Log()

personajes = []

def menu():
    print("\n--- MENÚ ---")
    print("1) Crear Héroe")
    print("2) Crear Villano")
    print("3) Buscar personaje por atributo")
    print("4) Emparejar héroe y villano")
    print("5) Salir")

def gestionAulaDeHeroesYVillanos(opcion):
    if opcion == 1:
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        fecha = input("Fecha de nacimiento (dd/mm/yyyy): ")
        identificador = input("Identificador: ")
        heroe = crear_personaje("heroe", nombre, apellidos, fecha, identificador)
        personajes.append(heroe)
        log.info(f"Héroe creado: {heroe.nombre} {heroe.apellidos}")
        print(f"Héroe creado con puntuación {heroe.puntuacion_total}")

    elif opcion == 2:
        nombre = input("Nombre: ")
        apellidos = input("Apellidos: ")
        fecha = input("Fecha de nacimiento (dd/mm/yyyy): ")
        identificador = input("Identificador: ")
        villano = crear_personaje("villano", nombre, apellidos, fecha, identificador)
        personajes.append(villano)
        log.info(f"Villano creado: {villano.nombre} {villano.apellidos}")
        print(f"Villano creado con puntuación {villano.puntuacion_total}")

    elif opcion == 3:
        filtro = input("Atributo a buscar (nombre, apellidos, fecha de nacimiento, GITGod, chagepeteador...): ")
        valor = input("Valor a buscar: ")
        resultados = []
        for p in personajes:
            if hasattr(p, filtro):
                try:
                    if valor.isdigit():
                        if getattr(p, filtro) >= int(valor):
                            resultados.append(p)
                    else:
                        if getattr(p, filtro) == valor:
                            resultados.append(p)
                except Exception as e:
                    log.error(f"Error en búsqueda: {e}")

        print(f"Encontrados {len(resultados)} personajes:")
        for r in resultados:
            print(f"{r.nombre} {r.apellidos} ({r.puntuacion_total})")
        log.info(f"Búsqueda realizada en {filtro} con valor {valor}")

    elif opcion == 4:
        heroes = [p for p in personajes if isinstance(p, Heroe)]
        villanos = [p for p in personajes if isinstance(p, Villano)]
        if not heroes or not villanos:
            print("No hay héroes o villanos suficientes.")
            return
        h = random.choice(heroes)
        v = random.choice(villanos)
        dif = abs(h.puntuacion_total - v.puntuacion_total)
        if dif < 15:
            resultado = "Enfrentamiento equilibrado"
        else:
            resultado = "Gran diferencia de poder"
        print(f"{h.nombre} (Héroe) vs {v.nombre} (Villano) -> {resultado}")
        log.info(f"Emparejados {h.nombre} vs {v.nombre}: {resultado}")

    elif opcion == 5:
        print("Saliendo...")
        exit()

def main():
    try:
        while True:
            menu()
            opcion = int(input("Qué eliges: "))
            if opcion < 1 or opcion > 5:
                print("Selecciona una opción válida")
            else:
                gestionAulaDeHeroesYVillanos(opcion)
    except Exception as e:
        log.error(f"Error general: {e}")
        print(f"TODOS LOS ERRORES AL LOG {e}")

if __name__ == "__main__":
    main()
