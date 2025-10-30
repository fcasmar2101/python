puntuacion = float(input("Di tu puntuacion "))
dinero = 2400
if puntuacion == 0.0:
    resultado=puntuacion*dinero
    print (f"Tu nuvel de rendimiento ha sido inaceptable y tu sueldo es de {resultado}")
else:
    if puntuacion == 0.4:
        resultado=puntuacion*dinero
        print (f"Tu nuvel de rendimiento ha sido aceptable y tu sueldo es de {resultado}")
    else:
        if puntuacion >= 0.6:
            resultado=puntuacion*dinero
            print (f"Tu nuvel de rendimiento ha sido meritorio y tu sueldo es de {resultado}")
        else:
            print ("Valor no valido")
            