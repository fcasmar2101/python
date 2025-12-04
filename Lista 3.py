lista = ["Matematicas", "Fisica", "Quimica", "Historia", "Lengua"]
print(lista)
for i in range (len(lista)):
    nota=input(f"Que nota has sacado en {lista[i]} ")
    print(f"Has sacado {nota} en {lista[i]} ")