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
else : 
    print("Se regalan 15 caramelos")
#codigo para el descuento del importe

importe = cantidad_de_productos * 20

#Calcular el descuento 
if importe > 700: 
    descuento = importe * 0.16
    print (f"Importe sin descuento: {importe: .2f}")
    print (f"Importe con descuento: {descuento: .2f}")
elif importe >= 501 and importe < 700: 
    descuento = importe * 0.14
    print (f"Importe sin descuento: {importe: .2f}")
    print (f"Importe con descuento: {descuento: .2f}")
elif importe <= 500: 
    descuento = importe * 0.12
    print (f"Importe sin descuento: {importe: .2f}")
    print (f"Importe con descuento: {descuento: .2f}")
