import os
os.system("cls")

#Entrada
print ( "============================== Bienvenido a la tienda ==========================================")
#captura de datos
cantidad_de_productos = float(input("Ingrese la cantidad de productos: "))

#Proceso
if cantidad_de_productos <= 25:
    importe = cantidad_de_productos * 27
    descuento = importe * 0.05
    ipagar = importe - descuento
    #salida
    print(importe)
    print ("Aplica Descuento del 5%")
    print (f"Importe total a pagar: {ipagar: 2f} nuevos soles.")

elif cantidad_de_productos > 25 and cantidad_de_productos < 50:
    importe = cantidad_de_productos * 25
    descuento = importe * 0.05
    ipagar = importe - descuento
    #salida
    print(importe) 
    print ("Aplica Descuento del 5%")
    print (f"Importe total a pagar: {ipagar: 2f} nuevos soles.")
    
else :
    importe = cantidad_de_productos * 23
    print ("Aplica Descuento del 15%")
    descuento = importe * 0.15
    ipagar = importe - descuento
    #salida
    print(importe)
    print (f"Importe total a pagar: {ipagar: 2f} nuevos soles.")
    print (f"¡Muchas gracias por su compra!")