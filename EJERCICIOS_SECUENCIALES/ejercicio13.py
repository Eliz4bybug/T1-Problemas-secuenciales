import os
os.system("cls")
import datetime

'''horas= int(input("Ingrese la hora: "))
minutos = int(input("Ingrese los minutos: "))
segundos = int(input("Ingrese los segundos: "))

print ("La hora del día es {} : {} : {}".format(horas, minutos, segundos))
'''
#proceso
hora = datetime.datetime.now()
print("HORA ACTUAL: ", hora)
print ("======================= Determine la hora del día dentro de 45 minutos ===================")

hora_aproximada = hora + datetime.timedelta(minutes=45)
#salida
print ("Dentro de 45 minutos la hora será: " )
print (hora_aproximada)