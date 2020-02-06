char = input("Introduce una letra: ")
if char in 'aeiouAEIOU':
   print("Vocal")
elif char == 'y' or char == 'Y':
   print("A veces vocal, a veces consonante")
else:
   print("Consonante")
