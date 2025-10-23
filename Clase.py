monto = float(input("Digite el mondo: "))
tipo = input("Tipo (local/internacional): ") 

if tipo.lower() == "local": 
    if monto > 100: 
        print ("7%")
    elif monto > 75: 
        print ("5%")
    else: 
        print ("0%")

elif tipo.lower() == "internacional": 
    if monto > 100: 
        print ("12%")
    elif monto > 75: 
        print ("9%")
    else: 
        print ("0%")

else: 
    print ("Esa opción no existe")