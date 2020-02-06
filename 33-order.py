lista = []
sorted = []
a = int(input("Introduce un numero, cero para acabar: "))
while (a):
   lista.append(a)
   a = int(input("Introduce un numero, cero para acabar: "))
print(lista)
while (lista):
   b = min(lista)
   sorted.append(b)
   lista.remove(b)
print(sorted)
