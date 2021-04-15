def bisiesto():
    year=int(input("ingrese un año: "))
    if (year % 400 == 0 or year % 100 == 0 or year %4 == 0):
        print("es bisiesto el año: ", year)
        return year
    elif(year % 4 != 0 and year % 400 != 0):
        print("el año ", year ,"no es bisiesto")
        return year
print(bisiesto()) 