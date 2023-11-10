def factorialStr(num):

    total = 1
    res = str(num) + "! => "

    while num > 0 :
        res += str(num)

        if num != 1:
            res += " x "
        total *= num
        num -=1
    total = str(total)

    res += " = " + total 

    return res

numero= int(input ("Escribe el numero factorial: "))

print( factorialStr(numero))