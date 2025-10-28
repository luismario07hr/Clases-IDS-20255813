num = int(input())
edades=[]
n = 0

for x in range(num): 
    edades.append(int(input()))

for edad in edades: 
    if edad >= 15: 
        n = n + 1

print (n)