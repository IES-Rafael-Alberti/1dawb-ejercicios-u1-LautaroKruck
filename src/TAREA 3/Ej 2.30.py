"""
El incremento y el total deben ser mayor que cero, sino el programa debe finalizar con un error u obligar a que introduzcan un valor correcto de ambos (os lo dejo a vuestra elección, la primera opción es más fácil, aunque el mundo está lleno de valientes)
Por ejemplo, si introducen los valores 1, 1 y 10, el programa mostrará en consola exactamente lo siguiente: SERIE => 1-2..3..4..5..6..7..8..9-10

Inicio
    Escribe("Introduce el valor inicial: ")
    Lee inicial
    Escribe("Introduce el incremento: ")
    Lee incremento
    Escribe("Introduce el total de números: ")
    Lee total

    Si (incremento <= 0 o total <= 0)
        Escribe("El incremento y el total deben ser mayores que cero. Programa finalizado.")
    Sino
        serie = ""
        valor = inicial
        i = 1
        Mientras (i <= total)
            serie = serie + valor_actual
            Si (i < total)
                serie = serie + ".."
            Fin Si
            valor += incremento
            i = i + 1
        Fin Mientras
        Escribe("SERIE => " + serie)
    Fin Si
Fin
"""
inicial = int(input("Introduce el valor inicial: "))
incremento = int(input("Introduce el incremento: "))
total = int(input("Introduce el total de números: "))

if (incremento <= 0 or total <= 0):
    print("El incremento y el total deben ser mayores que cero. Programa finalizado.")
else:
    serie = ""
    valor = inicial
    i = 1
    while (i <= total):
        serie = serie + str(valor)
        if (i < total):
            serie = serie + ".."   
        valor += incremento
        i = i + 1
    print("SERIE => " + serie)

    
