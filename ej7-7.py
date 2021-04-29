dia = int(input("Ingrese el dia "))
mes = int(input("Ingrese el mes "))
year = int(input("Ingrese el año "))
dia2 = int(input("Ingrese el dia2 "))
mes2 = int(input("Ingrese el mes2 "))
year2 = int(input("Ingrese el año2 "))

def dos_fechas(dia, mes, year, dia2, mes2, year2):
    from datetime import date
    fecha = date(year, mes , dia)#cargo la prierma fecha
    otra_fecha = date(year2 , mes2 , dia2)#cargo la segunda fecha
    diferencia = otra_fecha - fecha#calculo la diferencia
    print("numero de dias es ", diferencia.days)#printeo los dias
    print("numero de meses es " , "{0:.2f}" .format(diferencia.days / 30.44))#printeo los meses
    print("numero de años es ", "{0:.2f}" .format(diferencia.days / 365))# y printeo los años
    return diferencia # y ya aca devuelo lo que valdria diferencia


print(dos_fechas(dia,mes,year,dia2,mes2,year2))