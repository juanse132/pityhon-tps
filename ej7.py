dia = int(input("Ingrese el dia "))
mes = int(input("Ingrese el mes "))
year = int(input("Ingrese el año "))

def bisiesto(year):
    if year > 0:
        if (year % 400 == 0 or year % 100 == 0 or year %4 == 0):
            return True
            #En el primer if hago si el year es bisiesto
        elif(year % 4 != 0 and year % 400 != 0):
            return False
            #Y en este if hago si no es bisiesto
    else:
        return False

def cantidad_dias(mes):
    if  mes in (1 , 3, 5 , 7 , 8 , 10 , 12 ): 
        return 31
        #En el primer if comparo el input con los meses que tienen 31
    elif mes == 2:
        if bisiesto(year):
            return 29
        else:
            return 28
        #En el segundo if comparo el input con los meses que tienen 28/29
    else: 
        return 30

def validar_fecha(dia,mes,year):
    total = cantidad_dias(mes)
    if 0 <= dia <= total: #En el primer if comparo valido los dias
        if 0 <= mes <= 12: #En el segundo if valido los meses
            if year > 0: #En el ultimo if valido el año
                return True
            else:
                return False
        else:
            return False
    else:
        return False

def dias_mes(dia,mes,year):
    if validar_fecha(dia,mes,year): #valido la fecha
        total = cantidad_dias(mes) #guardo en la var el return de lo que vale mes
        dias_restantes = total - dia #calculo los dias restantes
        return dias_restantes
    else:
        print("fecha invalida")
        return False

def dias_year(dia,mes,year):
    if validar_fecha(dia,mes,year): #valido la fecha
        dias_totales = 0
        dias_anteriores = 0    
        if bisiesto(year): #valido el año bisiesto
            dias_totales = 366
        else:
            dias_totales = 365   
        for i in range(1 , mes): #recorro desde 1 hasta el nro que ingreso la persona de mes    
            dias_anteriores += cantidad_dias(i) #suma los returns de los diferesnts dias a la var
        else:
            resultado = dias_totales - dias_anteriores - dia #calculo los dias que faltan hasta fin de año
            print("quedan" , resultado ,  "para que finalize el año")
            return resultado
    else:
        return False

def dias_fecha(dia,mes,year):
    if validar_fecha(dia,mes,year): #valido la fecha
        dias_anteriores = 0    
        for i in range(1 , mes): #recorro desde 1 hasta el nro que ingreso la persona de mes    
            dias_anteriores += cantidad_dias(i) #suma los returns de los diferesnts dias a la var
        else:
            resultado = dias_anteriores + dia #calculo los dias hasta la fecha
            print("pasaron" , resultado ,  "dias hasta la fecha")
            return resultado
    else:
        return False

