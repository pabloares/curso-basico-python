cantidad = float(input("Introduce la cantidad hasta dos decimales: "))
interes = float(input("Introduce el interes hasta dos decimales: "))
years = int(input("Introduce el numero de an~os, entero: "))
print("Cantidad final sera", cantidad * (1 + interes / 100)**years)
