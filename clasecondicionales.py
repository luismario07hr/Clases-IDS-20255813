"""print ("HOLA, BIENVENIDO uwu")

a = int(input("¿Cuántas personas entran?: "))
lista = []
entra = 0
noentra = 0

for x in range(a): 
    lista.append(int(input("Ingrese la edad de la persona que va a entrar: ")))
    
for edad in lista: 
    if edad >= 15: 
        entra = entra + 1
    else: 
        noentra = noentra + 1

print (f"Las personas que entran son {entra} y las que no entran son {noentra}")"""

"""dias = ["Lunes", "Martes", "Miercoles", "Jueves", "Viernes", "Sabado", "Domingo"]
for i in dias[1]: 
    print (i)"""
    

"""a = int(input())
valores = [[1, 2, 6], 
           [2, 7, 4], 
           [6, 5, 9], 
           [1, 10, 20]]
valores6 = []

for x in valores: 
    for y in x: 
        if y > a:
            valores6.append(y)
        
print (valores6)"""

"""presupuesto = 1000
gasto = 0


while gasto < presupuesto: 
    compra =float(input("Monto a comprar: "))
    gasto += compra 

presupuesto -= gasto

print ("Ha llegado al límite del presupuesto")
print (f"Su presupuesto final es de {presupuesto}")"""

limite = int(input())
valores = [[1, 2, 6], 
           [2, 7, 4], 
           [6, 5, 9], 
           [1, 10, 20]] 
suma = 0
i = 0


while i < len(valores) and suma < limite:
    j = 0
    while j < len(valores[i]) and suma < limite:
        suma += valores[i][j]
        j += 1
    i += 1
               
print (suma)