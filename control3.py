"""1.	Configuración inicial [5 puntos]
Para que nuestro sistema funcione adecuadamente, debemos crear ciertos elementos mínimos que, nos ayudarán a trabajar más ordenadamente:
•	Crear una variable agente, y ésta tendrá el valor de encargado.
•	Crear una lista platillo que, eventualmente será gestionada.
•	Crear una lista precios que, eventualmente será gestionada."""

agente = "encargado"
platillos = []
precios = []

"""2.	Ingreso a la aplicación [15 puntos]
Al ejecutar la aplicación se pedirá al usuario ingresar el nombre del agente, por tanto, si el usuario no ingresa el valor que definimos previamente (pregunta 1), le seguirá indicando dos mensajes:
•	“Agente no registrado”
•	“Favor ingrese el nombre del agente:" """

estado = True
confirmacion = input("Ingrese el nombre del agente:") 

"""3.	Gestión del menú principal [15 puntos]
Se le pide desarrollar una lógica tal que, el usuario pueda, además de salir de la aplicación, elegir entre las opciones del menú:
1.	Creación de platillos.
2.	Consulta de platillos y precios.
3.	Colocar un pedido.
4.	Salir"""

while confirmacion != agente:
    print ("Agente no registrado")
    confirmacion = input("Favor ingrese el nombre del agente: ")

while estado: 
    menu = input("Elija la opción a realizar (1: Crear un platillo)(2: Consulta un platillo y su precio) (3: Coloca un pedido)(4: Salir)")
    if menu == "4":
        estado = False
    
    elif menu == "1": 
        platillo = input("Ingrese el nombre el nombre del platillo a crear: ")
        platillos.append(platillo)
        precio = float(input("Ingrese el precio del platillo a crear: "))
        precios.append(precio)
        
    elif menu == "2":
        consulta = int(input("Elija el número de platillo a consultar: "))
        if platillos == []:
            print ("Actualmente no hay platillos ingresados")
        else: 
            print (f"{platillos[consulta-1]}: {precios[consulta-1]}")
       
    elif menu == "3": 
        eleccion = input("Indique el nombre del platillo para su orden: ")
        for platillo in platillos:
            if eleccion.lower() == platillo.lower():
                precioelec = platillos.index(eleccion)
                print (f"Usted ha elegido el {platillo} con un precio de {precios[precioelec]}")
                break
            else: 
                print ("El nombre del platillo no existe")
                break
            
    elif menu == "4": 
        crear = 0



"""5.	Consulta de platillos [25 puntos]
Al elegir la opción 2, el usuario podrá consultar dos datos (nombre de platillo y precio de platillo), bajo las siguientes consideraciones:
•	Si se elige opción 2 sin haber platillos ingresados, lo deberá indicar por medio de un mensaje “Actualmente no hay platillos ingresados”.
•	Si se elige opción 2 y sí hay platillos ingresados, los mostrará por cada línea, ejemplo:
Pollo: $3.45
Sopa: $2.75"""

"""6.	Colocar un pedido [25 puntos]
Al elegir la opción 3, el usuario podrá indicar el nombre del platillo a elegir por medio de un mensaje:
•	“Indique el nombre del platillo para su orden:”
Si el platillo existe le indicará por ejemplo “Usted ha elegido pollo con un precio de $3.45” el precio será correspondiente al valor ya ingresado en el punto anterior (pregunta 4). El nombre podrá ser ingresado en cualquier combinación de mayúsculas y minúscula y deberá ser considerado como válido.
Si el nombre del platillo ingresado no existe, deberá indicarlo por medio de un mensaje y lo regresará al menú anterior."""

"""7.	Salir [10 puntos]
Al elegir la opción 4, terminará la ejecución de nuestra aplicación."""
