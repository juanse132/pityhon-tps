def area_circulo():
    pi = 3.14
    r = int(input("ingrese el radio del circulo: "))
    a = pi * r ** 2  # calculo del area del circulo
    return f"El area del circulo: {a}"


print(area_circulo())     
