a1 = float(input("Latitud del primer punto: "))
b1 = float(input("Longitud del primer punto: "))
a2 = float(input("Latitud del segundo punto: "))
b2 = float(input("Longitud del segundo punto: "))
from math import cos, sin, acos
distance = 637.01 * acos(sin(a1) * sin(a2) + cos(a1) * cos(a2) * cos(b1
           - b2))
print("La distancia entre los puntos es ", distance, "kms")
