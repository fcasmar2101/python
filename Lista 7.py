letras = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"]

lista_filtrada = []

for i in range(len(letras)):
    if i % 3 != 0:
        lista_filtrada.append(letras[i])

print(lista_filtrada)