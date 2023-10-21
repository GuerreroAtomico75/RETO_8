#Importamos math y de math traemos la función seno y al factorial
from math import sin, factorial
#Creamos una función que nos ayude a llegar a la aproximación de la función seno
def aproxFuncSen (b:float, e:int) -> float:
    funcSen: float = 0
    for i in range(0, e+1):
        funcSen += ((-1)**i)*((b**((2*i)+1))/factorial((2*i)+1))
    return funcSen

if __name__=="__main__":
    #Le pedimos al usuario que ingrese un valor para la base
    b = float(input("Ingrese un valor para la base 'b': "))
    e : int = 1
    aprox = aproxFuncSen(b, e)
    real = sin(b)

    #Para que el exponente sea el correcto creamos un while con la siguiente operación, así miramos la aproximación
    while abs((real - aprox)/real*100)>0.1:
        aprox: float = aproxFuncSen(b, e)
        #Actualizamos cada vez el exponente
        e += 1
    print(e, " es el valor del exponente para que funcione la aproximación")
    
    #Restamos el valor real con el exponente
    difAprox = real - aprox

    #Imprimimos
    print("La aproximación de la función seno es", aprox)
    print("La función seno real es", real)
    print("La diferencia de la función real y la aproximación es", difAprox)