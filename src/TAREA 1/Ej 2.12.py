#Escribir un programa que pida al usuario su peso (en kg) y estatura (en metros), calcule el índice de masa corporal y lo almacene en una variable, y muestre por pantalla la frase Tu índice de masa corporal es donde es el índice de masa corporal calculado redondeado con dos decimales
peso = float(input("Dame tu peso en kg: "))
altura = float(input("Dame tu estatura en metros: "))
mascor = peso / altura**2 
print("Tu índice de masa corporal es " , "{:.2f}".format(mascor))