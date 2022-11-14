'''Un estudiante recibe una propina mensual S/. 20. El estudiante rinde mensualmente tres
exámenes. Su papá ha decidido incentivarlo dándole una propina adicional de S/. 5 por cada
examen aprobado. Desarrolle el programa que determine el monto total de la propina '''

import os
os.system ("cls") 

propina_mensual = 20
pc1 = float(input("Ingrese la nota del examen 1: "))
pc2 = float(input("Ingrese la nota del examen 2: "))
pc3 = float(input("Ingrese la nota del examen 3: "))

if pc1 <= 20 and pc2 <= 20 and pc3 <= 20:
   if pc1 >= 13 and pc2 >= 13 and pc3 >= 13: 
      propinatotal = propina_mensual + 5 + 5 + 5
   else : 
      print("No recibirá propina")
      if pc1 >= 13 and pc2 < 13 and pc3 < 13: 
         propinaPC1 = propina_mensual + 5
         print(f"Examen 1 Aprobado, La propina será: {propinaPC1: .2f}")
      else : 
         print("NO RECIBE PROPINA ADICIONAL")
         if pc2 >= 13 and pc1 < 13 and pc3 < 13: 
            propinaPC2 = propina_mensual + 5
            print(f"Examen 2 Aprobado, La propina será: {propinaPC2: .2f}")
         else : 
            print("NO RECIBE PROPINA ADICIONAL")
            if pc1 < 13 and pc2 < 13 and pc3 >= 13: 
               propinaPC3 = propina_mensual + 5
               print(f"Examen 3 Aprobado, La propina será: {propinaPC3: .2f}")
            else : 
               print("NO RECIBE PROPINA ADICIONAL")

    
else: 
   print("Ingrese notas validas de 0 a 20") 
    