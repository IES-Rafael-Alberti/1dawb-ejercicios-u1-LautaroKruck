#Escribe un programa que pida el importe sin IVA de un artículo y el tipo de IVA a aplicar y calcule e imprima por pantalla el precio final del artículo.
def precio(psiniva,iva):

    return psiniva * (1 + (iva / 100))
psin= int(input ("Escribe el importe sin IVA de un artículo: "))
IV= int(input ("Escribe el porcentage de IVA: "))

print( f"El precio total del artículo es de {(precio(psin,IV)):.2f}")