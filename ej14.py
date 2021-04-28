print("Bienvenido al juego de Mastermind")
import time
time.sleep(1.5)
print("Usted debera adiviniar un numero de 4 cifras secreto ya creado")
time.sleep(2)
print("""
REGLAS:
Se debe ingresar otro numero de 4 cifras.
Si en el numero que ingresaste,un numero coincide y esta en la misma posicion cuenta como acierto.
Y si esta pero en otra posicion cuenta como coincidencia.
""")
time.sleep(8)
print("A jugar!!!")

numeroAleatorio = []
aciertos = 0 
coincidencias = 0
intentos = 0
import random

numeroUsuario = str(input("ingrese el numero que cree que es correcto "))
if  0 <= len(numeroUsuario) <= 3:
    for i in range(0, 4):
        numeroAleatorio.append(random.randrange(0, 9)) # genero un numero ramdom
    while numeroAleatorio[0] in (numeroAleatorio[1], numeroAleatorio[2], numeroAleatorio[3]):  # verifico que sea distinto el primero de todos
        numeroAleatorio[0] = random.randrange(0, 9)
    while numeroAleatorio[1] in (numeroAleatorio[2], numeroAleatorio[3]):  # verifico que sea distinto el segundo de todos
        numeroAleatorio[1] = random.randrange(0, 9)
    while numeroAleatorio[2] == numeroAleatorio[3]:  # verifico que sea distinto el tercero de todos
        numeroAleatorio[2] = random.randrange(0, 9)

    numeroAleatorio = [str(item) for item in numeroAleatorio]  # agarro de item en item y lo transformo a str
    numeroAleatorio = "".join(numeroAleatorio)  # junto los 4 items de la lista en uno

    while numeroUsuario != numeroAleatorio:  # repito esto hasta que el usuario escriba bien el numero secreto
        for i in range(0, 4):
            if numeroUsuario[i] == numeroAleatorio[i]:  # comparo si es igual el primer digito con el digito del nro secreto y asi
                aciertos += 1
            elif numeroUsuario[i] in numeroAleatorio:  # busco si hay un digito del nro del usuario en el numero secreto 
                coincidencias += 1
        print("tiene: ", aciertos, " aciertos y", coincidencias, "coincidencias")
        intentos += 1
        aciertos = 0 
        coincidencias = 0
        numeroUsuario = str(input("ingrese el numero que cree que es correcto "))
    print("Es el mismo numero que el secreto y ganaste en:", intentos, "intentos")
else:
    print("numero invalido")
    

