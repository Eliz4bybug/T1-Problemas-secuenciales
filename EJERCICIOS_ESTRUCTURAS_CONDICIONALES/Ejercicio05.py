'''Desarrolle el programa que dado un número de 4 cifras, forme el mayor número posible de dos
cifras usando la mayor y menor cifra del número ingresado.'''
# EJERCICIO MAL DESARROLLADO 
# ============== CORREGIR ===========================
import os
os.system("cls")

# ENTRADA 
numero = int(input("Ingrese un número de 4 cifras: "))

# PROCESO
d4 = numero % 10
d3 = int((numero % 100) / 10)
d2 = int((numero % 1000) / 100)
d1 = int((numero - (numero % 1000)) / 100)

print (f"Digito 1: {d1: .2f}")
print (f"Digito 2: {d2: .2f}")
print (f"Digito 3: {d3: .2f}")
print (f"Digito 4: {d4: .2f}")

if d1 > d2 and d1 > d3  and d1 > d4: 
    print(f"Dígito mayor: {d1: .2f}")
    digito_Mayor = (d1 / 10) 
    print(f"Número mayor: {digito_Mayor: .2f}9")
if d2> d1 and d2 > d3  and d2 > d4: 
    print(f"Dígito mayor: {d2: .2f}")
    print(f"Número mayor: {d2: .2f}9")
if d3 > d1 and d3 > d2  and d3 > d4: 
    print(f"Dígito mayor: {d3: .2f}")
    print(f"Número mayor: {d3: .2f}9")
if d4 > d1 and d4 > d2  and d4 > d3: 
    print(f"Dígito mayor: {d4: .2f}")
    print(f"Número mayor: {d4: .2f}9")
else :
    print("HA INGRESADO UN VALOR INCORRECTO")