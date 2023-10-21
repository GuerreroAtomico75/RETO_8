n : int = int(input("Ingrese un número entero el cual corresponderá al final del rango: ")) #Le pedimos al usuario que ingrese el último número del rango
for num in range(1, n+1): #El rango va a ser de 1 hasta n+1 para que l número ingresado también reciba su factorial
    factorial = 1 #Incializamos variable factorial
    for f in range(1, num + 1): #Creamos otro ciclo for, para que el num que se está en ese momento en el primer ciclo for sea multiplicado por cada valor del segundo ciclo. Así con cada valor del ciclo for.
        factorial *= f #El valor de 'f' lo multiplicamos por el factorial
    print(num, factorial, sep=", ") #Por último se imprimen los números desde 1 hasta el número ingresado por el usuario, con su respectivo factorial cada número.