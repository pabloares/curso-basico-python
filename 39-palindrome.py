frase = input("Introduce una frase: ")
frase1 = frase.lower()
frase2 = ""
frase3 = ""
for char in frase1:
   if char in "abcdefghijklmnopqrstuvwxyz":
      frase2 = frase2 + char
n = len(frase2)
for i in range(len(frase2)):
   frase3 = frase3 + frase2[n - 1 - i]
print(frase)
print(frase2)
print(frase3)
if frase2 == frase3:
   print("La frase es palindroma")
else:
   print("La frase no es palindroma")
