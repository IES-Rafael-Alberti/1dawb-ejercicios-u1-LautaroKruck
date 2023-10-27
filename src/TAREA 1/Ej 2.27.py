#Escribir un programa que pregunte el nombre el un producto, su precio y un número de unidades y muestre por pantalla una cadena con el nombre del producto seguido de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con tres dígitos y el coste total con 8 dígitos enteros y 2 decimales.
producto = str(input("Introduzca el nombre del producto: "))
num_uni = int(input("Introduzca el número de unidades: "))
precio = float(input("Introduzca el precio del producto: "))

total = precio * num_uni
print(f"Nombre del producto: {producto}\nPrecio unitario: {precio:.2f}\nNúmero de unidades: {num_uni:03d}\nCosto total: {total:.2f}")

