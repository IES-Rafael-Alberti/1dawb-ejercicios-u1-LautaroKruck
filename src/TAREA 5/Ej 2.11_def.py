#Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:
def total(num):
    return (num * (num + 1 )) / 2

n1 = int(input("Introduzca un número: "))
print ( f"La suma de los primeros numeros enteros hasta {n1} es {total(n1):.0f}")