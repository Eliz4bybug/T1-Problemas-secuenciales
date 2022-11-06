import os
os.system("cls")

#entrada
#captura de datos 
radio = float(input("Ingrese el radio del cilindro: "))
altura = float(input("Ingrese la altura del cilindro: "))

#proceso
pi = 3.141592
areabase = pi * (radio ** 2)
arealateral = 2 * pi * radio * altura
areatotal = 2 * areabase * arealateral

#salida
print(f"=============================== HALLANDO EL CILINDRO =================================")
print(f"Valor asignado de π será  {pi: .2f}")
print(f"Área Base: {areabase: .2f} m²")
print(f"Área lateral : {arealateral: .2f} m²")
print(f"ÁREA TOTAL: {areatotal: .2f} m²")