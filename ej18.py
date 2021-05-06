frase_inicial = str(input("ingrese una frase para que luego sea invertida: "))
lista_inicial = frase_inicial.split(" ")

def vuelta_listas(lista_inicial):
    """
    Devuelvo una lista string ingresada por el usuario pero dada vuelta utilizando una lista auxiliar 
    """
    lista_final = [""]
    for palabra  in lista_inicial[::-1]:  # recorro la lista de izquierda a derecha
        lista_final += palabra + " "  # concateno lo que vale la palabra a la posicion de la lista final
    return "".join(lista_final)


print(vuelta_listas(lista_inicial))


def lista_modificada(lista_inicial):
    """
    Devuelvo una lista string ingresada por el usuario pero dada vuelta en una sola linea
    """
    lista_inicial = lista_inicial[4::-1]  # pongo en la lista inicial desde la posicion final de la misma hasta el inicio dando saltos de -1   

    return lista_inicial


