import os
os.system("cls")

#Entrada
print ( "============================== Bienvenido a la tienda ==========================================")
#captura de datos
cantidad_de_productos = float(input("Ingrese la cantidad de productos: "))

#codigo para ver cúantos caramelos se regalarán 
if cantidad_de_productos <= 50:
    print("Se regalan 5 caramelos")
elif cantidad_de_productos >= 51 and cantidad_de_productos <= 100: 
    print("Se regalan 10 caramelos")
else cantidad_de_productos > 100: 
    print("Se regalan 15 caramelos")
#codigo para el descuento del importe