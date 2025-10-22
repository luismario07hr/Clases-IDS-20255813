amor_num = int(input())
amores = []

for _ in range(amor_num): 
    amores.append (input())

for amor in amores: 
    if len(amor) <= 6:
        print ("No vale la pena")
    elif 6 < len(amor) < 8: 
        print ("Dios no creo aguantar esta vez")
    elif len(amor) >= 8:
        print ("Si aguanto otro desarrollo de personaje")