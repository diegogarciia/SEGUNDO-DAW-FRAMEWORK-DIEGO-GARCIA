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

#LISTAS

listacompra = ["Manzana", "Plátano", "Sandía"]
print(listacompra)

print(len(listacompra)) #va a imprimir la cantidad de elementos que hay en la lista
print(type(listacompra)) #devuelve el tipo de los elementos de la lista

#WHILE

i = 1
while i < 5:
    print(i)
    i += 1
else:
    print("i no es mayor que 5")

#ARRAYS

coches = ["Toyota", "Kia", "Ford"]
x = coches[0]
coches[1] = "BMW"
y = len(coches)

for elemento in coches:
    print(elemento)

coches.append("Hyundai")
coches.pop(3)
coches.remove("Kia")

#REPASO INPUT

nombre = input("Nombre: ")
print("Hola {nombre}")
numerofavorito = input("¿Cuál es tu número favorito?")

#TRY EXCEPT

try:
    print("Hola a todos")
except:
    print("Algo ha salido mal")
else:
    print("Ha salido todo correcto")

try:
    print("Hola")
except:
    print("Algo ha salido mal")
finally:
    print("Ha salido todo correcto")