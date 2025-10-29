personas = int(input())
edades = []
conteo = 0

for x in range(personas): 
     edades.append(int(input()))

for edad in edades: 
    if edad >=15: 
        conteo += 1

print (conteo)