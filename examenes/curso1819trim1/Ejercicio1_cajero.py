'''
Cajero de cambio: devuelve y desglosa el cambio en billetes y monedas de forma "ideal"; es decir, con el menor número de billetes y monedas posibles.

Pide un valor en euros y devuelve los billetes de 500, 200, 100, 50, 20, 10 y 5 euros, y las monedas de 2€, 1€, 50c, 20c, 10c, 5c, 2c y 1c. Ejemplo:

Valor en €uros:  175,50

Cambio: 1 billete de 100€
		1 billete de 50€
		2 billetes de 20€
		1 billete de 5€
		1 moneda de 50c
'''

# Pedir los euros de los que ha que devolver el cambio
dinero = input("Dame la cantidad en euros de los que quieres cambio: ")

# Dividir entre euros y centimos
euros = int(dinero.split(".")[0])
cts = int(dinero.split(".")[1])

# Calcular los billetes
billetes = [500,200,100,50,20,10,5]
resto = euros
for billete in billetes:
    b = resto//billete
    if b>0:
        if b==1:
            print("un billete de",billete,"euros")
        else:
            print(b, "billetes de", billete, "euros")
        resto %= billete

# Calcular monedas
monedas = [200,100,50,20,10,5,2,1]
resto = resto*100 + cts
for moneda in monedas:
    m = resto//moneda
    if m>0:
        if moneda>=100:
            if m==1:
                print("una moneda de", int(moneda/100), "euros")
            else:
                print(m, "monedas de", int(moneda/100), "euros")
        else:
            if m==1:
                print("una moneda de", moneda, "centimos de euro")
            else:
                print(m, "monedas de", moneda, "centimos de euro")
        resto %= moneda
