nums = int(input())
a, b ,c = map(int, input().split())
combos =[]

for x in range(nums): 
    combos.append(input())
    
for combo in combos:
    ah = str(combo).count("A")*a
    bh = str(combo).count("B")*b
    ch = str(combo).count("C")*c
    daño = ah + bh + ch
    print (daño)

