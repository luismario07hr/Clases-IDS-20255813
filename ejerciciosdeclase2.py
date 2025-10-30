alumnos = 0 
lista_alumno = []

print ("Bienvenido a nuestro sistema de control de alumnos")
menu_activo = True

while menu_activo: 
    opcion = input("Elija la opción (1: Ingresar alumnos)(2: Consultar)(3: Modifica)(4:Eliminar)(5: Salir): ")
    
    if opcion == "5": 
        menu_activo = False #el más importante porque rompe el bucle
        
    elif opcion == "1":
        print ("Vamos a ingresar alumnos")
        a = int(input("¿Cuantos estudiantes quieres agregar?: "))
        for x in range(a):
            alumno = input()
            lista_alumno.append(alumno)
    
    elif opcion == "2": 
        for nombre in lista_alumno: 
            print (f"Alumno: {nombre}")
    
    elif opcion == "3": 
        pos = int(input("Ingrese el num del alumno a reemplazar: "))
        n = input("Ingrese el nuevo nombre: ")
        lista_alumno[pos-1] = n
    
    elif opcion == "4": 
        re = int(input("Ingrese el numero de alumno que quiere eliminar: "))
        borrado = lista_alumno.pop(re-1)
        print (f"Usted ha borrado a {borrado}")
    else: 
        print ("La opción no es valida")