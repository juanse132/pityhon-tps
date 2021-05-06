palabra = str(input("Ingrese una palabra: "))
otra_palabra = str(input("Ingrese la forma capitalizada de la anterior palabra: "))

def palabra_capital(palabra,otra_palabra):
    """
    Comparo 2 cadenas strings y devuelvo true si la segunda es la capitalizada de la primera 
    """
    if palabra == palabra.lower():  # pregunto si esta en minuscula
        if otra_palabra == otra_palabra.upper():  # pregunto si esta en mayuscula
            otra_palabra = otra_palabra.lower() 
            if palabra == otra_palabra: 
                return True
            else:
                return False
        else:
            return False
    else:
        return False


print(palabra_capital(palabra,otra_palabra))