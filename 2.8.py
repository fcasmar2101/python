precio=input("Dime el precio ")
decimales=precio.split(",")[1]
entero=precio.split(",")[0]
print(f"El precio es de {entero} euros y {decimales} centimos")