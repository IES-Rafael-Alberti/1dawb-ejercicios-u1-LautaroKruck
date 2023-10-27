#Imagina que acabas de abrir una nueva cuenta de ahorros que te ofrece el 4% de interés al año. Estos ahorros debido a intereses, que no se cobran hasta finales de año, se te añaden al balance final de tu cuenta de ahorros. Escribir un programa que comience leyendo la cantidad de dinero depositada en la cuenta de ahorros, introducida por el usuario. Después el programa debe calcular y mostrar por pantalla la cantidad de ahorros tras el primer, segundo y tercer años. Redondear cada cantidad a dos decimales.

"Calcula el interés: capital * (1 + interes)"
dinero = float(input("Introduzca la cantidad de dinero: "))

interes1 = dinero * (1 + 0.04)
print("Ahorros en el primer año:""{:.2f}".format(interes1) )

interes2 = interes1 * (1 + 0.04)
print("Ahorros en el segundo año:""{:.2f}".format(interes2) )

interes3 = interes2 * (1 + 0.04)
print("Ahorros en el tercer año:""{:.2f}".format(interes3) )

