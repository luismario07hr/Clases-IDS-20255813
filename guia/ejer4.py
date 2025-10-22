num = int(input())
numeros = []

for numero in range(num): 
    numeros.append(int(input()))
        
print(numeros.count(7), numeros.count(5))
