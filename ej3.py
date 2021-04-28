def factorial_numero():
    n = int(input("Ingrese un numero: "))
    resultado = 0
    for iterador in range(1, n):  # recorro el for desde 1 hasta lo que se haya puesto en n
        resultado = resultado + n * iterador  # hago el factorial
    else:
        return resultado
        

print(factorial_numero())

