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

def fecha_validar():
    from datetime import date , datetime
    while True:
        fecha_str = input("ingrese fecha dd/mm/aaaa: ")
        try:
            fecha = datetime.strptime(fecha_str, '%d/%m/%Y')
        except ValueError:
            print("fecha invalida")
        else:
            print("fecha valida")
            break


def fecha_dia_mes():
    year=int(input("ingrese un año: "))
    if (year % 400 == 0 or year % 100 == 0 or year %4 == 0):
        mes = str(input("Ingrese un mes: "))
        'Solo se admiten los meses en mayuscula'
        if(mes == "ENERO" or mes == "MARZO" or  mes == "MAYO" or  mes == "JULIO" or  mes == "AGOSTO" or  mes == "OCTUBRE" or  mes == "DICIEMBRE"):
            'hay 31 dias'
            dia = int(input("ingrese un dia: "))
            if (1 <= dia <= 31):
                dias_retantes = 31 - dia
                print("quedan", dias_retantes , "meses para que finalize el mes")
            else:
                print("dia invalido")
                return dia
        elif(mes == "ABRIL" or  mes == "JUNIO" or mes == "SEPTIEMBRE" or mes == "NOVIEMBRE"):
            'hay 30 dias'
            dia = int(input("ingrese un dia: "))
            if (1 <= dia <= 30):
                dias_retantes = 30 - dia
                print("quedan", dias_retantes , "meses para que finalize el mes")
            else:
                print("dia invalido")
                return dia
        elif(mes == "FEBRERO"):
            'hay 29 dias'
            dia = int(input("ingrese un dia: "))
            if (1 <= dia <= 29):
                dias_retantes = 29 - dia
                print("quedan", dias_retantes , "meses para que finalize el mes")
            else:
                print("dia invalido")
                return dia
        else:
            print("mes invalido")
            return mes

    elif(year % 4 != 0 and year % 400 != 0):
        mes = str(input("Ingrese un mes: "))
        'Solo se admiten los meses en mayuscula'
        if(mes == "ENERO" or mes == "MARZO" or  mes == "MAYO" or  mes == "JULIO" or  mes == "AGOSTO" or  mes == "OCTUBRE" or  mes == "DICIEMBRE"):
            'hay 31 dias'
            dia = int(input("ingrese un dia: "))
            if (1 <= dia <= 31):
                dias_retantes = 31 - dia
                print("quedan", dias_retantes , "meses para que finalize el mes")
            else:
                print("dia invalido")
                return dia
        elif(mes == "ABRIL" or  mes == "JUNIO" or mes == "SEPTIEMBRE" or mes == "NOVIEMBRE"):
            'hay 30 dias'
            dia = int(input("ingrese un dia: "))
            if (1 <= dia <= 30):
                dias_retantes = 30 - dia
                print("quedan", dias_retantes , "meses para que finalize el mes")
            else:
                print("dia invalido")
                return dia
        elif(mes == "FEBRERO"):
            'hay 28 dias'
            dia = int(input("ingrese un dia: "))
            if (1 <= dia <= 28):
                dias_retantes = 28 - dia
                print("quedan", dias_retantes , " meses para que finalize el mes")
            else:
                print("dia invalido")
                return dia
        else:
            print("mes invalido")
            return mes


def fecha_year():
    year=int(input("ingrese un año: "))
    if (year % 400 == 0 or year % 100 == 0 or year %4 == 0):
        dias_finales = 366
        dia = int(input("ingrese un dia "))
        'hay que ingresar un dia entre 1 y 366 porque el year es bisiesto'
        if (1 <= dia <= 366): #aplica una validacion
            dias_restantes = dias_finales - dia
            print("quedan", dias_restantes , " dias para que finalize el year")
        else:
            print("dia invalido")
            return dia
    elif(year % 4 != 0 and year % 400 != 0):
        dias_finales = 365
        dia = int(input("ingrese un dia "))
        'hay que ingresar un dia entre 1 y 366 porque el year es bisiesto'
        if (1 <= dia <= 365): #aplica una validacion
            dias_restantes = dias_finales - dia
            print("quedan", dias_restantes ,  " dias para que finalize el year")
        else:
            print("dia invalido")
            return dia

print(fecha_year())



    







        
