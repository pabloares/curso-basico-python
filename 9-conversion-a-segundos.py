dias = int(input("Introduce un numero entero de dias: "))
horas = int(input("Introduce un numero entero de horas: "))
minutos = int(input("Introduce un numero entero de minutos: "))
segundos = int(input("Introduce un numero entero de segundos: "))
print('El numero total de segundos es', dias * 24 * 60 * 60 +
       horas * 60 * 60 + minutos * 60 + segundos)
