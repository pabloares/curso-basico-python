lista1 = ["abc", "def", 1, 3, 55]
lista2 = ["abcd", "defg", 2, 4, 55]
iguales = False
i = 0
while (iguales == False) & (i < len(lista1)):
   if lista1[i] == lista2[i]:
      iguales = True
   i+= 1
print(iguales)
print(i)
