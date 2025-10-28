nombres = ["Ana", "Fer", "Caro"]

for x in range(2): 
    nombres.append(input())
    print (nombres)

for nombre in nombres: 
    a = nombres.index(input())
    print (a+1)
    if nombres[a] == "Fer":
        print ("Hola")
        break
    else: 
        print ("Adios")