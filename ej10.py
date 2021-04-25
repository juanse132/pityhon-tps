#numero = int(input("ingrese un numero entre 1 y 30: "))
#lista_numeros = [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30]

def buscar_numero(numero):
    izq = 0
    medio = 0
    der = numero - 1
    if 1 <= numero <= 30:
        while izq <= der:
            medio = (izq + der) / 2
            if lista_numeros[medio] == numero:
                return  medio
            elif lista_numeros[medio] > numero:
                der = medio - 1
            else:
                izq = medio + 1
        else:
            return -1
    else:
        print("numero invalido")
        return numero

import random
numero = int(input("ingrese un numero a buscar: "))
for i in range(25):
    print(random.randrange(5,numero,5), end=' ')



