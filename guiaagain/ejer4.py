a = int(input())
nums = []

for x in range(a): 
    nums.append(int(input()))

sietes = nums.count(7)
cincos = nums.count(5)

print (sietes, cincos)