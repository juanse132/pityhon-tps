def volumen_esfera():
    from math import pi
    r = int(input("ingrese el radio del circulo: "))
    v = (4/3) * pi * r ** 3 # calculo del volumen
    return f"El volumen de la esfera: {v}"


print(volumen_esfera())