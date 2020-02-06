mes = input("Introduce en minusculas las tres primeras letras de un mes: ")
if (mes == 'feb'):
   print('28 o 29 dias')
elif (mes == 'ene' or mes == 'mar' or mes == 'may' or mes == 'jul' \
      or mes == 'ago' or mes == 'oct' or mes == 'dic'):
   print('31 dias')
else:
   print('30 dias')
