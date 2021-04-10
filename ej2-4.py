def perimetro_circulo():
    from math import pi
    r = int(input("ingrese el radio del circulo: "))
    p = 2 * pi * r # calculo el perimetro 
    return f"El perimetro del circulo: {p}"


print(perimetro_circulo())
