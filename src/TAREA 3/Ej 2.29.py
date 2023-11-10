"""
Si el nombre está vacío, debes utilizar el valor "Desconocido". La edad debe pedirla hasta que introduzca una edad comprendida entre 0 y 125 años.
El programa mostrará la siguiente frase: "Te llamas Pepito y tienes 20 años, te quedan aún 105 años por cumplir".

Inicio
    Escribe("Introduce tu nombre: ")
    Lee nombre
    Si (nombre == "")
        nombre = "Desconocido"
    Si
    edad = -1
    Mientras (0 > edad > 125)
        Escribe("Por favor, introduce tu edad (entre 0 y 125 años): ")
        Lee edad
    Fin 
    Mientras
    años = 125 - edad
    Escribe("Te llamas ", nombre, " y tienes ", edad, " años, te quedan aún ", años, " años por cumplir.")
Fin
"""

nombre = input("Introduce tu nombre: ")
if (nombre == ""):
    nombre = "Desconocido"
edad = -1
while (edad < 0 or edad > 125):
    edad = int(input("Introduce tu edad (entre 0 y 125 años): "))
años = 125 - edad
print("Te llamas ",nombre," y tienes ",edad," te quedan aún ",años," años por cumplir.")
