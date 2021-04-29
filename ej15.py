def mostrarSiglas(cadena):
    cadena_final = ""
    palabras = cadena.split(" ")  # separo la cadena 
    lista_iniciales = []
    for palabra in palabras:  # recorro la palabra separada y saco la primera letra
        lista_iniciales.append(palabra[0])
    return cadena_final.join(lista_iniciales)  # y aca devuelo la lisa convertida en str


def primera_palabra_mayuscula(cadena):
    palabras = cadena.split(" ")
    frase_final = ""
    for palabra in palabras:  # recorro la palabra separada  
        frase_final  += palabra.capitalize() + " "  # agarro la palabra separado y la primera letra la pongo en mayuscula      
    return frase_final

print((primera_palabra_mayuscula("republica argentina")))

def palabras_iniciales(cadena, letra):
    palabras = cadena.split(" ")
    palabras_iniciales = " "
    for i in palabras:
        if i[0] == letra.lower() or i[0] == letra.upper():  # comparo la primera letra con la letra si es mayuscula o minuscula
            palabras_iniciales += i + " "  # pongo las palabras acorde a la letra pre-seleccionada
    if palabras_iniciales == " ":  # Y si no hay nada con la letra pre-elejida devuelvo que no hay letra en la cadena
        print("no hay:", letra, " en:", cadena)

    return palabras_iniciales
    



