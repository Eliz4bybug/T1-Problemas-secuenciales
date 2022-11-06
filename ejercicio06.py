import os
os.system("cls")

#entrada
#captura de datos 
radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))

#proceso
pi = 3.141592
area = 2 * pi * radio * (radio + altura) 
volumen = pi * ( radio ** 2 ) * altura

#salida
print(f"=============================== HALLANDO EL ÁREA Y VOLUMEN DEL CILINDRO =================================")
print(f"El área y volumen del cilindro será teniendo en cuenta el valor asignado a π es  {pi: .2f}")
print(f"Área Total: {area: .2f} m²")
print(f"Volumen: {volumen: .2f} m³")