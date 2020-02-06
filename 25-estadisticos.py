numero = 1
suma = 0
sumacuadrado = 0
count = 0
while numero:
   numero = float(input("Introduce un numero, 0 para terminar: "))
   if numero == 0:
      break
   suma += numero
   sumacuadrado += numero * numero
   count += 1
if suma == 0:
   print("Error, no hay datos")
else:
   media = suma / count
# No hacen falta los parentesis, son para que se entienda mejor
   varianza = (sumacuadrado / count) - (media**2)
   from math import sqrt
   stdeviation = sqrt(varianza)
   print("Media:", media, "Varianza:", varianza, "Desviacion:", stdeviation)
