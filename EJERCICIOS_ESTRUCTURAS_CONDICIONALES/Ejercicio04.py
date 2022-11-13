'''El promedio final de un curso se obtiene en base al promedio simple de tres prácticas
calificadas. Para ayudar a los alumnos, el profesor del curso ha prometido incrementar en dos
puntos la nota de la tercera práctica calificada, si es que esta no es menor que 10. Desarrolle el
programa que determine el promedio final de un alumno conociendo sus tres notas. 
'''
import os
os.system("cls")

# ENTRADA

nota1 = int(input("Ingrese la primera nota: "))
nota2 = int(input("Ingrese la segunda nota: "))
nota3 = int(input("Ingrese la tercera nota: "))

# PROCESO

if nota3 > 10 and nota3 <=18 and nota1 < 21 and nota2 < 21: 
   nota3_conPuntos = nota3 + 2
   # SALIDA
   print(f"Nota de la PC3 con puntos agregados: {nota3_conPuntos: .2f}")
   promedio = (nota1 + nota2 + nota3_conPuntos) / 3
   print(f"PROMEDIO: {promedio: .2f}")
elif nota1 > 20 or nota2 > 20 or nota3 > 20: 
   # SALIDA
   print(f"*** HA INGRESADO UNA NOTA INCORRECTA ***")
else: 
   promedio = (nota1 + nota2 + nota3) / 3
   # SALIDA
   print(f"No se incrementará la nota porque es menor a 10") 
   print(f"PROMEDIO: {promedio: .2f}")