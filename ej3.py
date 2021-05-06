def factorial_numero():
    """
    Calculo el factorial del numero que ingresa el usuario 
    """
    n = int(input("Ingrese un numero: "))
    resultado = 0
    for iterador in range(1, n):  # recorro el for desde 1 hasta lo que se haya puesto en n
        resultado = resultado + n * iterador  
    else:
        return resultado


print(factorial_numero())