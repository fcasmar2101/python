palabra=input("Dime tu palabra")
vocales=["a","e","i","o","u"]
for vocal in vocales:
    cantidad=palabra.count(vocal)
    print(f"La vocal {vocal} aparece un total de {cantidad} veces")