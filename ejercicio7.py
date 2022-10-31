import os
os.system ("cls")

#entrada
    #captura de datos 
largo = float(input("Ingrese el largo del rectángulo: "))
ancho = float(input("Ingrese el ancho del rectángulo: "))

#proceso
area = largo * ancho 
perimetro = 2 * (largo + ancho )

#salida 
print(f"====================================== HALLANDO EL RECTÁNGULO =====================================")
print(f"Área: {area: .2f} m²" )
print(f"Perímetro: {perimetro: .2f} m")