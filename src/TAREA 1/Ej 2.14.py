#Una juguetería tiene mucho éxito en dos de sus productos: payasos y muñecas. Suele hacer venta por correo y la empresa de logística les cobra por peso de cada paquete así que deben calcular el peso de los payasos y muñecas que saldrán en cada paquete a demanda. Cada payaso pesa 112 g y cada muñeca 75 g. Escribir un programa que lea el número de payasos y muñecas vendidos en el último pedido y calcule el peso total del paquete que será enviado.
pesop = 112 
pesom = 75 
nump = int(input ("Número de payasos vendidos en el pedido: "))
numm = int(input ("Número de muñecas vendidos en el pedido: "))

pesototal = (pesop * nump) + (pesom * numm)

print ("El peso total del pedido es de ", pesototal , "g")
