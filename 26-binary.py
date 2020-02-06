numero = int(input("Introduce un numero en binario: "))
decimal = 0
factor = 1
while (numero):
   decimal += (numero % 10) * factor
   factor *= 2
   numero //= 10
print("El numero en base 10 es igual a =", decimal)
