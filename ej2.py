def perimetro_rectangulo():
    """
    Calculo el perimetro de un rectangulo
    """
    h = int(input("Ingrese la altura: "))  # pido la altura del rectangulo
    b = int(input("Ingrese la base: "))  # pido la base del rectangulo
    p = h * 2 + b * 2  # calculo el perimetro
    return f"El perimetro del rectangulo dado es: {p}" 


print(perimetro_rectangulo())
