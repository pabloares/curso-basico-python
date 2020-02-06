dia = int(input("Introduce el dia del mes: "))
mes = input("Introduce en minusculas las tres primeras letras del mes: ")
if (mes == 'ene' or mes == 'feb'):
   print("Invierno")
elif (mes == 'mar') & (dia < 20):
   print("Invierno")
elif mes == 'mar' or mes == 'abr' or mes == 'may':
   print("Primavera")
elif (mes == 'jun') & (dia < 21):
   print("Primavera")
elif mes == 'jun' or mes == 'jul' or mes == 'ago':
   print("Verano")
elif (mes == 'sep') & (dia < 22):
   print("Otono")
elif mes == 'sep' or mes == 'oct' or mes == 'nov':
   print("Otono")
elif (mes == 'dic') & (dia < 21):
   print("Otono")
else:
   print("Invierno")
