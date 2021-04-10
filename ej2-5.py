def area_circulo():
    from math import pi
    r = int(input("ingrese el radio del circulo: "))
    a = pi * r ** 2 # calculo del area del circulo
    return f"El area del circulo: {a}"


print(area_circulo())     
