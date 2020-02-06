lista = ["pablo", "ares", "gastesi", "inteligencia", "uno", "dos", "1"]
n = int(input("Introduce un entero positivo: "))
for i in range(len(lista)):
   if len(lista[i]) >= n:
      print(lista[i])
