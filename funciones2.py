#Modulos

def mascota (nombre: str, tipo: str): 
    print (f"Mi mascota se llama {nombre} y es un {tipo}")

mascota ("Firulais", "Perro")

def registro_usuario (nombre, apellido, inicial = "", edad = 0): #Para que no me de error si faltan valores
    if edad:
        nombre_completo = f"La persona {nombre}{inicial}{apellido} de {edad} años de edad"
    else: 
        nombre_completo = f"La persona {nombre}{inicial}{apellido}"
    return nombre_completo

print (registro_usuario("Daniel ", "Wisecarver ", "L. ", 60))

def saludar_usuarios (nombres): 
    #Saludar usuario
    for nombre in nombres: 
        print (f"Hola {nombre}")
    
usuarios = ["Ana", "Luis", "Juan"]
saludar_usuarios (usuarios)

def order_pizza(size, masa, *ingredientes): #el * es para que los trate como lista
    print (f"Ordeno una pizza {size} {masa} de")
    for ignrediente in ingredientes:
        print (f"-{ignrediente}")
order_pizza ("Grande", "Delgada", "Queso", "Tocino")

def registro_profesor (nombre, apellido, **materias): #args(*) listas, quargs (**) diccionatios
    """Crea el registro de profesores"""
    print (f"El profesor {nombre}, {apellido}")
    for ciclo, materias in materias.items(): 
        print (f"\t - {ciclo}: \t {materias}")