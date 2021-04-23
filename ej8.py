entero = int(input("ingrese un entero: "))

def entero_romano(entero):
    numeros = [1000 , 900 , 500 , 400 , 100 , 90 , 50 , 40 , 10 , 9 , 5 , 4 , 1]
    letras_romanas = ["M" , "CM" , "D" , "CD" , "C" , "XC" , "L" , "XL" , "X" , "IX" , "V" , "IV" , "I"]

    conversion= " "
    i = 0
    numero_ingresado = entero # guardo el entero en una var para luego mostrar la conversion
    while entero > 0: #se ejecuta este while hasta el entero sea 0 ,ya que entero > 0 da false
        for _ in range(entero // numeros[i]):
            conversion += letras_romanas[i]
            entero -= numeros[i]

        i += 1
        """En este for recorre a numeros hasta que encuntre uno que al dividirlo me de un entero,
        luego se le concatena a conversion lo que haya en la iesima posicion de letras_romanas,
        se le resta a entero lo que haya en la iesima posicion de la lista numeros y por ultimo
        se le suma 1 a lo que ya tenga de i  """
    print("la conversion de:",numero_ingresado , " a numeros romanos es:",conversion)
    return conversion


print(entero_romano(entero))

