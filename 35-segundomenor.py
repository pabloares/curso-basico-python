a = int(input("Introduce un numero, cero para acabar: "))
lista = []
while (a):
   lista.append(a)
   a = int(input("Introduce un numero, cero para acabar: "))
lista.sort()
print(lista[1])
