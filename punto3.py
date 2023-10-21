n : int = int(input("Ingrese un número entero mayor o igual a 2: ")) #Le pedimos al usuario que ingrese un número mayor o igual a 0
#Como la secuecia descendente debe ser par y cabe la posibilidad de que dicho número sea impar entonces si pasa eso, lo convertiremos en par restandole 1
if n % 2 == 1:
    n -= 1
for n in range(n, 1, -2): # El rango empieza desde 'n' con intervalo cerrado, y termina en 1 con intervalo abierto, descendera dos números, por ende el -2
    print(n) #Imprimimos 'n'