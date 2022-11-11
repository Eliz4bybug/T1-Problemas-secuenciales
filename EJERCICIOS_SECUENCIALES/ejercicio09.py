import os
os.system("cls")

#entrada
numero = int(input ("ingrese un numero natural de 4 cifras: "))

#proceso
c4 = numero % 10
c3 = int((numero % 100) / 10)
c2 = int((numero % 1000) / 100)
c1 = int((numero - (numero % 1000)) / 1000)

sumatoria = c4 + c3 + c2 + c1

#Salida
print ( f"============ HALLANDO LA SUMATORIA DE LAS CIFRAS DE UN NÚMERO DE 4 DÍGITOS ===================")
print(sumatoria)
print(f"La Sumatoria de {numero: .2f} es: {sumatoria: .2f}")