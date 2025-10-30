renta=int(input("Pon tu renta anual "))
if renta<10000:
    print ("Tipo impositivo del 5%")
else:
    if renta<20000 and renta>=10000:
        print ("Tipo impositivo del 15%")
    else:
        if renta<35000 and renta>=20000:
            print ("Tipo impositivo del 20%")
        else:
            if renta<60000 and renta>=35000:
                print ("Tipo impositivo del 30%")
            else:
                if renta>=60000:
                    print ("Tipo impositivo del 45%")
