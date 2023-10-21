#Importamos math y de math traemos la función ArcTan
from math import atan
#Creamos una función que nos ayude a llegar a la aproximación de la función ArcTan
def aproxFuncArcTan (b:float, e:int) -> float:
    funcArcTan: float = 0
    for i in range(0, e+1):
        funcArcTan += ((-1)**i)*((b**(2*i+1))/(2*i+1))
    return funcArcTan

if __name__=="__main__":
    #Le pedimos al usuario que ingrese un valor para la base, que por regla debe estar entre -1 y 1
    b = float(input("Ingrese un valor para la base 'b' recuerde que debe ser un valor entre -1 y 1: "))
    e : int = 1
    aprox: float = aproxFuncArcTan(b, e)
    real = atan(b)

    #Para que el exponente sea el correcto creamos un while con la siguiente operación, así miramos la aproximación
    #Pero primero ponemos uncondicional que haga que el usuario ponga un valor entre -1 y 1
    if b<-1 or b>1:
        print("Debe ser un valor entre -1 y 1")
    else:
        while abs((real - aprox)/real*100)>0.1:
            aprox: float = aproxFuncArcTan(b, e)
            #Actualizamos cada vez el exponente
            e += 1
        print(e, " es el valor del exponente para que funcione la aproximación")
    
    #Restamos el valor real con el exponente
        difAprox = real - aprox

    #Imprimimos
        print("La aproximación de la función ArcTan es", aprox)
        print("La función ArcTan real es", real)
        print("La diferencia de la función real y la aproximación es", difAprox)