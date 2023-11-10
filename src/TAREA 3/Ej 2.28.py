"""
Realiza un algoritmo con PSEUDOCÓDIGO y pásalo a un programa en Python que lea dos números enteros, muestre cuál es el menor de los dos y cuantos números existen entre ellos dos.
El segundo número no puede ser igual, si es así, debe mostrar el error: "Los números no pueden ser iguales".
Si los números son diferentes, por ejemplo 5 y 12 debe mostrar la frase "El número menor es el 5 y entre ellos existen 7 números enteros".
El pseudocódigo debes incluirlo como comentarios en el programa de Python.

Inicio
Lee num1
Lee num2
Si (num1 == num2)
    Escribe("Los números no pueden ser iguales")
sino( num1 >= num2 )
    num3 = num1 - num2 
    Escribe ("El numero menor es el " + num2 + " y entre ellos existen " + num3 + " numeros enteros ")
sino( num2 >= num1 )
    num3 = num2 - num1 
    Escribe ("El numero menor es el " + num1 + " y entre ellos existen " + num3 + " numeros enteros ")
Fin
"""

num1= int(input("Escribe el primer número: "))
num2= int(input("Escribe el segundo número: "))

if(num1 == num2):
    print("Los números no pueden ser iguales")
elif(num1 >= num2):
    num3 = num1 - num2 
    print("El numero menor es el " , num2 , " y entre ellos existen " , num3 , " numeros enteros ")
elif(num2 >= num1):
    num3 = num2 - num1 
    print("El numero menor es el " , num1 , " y entre ellos existen " , num3 , " numeros enteros ")