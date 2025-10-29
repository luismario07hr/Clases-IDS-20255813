entero = int(input())
sls = []
conteo = 0

for x in range(entero): 
    sls.append(int(input()))

for sl in sls: 
    if sl >= 3: 
        print ("Ok")
    else: 
        print ("No")
