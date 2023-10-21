n : int = int(input("Ingrese un valor para el exponente: ")) #Se le pide al usuario que ingrese un valor para el exponente
for e in range(n+1): #El rango que existira va a ser (n+1) para que el exponente 'n' pueda participar en la porencia
    potencia = 2**e #La potencia va a ser 2 elevado a la 'e' que va a ser cada uno de los exponentes posibles del rango
print("El resultado de 2 elevado a la", n, "da", potencia) #El resultado de 2, elevado a la 'n' va a ser la ultima potencia que se hizo