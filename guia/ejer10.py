num = int(input())
sls = []

for x in range(num): 
    sls.append(int(input()))

for sl in sls: 
    if sl >= 3: 
        print ("Ok")
    else: 
        print ("No")