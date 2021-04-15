def bisiesto():
    year=int(input("ingrese un año: "))
    if (year % 400 == 0 or year % 100 == 0 or year %4 == 0):
        print("es bisiesto el año: ", year)
        return year
        'En el primer if hago si el year es bisiesto'
    elif(year % 4 != 0 and year % 400 != 0):
        print("el año ", year ,"no es bisiesto")
        return year
        'Y en este if hago si no es bisiesto'

def mes_dias():
    mes = str(input("Ingrese un mes: "))
    'Solo se admiten los meses en mayuscula'
    if(mes == "ENERO" or mes == "MARZO" or  mes == "MAYO" or  mes == "JULIO" or  mes == "AGOSTO" or  mes == "OCTUBRE" or  mes == "DICIEMBRE"):
        print(mes,"tiene 31 dias")
        return mes
    elif(mes == "ABRIL" or  mes == "JUNIO" or mes == "SEPTIEMBRE" or mes == "NOVIEMBRE"):
        print(mes,"tiene 30 dias")
        return mes
    else:
        print(mes,"tiene 28 dias")
        return mes
print(mes_dias())