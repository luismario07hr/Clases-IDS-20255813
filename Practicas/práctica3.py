#Crea tres variables: a = 10, b = 3, c = 5. Calcula y muestra: la suma de a y b, el resultado de a dividido entre b, el residuo de dividir a entre c.
a = 10
b = 3
c = 5
d = a + b

print (d)
print (d/3)
print (a%c) #el % es para que devuelca el residuo

#Crea una variable numero con valor 7 y muestra True si es mayor que 5, False en caso contrario.

num = 4
condicional = num > 5

print (condicional)

#Crea dos variables x = 10, y = 10. Usa los operadores is e is not para verificar si apuntan al mismo objeto en memoria.
x = 10
y = 10
veri = x is y
veri2 = x is not y

print (veri)
print (veri2)

#Pide un número al usuario y muestra True si es par, False si es impar (usa el operador %).

numero = int(input("dime un numero"))

print (numero % 2 == 0) #Divido entre dos, los número pares no tienen residuo (el residuo es 0) 


#Crea una variable booleana registrado = True. Usa operadores lógicos (and, or, not) para mostrar combinaciones posibles.
bol = True

print (bol and True)
print (bol and False)
print (bol or True)
print (bol or False)
print (not bol)
print (not False)

#Pide al usuario dos números y muestra si el primero es mayor o igual que el segundo.
num1 = int(input("Ingresa un número entero: "))
num2 = int(input("Ingresa otro número entero"))
boo = num1 >  num2
print (f"{boo}")


#Pide al usuario su edad y muestra si tiene edad suficiente para votar (mayor o igual que 18).
a = int(input("¿Cuál es tu edad?: "))
b = a >= 18

print (f"¿Tienes la edad suficiente?:{b}")

#Crea un ejemplo que combine operadores relacionales y lógicos, como: edad = 22; estudiante = True; print(edad >= 18 and estudiante).

num_students = int(input("Ingrese el número de estudiantes en su salón:"))
compa = num_students > 50

print (compa and False)