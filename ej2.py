def perimetro_rectangulo():
    """
    Calculo el perimetro de un rectangulo dado la base y la altura
    """
    h = int(input("Ingrese la altura: "))
    b = int(input("Ingrese la base: ")) 
    p = h * 2 + b * 2  # calculo el perimetro
    return f"El perimetro del rectangulo dado es: {p}" 


print(perimetro_rectangulo())
