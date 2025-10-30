vegetariano=input("¿Eres vegetariano? ")
if vegetariano == "si":
    print ("Igredientes: Pimiento, tofu")
    ingrediente=input("Elige uno: ")
    print (f"Tu pizza es vegetariana y lleva tomate mozzarella y {ingrediente}")
else:
    if vegetariano == "no":
        print ("Igredientes: Peperoni, jamon y salmon")
        ingrediente=input("Elige uno: ")
        print (f"Tu pizza no es vegetariana y lleva tomate mozzarella y {ingrediente}")
    else:
        print ("Respuesta no valida")