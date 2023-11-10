preciototal = input ("Escribe el importe total de un artículo: \n")
preciototal = float(preciototal)
iva = preciototal * 0.1
psiniva = preciototal - iva

print(f"Su precio sin iva es de {psiniva:.2f} y el iva es de {iva:.2f}")