num = int(input())
numpar = num
numimpar = num

if num%2 == 0: 
    numpar += 2
    numimpar -= 1
else: 
    numpar += 1
    numimpar -= 2
    
print (numpar)
print (numimpar)
