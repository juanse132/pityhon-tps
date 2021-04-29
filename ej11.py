ejercicios_totales = int(input("Ingrese ejerciocios totales de la prueba: "))
ejercicios_hechos = int(input("Ingrese cantidad de ejercicios resueltos bien: "))

def ejercicios_examen(ejercicios_totales,ejercicios_hechos):
    if ejercicios_totales > 0:  # valido si los ejericios totales son mayor a 0
        if 0 <= ejercicios_hechos <= ejercicios_totales:  # valido si los ejericicos resultos estan entre 0 y los totales
            porcentaje = int((ejercicios_hechos * 100) / ejercicios_totales)  # calculo el porcentaje de dichos ejercicios resueltos
            if 56 <= porcentaje <= 100:  # si esta dentro de este rango aprueba
                print("El alumno aprobo con: ", porcentaje, "%","con respecto a los ejercicios totales")
                return True
            elif 0 <= porcentaje <= 55:#si esta dentro de este rango desaprueba
                print("El alumno desaprobo con: ", porcentaje, "%","con respecto a los ejercicios totales")
                return False
        else:
            return False
    else:
        return False

print(ejercicios_examen(ejercicios_totales,ejercicios_hechos))