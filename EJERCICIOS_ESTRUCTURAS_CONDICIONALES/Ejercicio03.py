import os
os.system ("cls")

# Entrada 
print ( "=========================== Clasificación de Ángulos ======================")
angulo = int(input("Ingrese el ángulo en grados: "))

# Proceso
if angulo == 0: 
    print("Tipo de Ángulo: NULO")
    # Salida
if angulo > 0 and  angulo < 90: 
    print("Tipo de Ángulo: AGUDO")
if angulo == 90: 
    # Salida
    print("Tipo de Ángulo: RECTO")
if angulo > 90 and angulo < 180: 
    # Salida
    print("Tipo de Ángulo: OBTUSO")
if angulo >= 180 and angulo < 360: 
    # Salida
    print("Tipo de Ángulo: CÓNCAVO")
if angulo == 360: 
    # Salida
    print("Tipo de Ángulo: COMPLETO" )
elif angulo > 360: 
    # Salida
    print("********** INGRESE UN ÁNGULO DE 0° A 360° ********")