lista = []
unique = []
word = input("Introduce una palabra, o linea en blanco para acabar: ")
while (word):
   lista.append(word)
   word = input("Introduce una palabra, o linea en blanco para acabar: ")
for i in range(len(lista)):
   if not lista[i] in unique:
         unique.append(lista[i])
print(lista)
print(unique)
