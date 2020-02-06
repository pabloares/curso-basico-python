a = float(input("Introduce coeficiente del cuadrado, a: "))
b = float(input("Introduce coeficiente linear, b: "))
c = float(input("Introduce coeficiente independiente, c: "))
discriminante = b**2 - 4 * a * c
if (discriminante < 0):
   print("Las soluciones son complejas")
elif (discriminante == 0):
   print("Una solucion:", -b / (2 * a));
else:
   from math import sqrt
   raiz = sqrt(discriminante)
   print("Dos soluciones:", (-b + raiz) / (2 * a), "y", (-b - raiz) / (2 * a))
