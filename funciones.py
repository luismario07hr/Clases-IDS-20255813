print("Hola mundo") #Una fución, "Hola Mundo" el argumento

#Este modulo va a contener funciones. Tiene dos tipos, definición y llamada

#definirla
def mi_funcion(): #Parentesis son los parámetros
    print ("Hola Mundo")
    print ("amigo usuario")
    print ("Gracias por usar nuestro sistema")

mi_funcion() #Paréntesis son los argumentos

#Recibir info

#Input dentro de la función
def capturar_nombre (): 
    nombre = input() #input es una función
    apellido = input()
    nombrecompleto = f"{nombre.capitalize()} {apellido.capitalize()}"
    print (nombrecompleto)
    
#capturar_nombre()

#Por argumentos
def caputrar_usuario(nombre, edad): 
    nombre_usuario = nombre
    edad_usuario = edad
    texto = f"El usuario {nombre_usuario.title()} tiene {edad_usuario} años"
    print (texto)

#caputrar_usuario (input(), input())

def calculo_impuesto (ventas): 
    if ventas < 500: 
        tasa_impuesto = 0.1
    else: 
        tasa_impuesto = 0.25
    return tasa_impuesto

ventas = 100
print (f"""El valor de la venta fue de {ventas}
       La tasa de impuestos es {calculo_impuesto(ventas)}
       y el monto es {calculo_impuesto(ventas)*ventas:,.2f}""")