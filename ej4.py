def celsius_fahrenheit():
    f = int(input("Ingrese un valor de grados Fahrenheit: "))
    c = (f/(9/5)) - 32  # saco la conversion a grados celsisus
    return f"Los grados celsius son: {c}"  # devuelvo los celsius


print(celsius_Fahrenheit())
