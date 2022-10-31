import os
os.system("cls")

metros = int( input("Metros : "))

centimetros = metros * 100
pulgadas = centimetros / 2.54
pies = pulgadas / 12
yardas = pies / 3

print( f"Centímetros : {centimetros:.2f}")
print( f"Pulgadas : {pulgadas:.2f}")
print( f"Pies : {pies:.2f}") 