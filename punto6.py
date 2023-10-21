#Inicializamos variables pidiendole al usuario que ingrese valores
x : float = float(input("Ingrese un número real para la base: "))
n : int = int(input("Ingrese un número natural para el exponente: "))
base = 1 # La base será 1, para que se esté actalizando conforme a la multiplicación que se haga de la base por si misma.
#El rango n será para el número de veces el cual se haga la multiplicación de la base por si misma
for e in range(n):
    base *= x #Esto es de lo que en los comentarios anteriores me refería
print("El resultado de la potencia es", base)