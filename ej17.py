cadena = str(input("Ingrese una cadena:"))
long_palabra = int(input("Ingrese la maxima cantidad de letras por palabra:"))
costo_palabra_corta = int(input("Ingrese el costo de las palabras cortas: $"))
costo_palabra_larga = int(input("Ingrese el costo de las palabras largas: $"))

def arroba_letras(cadena, long_palabra, costo_palabra_corta, costo_palabra_larga):
    """
    Devuelvo la cadena y si hay un punto lo reemplazo por un STOP y si en la cadena
    una palabra tiene mas del maximo de letras pre-elegidas,entonces se corta hasta ese maximo y luego se le pone un @ 
    y alfinal devuelo esa cadena con las modificaciones ya hechas
    """
    palabras = cadena.split(" ")
    frase_final = ""
    costo_total = 0
    for i in range(len(palabras)):
        if len(palabras[i]) > long_palabra:#verificio si la longitud de esa palabra cortada es menor a lo previamente establecido
            frase_final += palabras[i][0:long_palabra] + "@ "  # corto la palabra en la posicion max y agrego un @
            costo_total += costo_palabra_corta
            if palabras[i][-1] == ".":  # veo si en la palabra corta cortada hay un punto y si lo lo borro y reemplazo por un STOP
                frase_final = frase_final.strip() + palabras[i].replace(palabras[i], " STOP ")
        elif palabras[i][-1] == ".":  # veo si en la palabra larga cortada hay un punto y si lo hay lo borro y lo reemplazo por un STOP
            frase_final = frase_final.strip(".") + palabras[i].replace(palabras[i][-1], " STOP ")  
        else:
            frase_final += palabras[i] + " "
            costo_total += costo_palabra_larga
    frase_final += "STOPSTOP" 
    
    return f"""El telegrama final es: 
{frase_final} 
utilizando {long_palabra} letras maximas por palabra a un costo de ${costo_total} """


print(arroba_letras(cadena, long_palabra, costo_palabra_corta, costo_palabra_larga))            