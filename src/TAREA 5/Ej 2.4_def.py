def celsius(grados):
    return (grados - 32) * 5 / 9 

gd = int(input("Escribe una temperatura en grados Fahrenheit: \n"))
print(f"Son {(celsius(gd)):.2f} grados Celsius")