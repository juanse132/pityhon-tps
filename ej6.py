def mayor_Producto(num1,num2,num3,num4):    
    maximo = num3 * num4
    for i in (num2,num3,num4): # Recorro hasta el num4 y comparo el producto con el maximo
        producto = num1 * i
        if (producto > maximo):
            maximo = producto  
    
    for i in (num3,num4): # Recorro desde num3 hasta num4 y comparo el producto con el maximo
        producto = num2 * i
        if (producto > maximo):
            maximo = producto
    return maximo
print("El mayor producto es: ", mayor_Producto(1,5,-2,-4))