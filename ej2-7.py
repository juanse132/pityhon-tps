def hipotenusa_triangulo():
    c1 = int(input("Ingrese el cateto 1: "))
    c2 = int(input("Ingrese el cateto 2: "))
    h = (c1 ** 2 + c2 ** 2) ** 0.5  # calculo la hipotenusa
    return f"La hipotenusa del triangulo es: {h}"  # devuelvo la hipotenusa


print(hipotenusa_triangulo())