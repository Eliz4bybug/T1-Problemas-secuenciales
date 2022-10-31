import os
os.system("cls")

#falta acomodar y anotar
n = int(input("Ingresa un numero: "))

suma = 0

while n > 0:

    suma = suma + (n % 10)

    n = n // 10

print(f"La suma de los dígitos es: {suma: .2f}")
