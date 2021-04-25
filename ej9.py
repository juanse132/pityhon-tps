password = str(input("Ingrese un password: "))
password_correcto = "jose132"

def password(password):
    import time
    cont = 3
    tiempo_espera = 1
    while password != password_correcto:#hago hasta que el password sea el correcto
        print("escriba bien su password ")
        password = input("ingrese otra vez el password: ")
        time.sleep(tiempo_espera)
        tiempo_espera += 2 #se sumo a la var para que luego tarde mas
        cont -= 1 #le resto al contador en 1 
        if cont == 0: # y pregunto si ese cont vale 0
            print("se acabaron los intentos")
            return False
            break
    else:
        return True      

print(password(password))

