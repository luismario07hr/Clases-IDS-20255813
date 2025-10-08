#a, b = map(int, input().split())
#print (a + b)

"""a = int(input())
if a%2 == 0:
    print (a/2)

else: 
    print (a*3 +1)"""
    
lenn = int(input())
idn = int(input())
lcj = int(input())
isnd = int(input())

tupla = (lenn, idn, lcj, isnd)
nombres = ("LEN", "IDN", "LCJ", "ISND")

print (nombres[tupla.index(max(tupla))])