#Escribe un programa que pida el importe final de un artículo y calcule e imprima por pantalla el IVA que se ha pagado y el importe sin IVA (suponiendo que se ha aplicado un tipo de IVA del 10%).

preciototal = input ("Escribe el importe total de un artículo \n")
preciototal = float(preciototal)
iva = preciototal * 0.1
psiniva = preciototal - iva

print("Su precio sin iva es de ", psiniva, " y el iva es de ", iva)