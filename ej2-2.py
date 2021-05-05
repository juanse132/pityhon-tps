def area_rectangulo():
    """
    Calculo el area de un rectangulo
    """
    h = int(input("Ingrese la altura: "))
    b = int(input("Ingrese la base del rectangulo: "))
    p = h * b  # calculo el perimetro
    return p


print(area_rectangulo())