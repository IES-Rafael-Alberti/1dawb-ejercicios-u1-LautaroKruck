ancho = 17
alto = 12.0

resultado1 = ancho / alto
tipo1 = type(resultado1)

resultado2 = ancho // 2
tipo2 = type(resultado2)

resultado3 = ancho / 2
tipo3 = type(resultado3)

resultado4 = ancho * 2
tipo4 = type(resultado4)

resultado5 = ancho * alto
tipo5 = type(resultado5)

resultado6 = (5 + 1) * 3
tipo6 = type(resultado6)

resultado7 = (5 + 1) / 3
tipo7 = type(resultado7)

print(f"ancho / alto = {resultado1} y es de tipo {tipo1}")
print(f"ancho // 2 = {resultado2} y es de tipo {tipo2}")
print(f"ancho / 2 = {resultado3} y es de tipo {tipo3}")
print(f"ancho * 2 = {resultado4} y es de tipo {tipo4}")
print(f"ancho * alto = {resultado5} y es de tipo {tipo5}")
print(f"(5 + 1) * 3 = {resultado6} y es de tipo {tipo6}")
print(f"(5 + 1) / 3 = {resultado7} y es de tipo {tipo7}")