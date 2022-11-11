import os
os.system("cls")

#entrada
    #captura de datos 
gigabyte =float(input("Capacidad del disco duro en GB: "))

#proceso 

byte = gigabyte * 1024 * 1024 * 1024
megabyte = gigabyte * 1024
kilobyte = gigabyte * 1024 * 1024

#salida 
print(f"Capacidad del disco duro: {gigabyte: .2f} GB")
print( f"MEGABYTES: {megabyte: .2f} MG")
print( f"KILOBYTES: {kilobyte: .2f} KG")
print( f"BYTES: {byte: .2f} B")
