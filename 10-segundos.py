dato = int(input("Dame un numero grande de segundos: "))
data = dato
segs = dato % 60
dato = dato - segs
dato = dato / 60
mins = dato % 60
dato = dato - mins
dato = dato / 60
horas = dato % 24
dato = dato - horas
dias = dato / 24
print("%d:%02d:%02d:%0d" % (dias, horas, mins, segs))
# Otra manera
SEGSMIN = 60
SEGSHORA = 60 * 60
SEGSDIA = 24 * 60 * 60
dias = data // SEGSDIA
data = data % SEGSDIA
horas = data // SEGSHORA
data = data % SEGSHORA
mins = data // SEGSMIN
segs = data % SEGSMIN
print("%d:%02d:%02d:%0d" % (dias, horas, mins, segs))
