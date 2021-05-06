def perimetro_circulo():
    """
    Calculo el perimetro de un circulo,recibiendo el radio del circulo
    """
    pi = 3.14
    r = int(input("Ingrese el radio del circulo: "))
    p = 2 * pi * r  # calculo el perimetro 
    return f"El perimetro del circulo: {p}"


print(perimetro_circulo())