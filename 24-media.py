numero = 1
suma = 0
count = 0
while numero:
   numero = float(input("Introduce un numero, 0 para terminar: "))
   if numero == 0:
      break
   suma += numero
   count += 1
if suma == 0:
   print("Error, no hay datos")
else:
   print("La media es:", suma / count)
