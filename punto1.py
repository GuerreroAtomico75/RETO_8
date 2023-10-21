print("Se imprimirá un listado donde se vean los números de 1 a 100 con sus respectivos cuadrados") #Mensaje Contextualizador
for n in range(1, 101): # en el rango(1,101) Se pone ciento uno teniendo en cuenta que es un rango semiabierto, estando abierto al final.
    cuadrado = n**2
    print(n, cuadrado, sep=", ") #Imprimimos a 'n' y a 'cuadrado' separados para que se pueda ver a cada número de 1 a 100 con su respectivo cuadrado