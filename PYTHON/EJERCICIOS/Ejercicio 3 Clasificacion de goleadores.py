goles = [22, 12, 19, 5, 40, 16]

cantidadjugadores = len(goles)

print("Hay " + cantidadjugadores.__str__() + " jugadores")

goles.insert(1, 8)

print("Lista de goles ordenada de menos a mayor:")
goles.sort()
print(goles)
print("Lista de goles ordenada de mayor a menos:")
goles.reverse()
print(goles)

print("El máximo goleador metió la cantidad de " + max(goles).__str__() + " goles")
print("La cantidad de goles que metió el jugador menos goleador es de " + min(goles).__str__() + " goles\n")
media = sum(goles) / len(goles)
print("La media de goles marcados por jugador es de: " + media.__str__())

