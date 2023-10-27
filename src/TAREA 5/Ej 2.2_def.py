def sueldo(horas,coste):

    return coste * horas
hor= int (input( "Horas de trabajo: " ))
cos= int (input( "Coste por hora: " ))

print( f"Importe total: {(sueldo(hor, cos)):.2f}")
