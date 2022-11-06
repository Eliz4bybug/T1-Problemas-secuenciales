import os
os.system("cls")
#entradax
numero = int(input ("ingrese un numero natural de 4 cifras: "))

#proceso
c4 = numero % 10
c3 = int((numero % 100) / 10)
c2 = int((numero % 1000) / 100)
c1 = int((numero - (numero % 1000)) / 1000)

''' 12 // 10   C-> 1 
12 % 10   R->2

123 // 100

1234 ''' 

#Salida
print(c4)
print(c3)
print(c2)
print(c1)
print(f"{c4}{c3}{c2}{c1}")