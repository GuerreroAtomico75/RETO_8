# RETO_8
### Importante, Mensaje para el profe:
#### Profe, se me pasó la fecha para subir el repositorio, pero por favor tenga piedad de mí. Por favor califiqueme el reto, traté de hacerlo lo mejor posible. Misericordia Por Favor. Lo Ruego
---
#### Nota:
La documentación del repositorio está en los mismos códigos, explicando porque se tomaron algunas decisiones que considero importante
---
##### 1.Imprimir un listado con los números del 1 al 100 cada uno con su respectivo cuadrado.
```python
print("Se imprimirá un listado donde se vean los números de 1 a 100 con sus respectivos cuadrados") #Mensaje Contextualizador
for n in range(1, 101): # en el rango(1,101) Se pone ciento uno teniendo en cuenta que es un rango semiabierto, estando abierto al final.
    cuadrado = n**2
    print(n, cuadrado, sep=", ") #Imprimimos a 'n' y a 'cuadrado' separados para que se pueda ver a cada número de 1 a 100 con su respectivo cuadrado
```
---
##### 2. Imprimir un listado con los números impares desde 1 hasta 999 y seguidamente otro listado con los números pares desde 2 hasta 1000.
```python
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
```
---
##### 3. Imprimir los números pares en forma descendente hasta 2 que son menores o iguales a un número natural n ≥ 2 dado
```python
n : int = int(input("Ingrese un número entero mayor o igual a 2: ")) #Le pedimos al usuario que ingrese un número mayor o igual a 0
#Como la secuecia descendente debe ser par y cabe la posibilidad de que dicho número sea impar entonces si pasa eso, lo convertiremos en par restandole 1
if n % 2 == 1:
    n -= 1
for n in range(n, 1, -2): # El rango empieza desde 'n' con intervalo cerrado, y termina en 1 con intervalo abierto, descendera dos números, por ende el -2
    print(n) #Imprimimos 'n'
```
---
##### 4. Imprimir los números de 1 hasta un número natural n dado, cada uno con su respectivo factorial
```python
n : int = int(input("Ingrese un número entero el cual corresponderá al final del rango: ")) #Le pedimos al usuario que ingrese el último número del rango
for num in range(1, n+1): #El rango va a ser de 1 hasta n+1 para que l número ingresado también reciba su factorial
    factorial = 1 #Incializamos variable factorial
    for f in range(1, num + 1): #Creamos otro ciclo for, para que el num que se está en ese momento en el primer ciclo for sea multiplicado por cada valor del segundo ciclo. Así con cada valor del ciclo for.
        factorial *= f #El valor de 'f' lo multiplicamos por el factorial
    print(num, factorial, sep=", ") #Por último se imprimen los números desde 1 hasta el número ingresado por el usuario, con su respectivo factorial cada número.
```
---
##### 5. Calcular el valor de 2 elevado a la potencia n usando ciclos for.
```python
n : int = int(input("Ingrese un valor para el exponente: ")) #Se le pide al usuario que ingrese un valor para el exponente
for e in range(n+1): #El rango que existira va a ser (n+1) para que el exponente 'n' pueda participar en la porencia
    potencia = 2**e #La potencia va a ser 2 elevado a la 'e' que va a ser cada uno de los exponentes posibles del rango
print("El resultado de 2 elevado a la", n, "da", potencia) #El resultado de 2, elevado a la 'n' va a ser la ultima potencia que se hizo
```
---
##### 6. Leer un número natural n, leer otro dato de tipo real x y calcular x^n usando ciclos for. Disclaimer: Trate de no utilizar el operador de potencia (**).
```python
#Inicializamos variables pidiendole al usuario que ingrese valores
x : float = float(input("Ingrese un número real para la base: "))
n : int = int(input("Ingrese un número natural para el exponente: "))
base = 1 # La base será 1, para que se esté actalizando conforme a la multiplicación que se haga de la base por si misma.
#El rango n será para el número de veces el cual se haga la multiplicación de la base por si misma
for e in range(n):
    base *= x #Esto es de lo que en los comentarios anteriores me refería
print("El resultado de la potencia es", base)
```
---
##### 7. Diseñe un programa que muestre las tablas de multiplicar del 1 al 9.
```python
#Primero creamos un rango de 1 hasta 9, en el cual m pasará por cada uno
for m in range(1,10):
    #Al pasar por cada uno se imprimirá entonces cual tabla se está pasando
    print("La tabla del", m)
    #Como las tablas van a ir hasta el 10 entonces creamos un rango hasta el 10 en el cual pasará n
    for n in range(1,11):
        #Hacemos la multiplicación del m que se está haciendo por el n que está pasando
        tablas = m*n
        #Imprimimos
        print("El resultado de", m, "por", n, "es igual a", tablas)
```
---
##### 8. Diseñar una función que permita calcular una aproximación de la función exponencial alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función exponencial y mostrar la diferencia entre el valor real y la aproximación.
```python
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
```
---
##### 9. Diseñar una función que permita calcular una aproximación de la función seno alrededor de 0 para cualquier valor x (real), utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función seno y mostrar la diferencia entre el valor real y la aproximación.
```python
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
```
---
##### 10. Diseñar una función que permita calcular una aproximación de la función arcotangente alrededor de 0 para cualquier valor x en el rango [-1, 1], utilizando los primeros n términos de la serie de Maclaurin. Nota: use math para traer la función arctan y mostrar la diferencia entre el valor real y la aproximación.
```python
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
```
---
### Acá Termina el Reto 8. Misericordia por favor
