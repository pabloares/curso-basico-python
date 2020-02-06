mes = input("Introduce las tres primeras letras de un mes, en minusculas: ")
if (mes == "abr") or (mes == "jun") or (mes == "sep") or (mes == "nov"):
   print("El mes tiene 30 dias")
elif mes == "feb":
   print("El mes tiene 28 o 29 dias")
else:
   print("El mes tiene 31 dias")
