edad=int(input("Di tu edad "))
if edad<4 and edad>=0:
    print ("Entras gratis")
else:
    if edad>=4 and edad<18:
        print ("Pagas 5$")
    else:
        if edad>=18:
            print ("Pagas 10$")
        else:
            print ("introduce un numero valido")