cadena = str(input("Ingrese una cadena para contar vocales: "))

def contar_vocales(cadena):
	"""
    Saco la cantidad de vocales en una cadena string
    """
	cont = 0
	for letra in cadena:  # recorre la cadena tantas letras tenga la cadena
		if letra.lower() in "aeiou": 
			cont += 1
	return cont


print(contar_vocales(cadena))