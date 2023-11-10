#Escribir un programa que pregunte al usuario la fecha de su nacimiento en formato dd/mm/aaaa y muestra por pantalla, el día, el mes y el año. Adaptar el programa anterior para que también funcione cuando el día o el mes se introduzcan con un solo carácter.
fec_nac = input("Ingrese su fecha de nacimiento (dd/mm/aaaa): ")

dia, mes, año = fec_nac.split('/')

dia = int(dia)
mes = int(mes)
año = int(año)

print(f"Día: {dia} \n Mes: {mes} \n Año: {año}")


