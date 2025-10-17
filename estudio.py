"""El correo contiene exactamente un @
Antes y después del @ debe haber al menos 3 caracteres
El correo debe contener al menos un punto
El correo no puede contener espacios
El correo no puede iniciar ni terminar con un punto

a = input()
print (a.count('@') == 1 and len(a.split('@')[0]) >= 3 and len(a.split('@')[1]) >= 3 and '.' in a and ' ' not in a and a[0] != '.' and a[-1] != '.' )"""

"""b = input()
print (b.count("z"))

x = int(input())
ah = input()
bh = input()

que = int(len(ah)/x)
so = int(len(bh)/x)

print (ah[:que] + bh[-so:])

x = int(input())
y = int(input())
z = int(input())
j = int(input())

print (x*y - z*j)"""

"""ai = float(input())
be = float(input())
ce = float(input())
de = float(input())
e = float(input())
f = float(input())
lista = [ai, be, ce, de, e, f]

print (f"Maximo: {max(lista): .2f}")
print (f"Minimo: {min(lista): .2f}")
print (f"Diferencia: {(max(lista) - min(lista)): .2f}")
print (f"Suma: {(sum(lista)): .2f}")
print (f"Promedio: {((sum(lista))/6): .2f}")"""

"""a = int(input())
b = int(input())
c = int(input())
d = int(input())
e = int(input())
f = float(input())
g = float(input())
h = float(input())
i = float(input())
j = float(input())

print (int(a*f + b*g + c*h + d*i + e*j))"""

"""nombre = input()
apellido = input()
nick = nombre[:5].lower() + apellido[0].lower()
pin = (len(nombre)* 1000 + len(apellido))%10000
Id = "C3-" + str(nick) + "-" + str(pin)

print (f"Nick: {nick}")
print (f"Pin: {pin}")
print (f"ID: {Id}")"""

"""fecha = input()
año = fecha[6:]
mes = fecha[3:5]
dia = fecha [0:2]

print (f"{año}/{mes}/{dia}")"""

"""principal = ("Hamburguesa", "Pizza", "Tacos", "Pupusas", "Hotdog")
complemento = ("Papas fritas", "Alitas de pollo", "Ensalada", "Sopa", "Lasaña")
a = int(input())
b = int(input())
comida = principal[a-1]
side = complemento[b-1]

print (f"El pedido de Alvin es: {comida} con {side}")"""

num = int(input())
solucion = (num * (num+1))/2

print (int(solucion))