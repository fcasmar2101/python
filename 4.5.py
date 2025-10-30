cantidad=float(input("Cantidad a invertir "))
interes=int(input("Interes anual "))
años=int(input("Numero de años "))
intereses=0
for i in range(años):
    intereses=(cantidad*interes)/100
    cantidad+=intereses
    print (f"Tu capital el año {i} sera de {cantidad}")