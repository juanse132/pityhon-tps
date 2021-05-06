def letras_consonantes():
    """
    Devuelo las letras consonantes de una cadena string ingresada por el usuario
    """
    cadena_consonante = str(input("Ingrese una cadena para devolver consonantes: "))
    cadena_final = " "
    for letra in cadena_consonante:  # recorre la cadena tantas letras tenga la cadena
	    if letra.lower() not in  "aeiou":  # voy comparando letras de la cadena con las consonantes
		    cadena_final += letra
    return cadena_final


def letras_vocales(cant_espacios):
    """
    Devuelvo las vocales de una cadena string ingresada por un usuario
    """
    cadena_vocal = str(input("Ingrese una cadena para devolver vocales:"))
    cadena_final = ""
    for letra in cadena_vocal:  # recorre la cadena tantas letras tenga la cadena
        if letra.lower() in "aeiou " :  # voy comparando letras de la cadena con las vocales 
            if letra == " ":
                letra *= 3 
            cadena_final += letra
    return cadena_final


print(letras_vocales(3))


def reemplazar_vocales():
    """
    Devuelo la siguiente vocal que haya en una cadena string que haya ingresado el usuario
    """
    cadena_vocal = str(input("Ingrese una cadena para reemplazar vocales:"))
    cadena_final = ""
    for letra in cadena_vocal:  # voy comparando letras de la cadena con las vocales y si hay cambio esa vocal por la siguiente
        if letra in"aA":
            cadena_final += "e"
        elif letra in "eE":
            cadena_final += "i"
        elif letra in "iI":
            cadena_final += "o"
        elif letra in "oO":
            cadena_final += "u"
        elif letra in "uU":
            cadena_final += "a"
        else:
            cadena_final += letra
    return cadena_final


def capicua():
    """
    Devuelvo True si la cadena string ingresada por el usuario es palindromo 
    """
    cadena_capicua = str(input("Ingrese una cadena para saber si es capicua o no:").lower())
    cadena_capicua = cadena_capicua.replace(" ", "") 
    if cadena_capicua == cadena_capicua[::-1]:  # si es igual de tanto como de izquierda a derecha como de derecha a izquierda
        return True
    else:
        return False
        



