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