password = str(input("Ingrese un password: "))
password_correcto = "password123"

def password(password):
    """
    Establezco una contraseña inventada y la voy comparando con la que escribe el usuario 
    """
    import time
    cont = 3
    tiempo_espera = 1
    while password != password_correcto:  # hago hasta que el password sea el correcto
        print("Escriba bien su password ")
        password = input("Ingrese otra vez el password: ")
        time.sleep(tiempo_espera)
        tiempo_espera += 2  # se sumo a la var para que luego tarde mas
        cont -= 1  
        if cont == 0:
            print("Se acabaron los intentos")
            return False
            break
    else:
        return True      

print(password(password))

