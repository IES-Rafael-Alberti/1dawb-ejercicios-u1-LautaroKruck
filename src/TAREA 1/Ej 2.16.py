#Una panadería vende barras de pan a 3.49€ cada una. El pan que no es el día tiene un descuento del 60%. Escribir un programa que comience leyendo el número de barras vendidas que no son del día. Después el programa debe mostrar el precio habitual de una barra de pan (establecido en el programa como una constante), el descuento que se le hace por no ser fresca y el coste final total de todas las barras no frescas.
costpd = 3.49
costpnd = costpd * 0.4
descuento = costpd * 0.6
numpnd = int(input("Número de barras vendidas que no son del día: ")) 
print("El precio habitual de una barra de pan es de ", costpd)
print("El descuento que se le hace por no ser fresca es de ", "{:.2f}".format(descuento))
print("El coste final total de todas las barras no frescas es de ", costpnd * numpnd)