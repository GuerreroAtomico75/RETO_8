#Importamos math y de math traemos la función exponencial y al factorial
from math import exp, factorial
#Creamos una función que nos ayude a llegar a la aproximación de la función exponencial
def aproxFunc(x: float, e: int) -> float:
    #Ponemos un condicional que nos especifíca que si la base es diferente de 1 se puede hacer el ejercicio, si no, no se podría porque en la función exponencial no se puede tener de base a 1
    if x != 1:
        funcAprox = 0
        #El rango irá de 0 a e+1 para que se tenga en cuenta el exponente necesario
        for i in range(0, e+1):
            funcAprox += (x**i) / factorial(i)
        return funcAprox
    else:
        print("En la función exponencial la base no puede ser 1, porque entonces se convertiría en una función constante")

if __name__ == "__main__":
    #Le pedimos al usuario que ingrese un valor para la base
    x : float = float(input("Ingrese un valor para x: "))
    e : int = 1
    aprox = aproxFunc(x, e)
    real = exp(x)

    #Para que el exponente sea el correcto creamos un while con la siguiente operación, así miramos la aproximación
    while ((real - aprox)/real*100)>0.1:
        aprox: float = aproxFunc(x, e)
        #Actualizamos cada vez el exponente
        e += 1
    print(e, " es el valor del exponente para que funcione la aproximación")

    #Restamos el valor real con el exponente
    difAprox = real - aprox

    #Imprimimos los siguientes valores
    print("La aproximación de la función exponencial es", aprox)
    print("La función exponencial real es", real)
    print("La diferencia de la función real y la aproximación es", difAprox)