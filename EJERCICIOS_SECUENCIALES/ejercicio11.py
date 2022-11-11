import os
os.system("cls")

#entrada
primernumero = int(input ("ingrese un numero entero de 3 cifras: "))
segundonumero = int(input ("ingrese un numero entero de 3 cifras: "))
#proceso
c3 = primernumero % 10
c2 = int((primernumero % 100) / 10)
c1 = int((primernumero % 1000) / 100)

d3 = segundonumero % 10
d2 = int((segundonumero % 100) / 10)
d1 = int((segundonumero % 1000) / 100)


#Salida
print ( f"============ INTERCAMBIANDO CIFRAS ===================")
print(f"{d3}{c2}{d1}")
print(f"{c3}{d2}{c1}")
