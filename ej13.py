palabra = str(input("ingrese una palabra: "))
otra_palabra = str(input("ingrese la forma capitalizada de la anterior palabra: "))
def palabra_capital(palabra,otra_palabra):
    if palabra == palabra.lower():  # pregunto si esta en minuscula
        if otra_palabra == otra_palabra.upper():  # pregunto si esta en mayuscula
            otra_palabra = otra_palabra.lower()  # transformo otra_palabra a minuscula para comparar
            if palabra == otra_palabra:  # y aca ya comparo ambas palabras
                return True
            else:
                return False
        else:
            return False
    else:
        return False
print(palabra_capital(palabra,otra_palabra))
