lista=[]
for i in range(6):
    numero=int(input("Dime un número ganador: "))
    lista.append(numero)
lista.sort()
print(f"Los numeros ganadores ordenados son: {lista}")