nombre = input("Dime el nombre: ")
precio = float(input("Dime el precio: "))
unidades = int(input("Dime el número de unidades: "))
total = precio * unidades
print(f"{nombre} {precio:06.2f} € {unidades:03d} unidades {total:08.2f} €")
