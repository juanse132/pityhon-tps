def area_circulo():
    """
    Calculo el area de un circulo dado el radio 
    """
    pi = 3.14
    r = int(input("Ingrese el radio del circulo: "))
    a = pi * r ** 2  # calculo del area del circulo
    return f"El area del circulo: {a}"


print(area_circulo())     
