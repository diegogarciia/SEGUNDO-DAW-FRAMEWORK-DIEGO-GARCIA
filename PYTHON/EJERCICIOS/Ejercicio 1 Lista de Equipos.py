equipos = ["Real Madrid", "FC Barcelona", "Atlético de Madrid", "Valencia", "Mallorca"]

primerclasificado = equipos[0]
ultimoclasificado = equipos[-1]

print("Primer clasificado:")
print(primerclasificado)
print("Ultimo clasificado:")
print(ultimoclasificado)

equipos.append("Sevilla FC")

equipos.insert(0, "Celta de Vigo")

equipos.remove("Valencia")

print()
print(equipos)