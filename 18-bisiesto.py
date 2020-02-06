year = int(input("Introduce un entero positivo: "))
if (year < 0):
   print("El entero debe ser positivo")
elif (not year % 400):
   BISIESTO = "si"
elif (not year % 100):
   BISIESTO = "no"
elif (not year % 4):
   BISIESTO = "si"
else:
   BISIESTO = "no"
print("El anno", year, "es bisiesto:", BISIESTO)
