peso=float(input("Introduce tu peso en KG: "))
altura=float(input("Introduce tu peso en CM: "))
imc=int(peso)/(altura)**2
print(f"Tu IMC es: ", round(imc,2))