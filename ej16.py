def letras_consonantes():
    cadena_consonante = str(input("ingrese una cadena para devolver consonantes: "))
    cadena_final = " "
    for letra in cadena_consonante:  # recorre la cadena tantas letras tenga la cadena
	    if letra.lower() not in  "aeiou":  # voy comparando letras de la cadena con las consonantes
		    cadena_final += letra
    return cadena_final


def letras_vocales():
    cadena_vocal = str(input("ingrese una cadena para devolver vocales:"))
    cadena_final = ""
    for letra in cadena_vocal:  # recorre la cadena tantas letras tenga la cadena
        if letra.lower() in "aeiou " :  # voy comparando letras de la cadena con las vocales 
            cadena_final += letra
    return cadena_final

def reemplazar_vocales():
    cadena_vocal = str(input("ingrese una cadena para reemplazar vocales:"))
    cadena_final = ""
    for letra in cadena_vocal:  # voy comparando letras de la cadena con las vocales y si hay cambio esa vocal por la siguiente
        if letra.lower() == "a":
            cadena_final += "e"
        elif letra.lower() == "e":
            cadena_final += "i"
        elif letra.lower() == "i":
            cadena_final += "o"
        elif letra.lower() == "o":
            cadena_final += "u"
        elif letra.lower() == "u":
            cadena_final += "a"
        else:
            cadena_final += letra
    return cadena_final

def capicua():
    cadena_capicua = str(input("ingrese una cadena para saber si es capicua o no:").lower())
    cadena_capicua = cadena_capicua.replace(" ", "")  # saco los espacios entre la cadena
    if cadena_capicua == cadena_capicua[::-1]:  # si es igual de tanto como de izquierda a derecha como de derecha a izquierda
        return True
    else:
        return False
        






