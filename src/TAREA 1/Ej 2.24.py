#Escribir un programa que pregunte por consola el precio de un producto en euros con dos decimales y muestre por pantalla el número de euros y el número de céntimos del precio introducido.
precio = input("Ingrese el precio del producto en euros: ")

euros , centimos = precio.split('.')

euros = int(euros)
centimos = int(centimos)

print(f"Número de euros: {euros}")
print(f"Número de céntimos: {centimos}")
