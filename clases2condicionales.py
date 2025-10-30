ejecucion = True

while ejecucion: 
    opcion = input("Continuamos ejecutando el menu?Y/N: ")
    if opcion.lower() == "n": 
        ejecucion = False 
    elif opcion == "y": 
        print ("Oc, mañana <3")
    else: 
        print ("La opción elegida no es valida, vuelva a intentar porfavor")
        
print ("Gracias por utilizas nuestro sistema!!!!!!!")