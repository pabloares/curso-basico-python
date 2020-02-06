lista = [2, 5, 23, 89,21, 24, 55]
n = int(input("Introduce un numero entero positivo o cero "))
if (n < 0):
   print("El numero debe ser positivo")
elif (n > len(lista)):
   print("La lista no tiene tantos elementos")
else:
   lista.pop(n)
   print(lista)
