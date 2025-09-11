locales = ["Real Madrid", "Barcelona", "Atlético", "Sevilla", "Valencia"]
visitantes = ["Athletic", "Betis", "Cádiz", "Villareal", "Osasuna"]

locales.remove("Sevilla")
visitantes.remove("Villareal")
locales.append("Oviedo")
visitantes.append("Getafe")

print("PARTIDOS DE LA JORNADA:\n")
num = 0
while num < len(locales):
    print(locales[num] + " vs " + visitantes[num])
    num += 1
