def conservation(celsius):
    """
    Hago la conversion de celcius a fahrenheit 
    """
    f = (celsius-32) * (5/9)  # hago la conversion de celcius a fahrenheit
    return f


for celsius in range(0, 130, 10):
    cambio = (conservation(celsius))  # cargo los valores de la funcion anterior a una var.
    print(celsius, "==", "{0:.2f}" .format(cambio)) 

