from random import randrange
import random

x=(random.randrange(30)) # establezco un nro aleatorio entre 30 y 0
cont = 0
numero = 0
while numero != x:  # repito esto hasta que el numero sea igual al secreto
    numero = int(input("Ingrese un numero: "))   
    if numero > x:
        cont += 1
        print("El numero es mas chico")
    elif numero < x:
        cont += 1
        print ("El numero es mas grande")
    elif numero == x:
        print("El numero a diviniar fue: ", x, " y acertaste en el intento numero:", cont)
        break

