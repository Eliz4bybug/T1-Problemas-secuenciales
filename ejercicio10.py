import os
os.system("cls")
#entrada
numero = int(input ("ingrese un numero natural de 4 cifras: "))

#proceso
print(numero)
print()
numero = str (numero)[::-1]

#salida
print(numero)