entero = int(input())
a, b, c = map(int, input().split())
combos = []
daño = 0

for x in range(entero):
    combo = input()
    combos.append(combo)

for individual in combos:
    daño = (individual.count("A")*a + individual.count("B")*b + individual.count("C")*c)
    print (daño)