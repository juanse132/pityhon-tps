entero = int(input("Ingrese un entero: "))

def entero_romano(entero):
    """
    Lo que hace esta funciones es pedirle un entero al usuario y le muestra el equivalente pero en numeros romanos 
    urilizando una lista en la que contiene enteros que son convertibles a numeros romanos
    """
    
    numeros = [1000 , 900 , 500 , 400 , 100 , 90 , 50 , 40 , 10 , 9 , 5 , 4 , 1]
    letras_romanas = ["M" , "CM" , "D" , "CD" , "C" , "XC" , "L" , "XL" , "X" , "IX" , "V" , "IV" , "I"]

    conversion= " "
    i = 0
    numero_ingresado = entero  # guardo el entero en una var para luego mostrar la conversion
    while entero > 0:
        for _ in range(entero // numeros[i]):
            conversion += letras_romanas[i]
            entero -= numeros[i]

        i += 1
    print("La conversion de:", numero_ingresado, " a numeros romanos es:", conversion)
    return conversion


print(entero_romano(entero))