s1 = float(input("Introduce el primer lado: "))
s2 = float(input("Introduce el segundo lado: "))
s3 = float(input("Introduce el tercero lado: "))
from math import sqrt
s = (s1 + s2 + s3) / 2
product = s * (s - s1) * (s - s2) * (s - s3)
print("El area es", sqrt(product))
