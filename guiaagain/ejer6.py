numnom = int(input())
nombres = []

for x in range (numnom): 
    nombres.append(input())

for nombre in nombres: 
    if len(nombre) <= 6: 
        print("No vale la pena")
    elif len(nombre) >= 8: 
        print ("Si aguanto otro desarrollo de personaje")
    elif 6 < len(nombre) < 8: 
        print ("Dios, no creo que aguante esta vez")
