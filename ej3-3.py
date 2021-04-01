def area_rectangulo2():
    x1 = int(input("ingrese x-1: "))
    x2 = int(input("ingrese x-2: "))
    b = x2 - x1
    y1 = int(input("ingrese y-1: "))
    y2 = int(input("ingrese y-2: "))
    h = y2 - y1

    return f"El area del rectangulo dado es: {b * h}"


print(area_rectangulo2())
