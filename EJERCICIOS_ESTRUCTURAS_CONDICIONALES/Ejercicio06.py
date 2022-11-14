'''
. Desarrolle el programa que determine la edad menor y mayor de tres edades ingresadas.
'''
import os
os.system ("cls")

edad1 = int(input("Edad 1: "))
edad2 = int(input("Edad 2: "))
edad3 = int(input("Edad 3: "))

if edad1 != edad2 and edad1 != edad3 and edad2 != edad3:
    if edad1 > edad2 and edad1 > edad3: 
        print(f"Edad Mayor: {edad1: .2f}")
    else : 
        print(f"Edad menor: {edad1: .2f}")
        if edad2 > edad1 and edad2 > edad3: 
           print(f"Edad Mayor: {edad2: .2f}")
        else : 
           #print(f"Edad menor: {edad2: .2f}")
           print(f"Edad Mayor: {edad3: .2f}")
           
    '''else : 
        print(f"Edad Menor: {edad1: .2f}")
    if edad2 > edad1 and edad2 > edad3: 
        print(f"Edad Mayor: {edad2: .2f}")
    else : 
        print(f"Edad Menor: {edad2: .2f} ")
    if edad3 > edad1 and edad3 > edad1: 
        print(f"Edad Mayor: {edad1: .2f}")
    else : 
        print(f"Edad Menor: {edad1: .2f} ")'''

else: 
    print("Ingrese 3 edades diferentes")