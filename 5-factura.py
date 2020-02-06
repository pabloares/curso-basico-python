factura = float(input("Introduce la factura hasta dos decimales: "))
iva = factura * 0.21
propina = factura * 0.1
print("El IVA es", iva)
print("La propina es", propina)
print("La factura total es", factura + iva + propina)
