pi = 3.0
print("1 aproximacion =", pi)
sign = 1
for i in range(1,7):
   product = 2 * i * (2 * i + 1) * (2 * i + 2)
   factor = 4 / product
   factor = sign * factor
   pi = pi + factor
   sign = sign * (-1)
   print(i + 1, "approximation =", pi)
