dia = int(input("Ingrese el dia "))
mes = int(input("Ingrese el mes "))
year = int(input("Ingrese el año "))
dia2 = int(input("Ingrese el dia2 "))
mes2 = int(input("Ingrese el mes2 "))
year2 = int(input("Ingrese el año2 "))
Dias_bisiesto = 366
Dias_no_bisiesto = 365

def bisiesto(year):
    """
    Saco si un año es bisiesto o no 
    """
    if year > 0:
        if (year % 400 == 0 or year % 100 == 0 or year %4 == 0):
            return True
            # En el primer if hago si el year es bisiesto
        elif(year % 4 != 0 and year % 400 != 0):
            return False
            # Y en este if hago si no es bisiesto
    else:
        return False


def cantidad_dias(mes):
    """
    saco la cantidad de dias que tiene un mes  
    """
    if  mes in (1, 3, 5, 7, 8, 10, 12 ): 
        return 31
        # En el primer if comparo el input con los meses que tienen 31
    elif mes == 2:
        if bisiesto(year):
            return 29
        else:
            return 28
        # En el segundo if comparo el input con los meses que tienen 28/29
    else: 
        return 30


def validar_fecha(dia, mes, year):
    """
    Valido una fecha 
    """
    total = cantidad_dias(mes)
    if 0 <= dia <= total:  # En el primer if comparo valido los dias
        if 0 <= mes <= 12:  # En el segundo if valido los meses
            if year > 0:  # En el ultimo if valido el año
                return True
            else:
                return False
        else:
            return False
    else:
        return False


def dias_mes(dia, mes, year):
    """
    Saco la cantidad de dias que faltan hasta fin de ese mes 
    """
    if validar_fecha(dia, mes, year):  # valido la fecha
        total = cantidad_dias(mes)  # guardo en la var el return de lo que vale mes
        dias_restantes = total - dia  # calculo los dias restantes
        return dias_restantes
    else:
        print("Fecha invalida")
        return False


def dias_faltantes_year(dia, mes, year):
    """
    Saco la cantidad de dias que faltan hasta fin de ese año
    """
    if validar_fecha(dia, mes, year):  # valido la fecha
        dias_totales = 0
        dias_anteriores = 0    
        if bisiesto(year):  # valido el año bisiesto
            dias_totales = dias_bisiesto
        else:
            dias_totales = dias_no_bisiesto
        for i in range(1, mes):    
            dias_anteriores += cantidad_dias(i)  # suma los returns de los diferesnts dias a la var
        else:
            resultado = dias_totales - dias_anteriores - dia  # calculo los dias que faltan hasta fin de año
            print("Quedan", resultado, "para que finalize el año")
            return resultado
    else:
        return False


def dias_fecha(dia, mes, year):
    """
    Saco la cantidad de dias (en el mismo año) que transcurrieron hasta la fecha que ingresa el usuario 
    """
    if validar_fecha(dia, mes, year):  # valido la fecha
        dias_anteriores = 0    
        for i in range(1, mes):  # recorro desde 1 hasta el nro que ingreso la persona de mes    
            dias_anteriores += cantidad_dias(i)  # suma los returns de los diferesnts dias a la var
        else:
            resultado = dias_anteriores + dia  # calculo los dias hasta la fecha
            print("Pasaron", resultado, "dias hasta la fecha")
            return resultado
    else:
        return False


def diferencia_years(dia, mes, year, dia2, mes2, year2):
    """
    Calculo la diferencia en dias,mes y años que hay entre 2 fechas 
    """
    years = year2 - year  # saco cuantos years hay de diferencia
    anio = 0
    meses = 0
    dias = 0 
    if validar_fecha(dia, mes, year) or validar_fecha(dia2, mes2, year2):  # valido ambas fechas
        diferencia_dias = dias_faltantes_year(dia, mes, year) + dias_fecha(dia2, mes2, year2)  # sumo los dias entre las fechas dadas
        for i in range(1,years):
            diferencia_dias += 365  # le sumo a diferencia_dias 365 que es el promedio que hay de dias en los years transcurridos
        while diferencia_dias != 0:
            if diferencia_dias - 365 >= 0:  # saco los years que hay en esa diferencia_dias
                diferencia_dias = diferencia_dias - 365
                anio = anio + 1
            elif diferencia_dias - 30 >= 0:  # saco los meses que hay en esa diferencia_dias
                diferencia_dias = diferencia_dias - 30
                meses = meses + 1
            elif diferencia_dias - 1 >= 0:  # saco los dias que hay en esa diferencia_dias
                diferencia_dias = diferencia_dias - 1
                dias = dias + 1
        
        return f"""El tiempo transcurrido entre las fechas es:  
{anio} years, {meses} meses y {dias} dias """


print(diferencia_years(dia, mes, year, dia2, mes2, year2))