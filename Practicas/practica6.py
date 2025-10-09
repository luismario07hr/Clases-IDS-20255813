#SECCIÓN 6: Operadores de string y métodos
#•	Crea una variable frase = 'La programación es poderosa'. Muestra un mensaje si la palabra 'poderosa' está dentro de la frase.
frase = "La programación es poderosa"
boool = "poderosa" in frase

if boool == True:
    print("La palabra está en la frase")
else: 
    print ("La palabra no esta en la frase")
 
#•	Usa el operador not in para verificar si 'Java' no aparece en la frase anterior.

boool2 = "Java" not in frase
if boool2 == True:
    print("La palabra no está en la frase")
else: 
    print ("La palabra esta en la frase")

#•	Crea una variable palabra = 'hola' y muestra esa palabra repetida 5 veces usando *.
a = "hola"

print (a*5)
#•	Crea una variable texto = 'banana' y muestra cuántas veces aparece la letra 'a'.
b = "banana"
print (b.count("a"))

#•	Crea una variable mensaje = 'El Salvador es un gran país' y muestra la posición donde aparece la palabra 'gran' usando .index().
mesaje = "El Salvador es un gran país"

print (mesaje.index("gran"))