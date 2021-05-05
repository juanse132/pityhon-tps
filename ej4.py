def celsius_fahrenheit():
    """
    Hago la conversion de fahrenheit a celcius 
    """
    f = int(input("Ingrese un valor de grados Fahrenheit: "))
    c = (f/(9/5)) - 32  # saco la conversion a grados celsisus
    return f"Los grados celsius son: {c}"  


print(celsius_Fahrenheit())
