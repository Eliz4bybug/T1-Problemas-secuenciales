import os
os.system("cls")

#entrada
    #captura de datos
tramo1km = float(input("ingrese la longitud en km del tramo 1: "))
tramo2pies = float(input("ingrese la longitud en pies del tramo 2: "))
tramo3millas = float(input("ingrese la longitud en millass del tramo 3: "))

#proceso
    #conversiones
tramo1m = tramo1km * 1000
tramo2m = tramo2pies / 3.281
tramo3m = tramo3millas * 1609

    #fórmula para el total en metros y en yardas
totalmetros = tramo1m + tramo2m + tramo3m
totalyardas = totalmetros * 1.094

#salida
print( f"Longitud total en metros:  {totalmetros:.2f} m")
print( f"Longitud total en yardas:  {totalyardas:.2f}  yd")