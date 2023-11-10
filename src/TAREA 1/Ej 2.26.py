#Escribir un programa que pregunte por consola por los productos de una cesta de la compra, separados por comas, y muestre por pantalla cada uno de los productos en una línea distinta.

productos_lista = input("Ingrese los productos de la cesta de la compra, separados por comas: ")

# Reemplaza las comas con saltos de línea y muestra los productos en líneas separadas
productos = productos_lista.replace(',', '\n')
print(productos)