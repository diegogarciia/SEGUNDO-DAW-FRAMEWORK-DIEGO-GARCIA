print("hola")
import calculadora as pruebaCalculadora
#COMENTARIO

resultado = 10
print(resultado)


#FLOAT PARA CASTEAR
a = float(input("dame un numero"))
a = a + 10
print(a)


def miPrimerMetodo():
    nombre = "Diego"
    apellido = "García"
    print(nombre + apellido)
miPrimerMetodo()

pruebaCalculadora.sumar()

#CONDICIONALES

a = 20

if a > 20:
    print("Hola")
    if a > 100:
        print("Qué grande eres")
    elif a < 100:
            print("No eres tan grande")
else:
    print("Adios")