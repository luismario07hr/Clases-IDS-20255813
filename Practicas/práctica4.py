#SECCIÓN 4: f-strings y formato de salida
#•	Crea tres variables (nombre, producto, precio) y muestra el mensaje: Hola Ana, el producto Laptop cuesta $1200.00 usando una f-string.
"""nombre = "Ana"
producto = "Laptop"
precio = 1200

print (f"Hola {nombre}, el producto {producto} cuesta ${float(precio)}")"""

#•	Pide el nombre y el país de un usuario y muestra: Hola, Carlos de El Salvador, ¡bienvenido!.
"""nombre1 = input("Hola, dame tu nombre:")
pais = input ("¿De qué país eres?")

print (f"Hola {nombre1} de {pais}, ¡bienvenido!")"""

#•	Crea un mini formulario que pida nombre, edad y ciudad, y luego muestre un resumen de la información en varias líneas usando f-strings.

"""print ("Ingresa tus datos")
a = input("Nombre")
b = int(input("Edad"))
c = input ("Ciudad")

print (f"Nombre proporcionado: {a}")
print (f"Edad proporcionada: {b}")
print (f"Ciudad de procedencia: {c}")"""


#•	Muestra el área de un rectángulo con base y altura dadas por el usuario. El resultado debe aparecer con dos decimales.
 
"""a = float(input())
h = float(input())
 
print (f"{a*h: .2f}")"""

#•	Muestra una tabla como esta: Producto: Pan, Precio: $1.50, Cantidad: 4, Total: $6.00 (Usa variables y f-strings).

a = input ("Producto: ")
b = float(input("Precio del prodcuto: "))
c = int(input("Cantidad: "))

print (f"Prodcuto: {a}, Precio: ${b: .2f}, Cantidad: {c}. Total a pagar: ${float(b*c): .2f}")
