#Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.

psiniva= input ("Escribe el importe sin IVA de un artículo: \n")
ptotal= float(psiniva) * 1.21

print( f"El precio total del artículo es de {ptotal:.2f}")