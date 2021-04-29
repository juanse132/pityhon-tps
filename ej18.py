lista_inicial = ["Di", "buen", "dia", "a", "papa"]
lista_final = ["", "", "", "", ""]

def vuelta_listas(lista_inicial,lista_final):
    cont = 0
    for palabra  in lista_inicial[::-1]:  # recorro la lista de izquierda a derecha
        lista_final[cont] += palabra  # concateno lo que vale la palabra a la posicion de la lista final
        cont += 1
    return lista_final


def lista_modificada(lista_inicial):

    lista_inicial = lista_inicial[4::-1]  # pongo en la lista inicial desde la posicion final de la misma hasta el inicio dando saltos de -1   

    return lista_inicial


print(lista_modificada(lista_inicial))

