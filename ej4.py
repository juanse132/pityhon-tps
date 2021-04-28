def celsius_Fahrenheit():
    f = int(input("ingrese un valor de grados Fahrenheit: "))
    c = (f/(9/5)) - 32  # saco la conversion a grados celsisus
    return f"los grados celsius son: {c}"  # devuelvo los celsius


print(celsius_Fahrenheit())
