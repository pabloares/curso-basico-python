MICRO = 2.0
MENOR = 4.0
LIGERO = 5.0
MODERADO = 6.0
FUERTE = 7.0
MAYOR = 8.0
CATACLISMO = 10.0
strength = float(input("Introduce el valor de Ritcher, con decimales si \
quieres: "))
if (strength < MICRO):
   type = "micro"
elif strength < MENOR:
   type = "menor"
elif strength < LIGERO:
   type = "ligero"
elif strength < MODERADO:
   type = "moderado"
elif strength < FUERTE:
   type = "fuerte"
elif strength < MAYOR:
   type = "mayor"
elif strength < CATACLISMO:
   type = "cataclismo"
else:
   type = "legendario"
print("El tipo de terremoto es", type)
