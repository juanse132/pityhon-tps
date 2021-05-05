def area_rectangulo2():
    """
    Calculo el area de un rectangulo dado 4 puntos
    """
    x1 = int(input("Ingrese x-1: "))
    x2 = int(input("Ingrese x-2: "))
    b = x2 - x1  # una vez pedidos los inputs saco la base
    y1 = int(input("Ingrese y-1: "))
    y2 = int(input("Ingrese y-2: "))
    h = y2 - y1  # una vez pedidos los inputs saco la altura

    return f"El area del rectangulo dado es: {b * h}"


print(area_rectangulo2())