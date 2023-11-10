#Escribir un programa que lea un entero positivo, n, introducido por el usuario y después muestre en pantalla la suma de todos los enteros desde 1 hasta n. La suma de los n primeros enteros positivos puede ser calculada de la siguiente forma:

num = int(input("Introduzca un número: "))

suma = (num * (num + 1 )) / 2

print ( "La suma de los primeros numeros enteros hasta" , num , "es" ,suma)