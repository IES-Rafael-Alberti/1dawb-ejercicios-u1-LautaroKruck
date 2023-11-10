def factorial(num):

    total = 1
    while num > 1 :
        total *= num
        num -=1
    return total

num= int(input ("Escribe el numero factorial: "))

print( f"El resultado de {num}! es {factorial(num)}")