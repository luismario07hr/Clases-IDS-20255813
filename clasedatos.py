"""surnames = ["2", "3", "4"]
for position, surname in enumerate(surnames, start=1): #Construir un correlatico al izquierdo
    print (position, surname)

ejemplo = {"Luis:": 3, 
           "Mario:": 4,
           "Ale:": 4}

ejemplo["Ale:"] = 3

for nombre, edad in ejemplo.items(): 
    print (nombre, edad)"""
    
personas = ["Luis", "Mario", "Fer", "Caro", "Abi"]
edades = [1, 2, 3, 4, 5]
mascotas = [2, 4, 6, 2, 8]

for persona, edad, mascota in zip(personas, edades, mascotas): #iterar varias listas a la vez
    print (f"{persona} tiene {edad} años y {mascota} mascota(s)")
