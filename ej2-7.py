def hipotenusa_triangulo():
    c1 = int(input("ingrese el cateto 1: "))
    c2 = int(input("ingrese el cateto 2: "))
    h = (c1 ** 2 + c2 ** 2) ** 0.5
    return f"La hipotenusa del triangulo es: {h}" # devuelvo la p


print(hipotenusa_triangulo())