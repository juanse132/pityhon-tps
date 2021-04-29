cadena = str(input("Ingrese una cadena para contar vocales: "))

def contar_vocales(cadena):
	cont = 0
	for letra in cadena:  # recorre la cadena tantas letras tenga la cadena
		if letra.lower() in "aeiou":  # voy comparando letras de la cadena con las vocales
			cont += 1
	return cont

print(contar_vocales(cadena))