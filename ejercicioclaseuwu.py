#Listas de diccionarios
datos_clientes = []
datos_productos = []

#Categorias
categorias = []


#Datos guardados de los pedidos
cliente_pedido = []
datos_pedidos = []
total_pedido = []

menu = True
n = 1
m = 1


while menu: 
    opcion = input("""Elija la opción: (1: Mostrar productos)(2: Registrar nuevo producto)(3: Registrar nuevo cliente)
                   (4: Mostrar clientes)(5: Registrar pedido)(6: Mostrar pedidos día)(7: Mostrar categorías)(8: Salir): """)
    if opcion == "8": 
        menu = False
        
    elif opcion == "1": #Mostrar prodcutos
        if datos_productos == []:
            print ("Aun no hay productos ingresados")
        else: 
            for producto in datos_productos: 
                print ("---------------------------")
                for dato, dato2 in producto.items(): 
                    print (f"{dato}: {dato2}")
                 
    elif opcion == "2": #Ingresar producto 
        
        producto = {}
        producto["Codigo"] = "P00" + str(n)
        producto["Nombre"] = input("Igrese el nombre del producto: ")
        producto["Categoria"] = input("Ingrese la categoría del producto: ")
        producto["Precio"] = float(input("Ingrese el precio del producto: "))
        n += 1
        datos_productos.append(producto)
      
   
    elif opcion == "3": #Ingresar cliente
        
        cliente = {}
        cliente["Codigo"] = "C00" + str(m)
        cliente["Nombre"] = input("Igrese el nombre del cliente: ")
        cliente["Correo"] = input("Ingrese el correo del cliente: ")
        cliente["Telefono"] = input("Ingrese el telefono del cliente: ")
        m += 1
        datos_clientes.append(cliente)
        
        
    elif opcion == "4": #Mostrar cliente
        if datos_clientes == []:
            print ("Aun no hay clientes ingresados")
        else:
            for cliente in datos_clientes: 
                    print ("---------------------------")
                    for dato1, dato3 in cliente.items(): 
                        print (f"{dato1}: {dato3}")
    
    elif opcion == "5": #Nuevo pedido
        
        client = input("Ingrese el código del cliente: ")
        num_cliente = int(client[-1])
        pedidoclient = {}
        pedidonum = int(input("Cuantos productos pedirá el cliente: "))
        productostotales = []
        total = 0
        
        for x in range(pedidonum): 
            pedidosss = input("Inserte el código del producto: ")
            num_elegido = int(pedidosss[-1])
            productostotales.append(datos_productos[num_elegido-1])
            total += datos_productos[num_elegido-1]["Precio"]
        
        print (f"Su total es de {total}")
        
        datos_pedidos.append(productostotales)
        cliente_pedido.append(datos_clientes[num_cliente-1])
        total_pedido.append(total)
    
    elif opcion == "6": #Mostrar los pedidos del día
        if cliente_pedido == [] and datos_pedidos == [] and total_pedido == []: 
            print ("No hay pedidos :(")
        else:
            print ("Los pedidos deL día son:")
            for client, productos, gastado in zip(cliente_pedido, datos_pedidos, total_pedido):
                print ("--------------------------------")
                print ("El cliente con los datos")
                print (" ")
                for x, y in client.items(): 
                    print (f"{x}: {y}")
                print (" ")
                print ("Pidio")
                for producto in productos: 
                    print ("  ")
                    for z, a in producto.items(): 
                        print (f"{z}: {a}")
                print (" ")
                print (f"Con un total de {gastado}")
                print ("--------------------------------")
                
        print (f"El total vendido es de {sum(total_pedido)}")
            
    elif opcion == "7": #Mostrar categorías
       
        for coso in datos_productos: 
            numcat = coso["Categoria"]
            categorias.append(numcat)
            
        print ("--------------------------------")   
        print (f"Las categorías disponibles son: ")
        for x in set(categorias):
            print (x)
        print ("--------------------------------")