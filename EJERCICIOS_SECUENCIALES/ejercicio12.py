import os
os.system("cls")

#entrada
segundos= int(input("Ingrese un número expresado en segundos: "))

#proceso
dias = segundos // (24 * 60 * 60)
segundos = segundos % (24 * 60 * 60)
horas = segundos // (60 * 60)
segundos = segundos % (60 * 60)
minutos = segundos // 60
segundos = segundos % 60

#salida
print ("En días: {}".format(dias))
print ("En horas: {}".format(horas))
print ("En minutos: {}".format(minutos))
print ("En segundos: {}".format(segundos))