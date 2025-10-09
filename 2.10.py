productos=input("Introduce los productos separados por comas: ")
lista=productos.split(",")
for producto in lista:
    print(producto.strip())
