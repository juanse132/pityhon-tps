def dos_fechas():
    from datetime import date
    dia = int(input("Ingrese el dia "))
    mes = int(input("Ingrese el mes "))
    year = int(input("Ingrese el año "))
    dia2 = int(input("Ingrese el dia2 "))
    mes2 = int(input("Ingrese el mes2 "))
    year2 = int(input("Ingrese el año2 "))

    hoy = date(year, mes , dia)
    otra_fecha = date(year2 , mes2 , dia2)

    diferencia = otra_fecha - hoy

    print("numero de dias es ", diferencia.days)
    print("numero de meses es " , "{0:.2f}" .format(diferencia.days / 30.44))
    print("numero de años es ", "{0:.2f}" .format(diferencia.days / 365))


print (dos_fechas())