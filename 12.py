barra = 3.49
descuento = 60
barraNO = barra * (100 - descuento) / 100

NbarraNO = float(input("¿Cuántas barras no frescas se han vendido? "))

print(f"El precio de una barra fresca es {barra:.2f} €. Si no es fresca, se aplica un {descuento}% de descuento y cuesta {barraNO:.2f} €.")
print(f"Por {NbarraNO} barras no frescas, el total es {barraNO * NbarraNO:.2f} €.")
