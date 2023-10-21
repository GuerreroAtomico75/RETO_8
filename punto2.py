print("Se imprimiran dos listados, el primero de los números impares de 1 hasta 999, el segundo va a ser de 2 hasta 1000") #Mensaje contextualizador sobre el programa
#Creamos listas, una para los impares y otra para los pares
imparLista = []
parLista = []
for n in range(1,1001): #El ciclo se repetirá para todos los 'n' del rango, teniendo en cuenta que el rango es abierto al final, por ende ponemos 1001
    #Condicionamos, la primera condición es para los impares, si el modulo de (n,2) da 1 o la división de (n,2) da 0.5 entonces es impar, sino se cumple ninguna de las dos entonces es par
    if n % 2 == 1 or n / 2 == 0.5:
        imparLista.append(n) #Agregamos a la lista de los impares para esta condición
    else:
        parLista.append(n) #Agregamos a la lista de los para en esta condición

#Imprimimos la lista de los impares y la lista de los pares
print(imparLista)
print(parLista)