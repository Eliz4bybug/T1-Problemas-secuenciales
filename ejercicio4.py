import os
os.system("cls")
#entrada
    #captura de datos
ft = float(input("ingrese la estatura en pies: "))
inches = float(input("Ingrese la estatura en pulgadas: "))

    # Mostrar datos para confirmación
print( f"Estatura inglesa:  {ft:} ft - {inches:} in")

#proceso 
ftametros = ft * (1.0 / 3.28084)
inenmetros = inches * (1.0 / 39.3701)
estaturaenmetros = ftametros + inenmetros  

#Salida
print( f"La estatura en metros sería: {estaturaenmetros: .2f} m") 