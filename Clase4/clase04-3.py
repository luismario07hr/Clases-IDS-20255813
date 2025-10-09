my_string = "ABCDEFHI"
letra1 = int(input("indique el indice de la letra a probrar (del 0 al 9):")) #input es naturalmente string
letra2 = int(input("indique hasta qué letra debe llegar (del 0 al 9):"))
print (my_string[letra1:letra2:2]) #se incluye el primero y no el segundo, el 2 es saltos cada dos. Es subsetting por slices

comparación1 = letra2 < letra1
print(comparación1)

print("H" not in my_string)
print (my_string*3)
print (max(my_string))

print (my_string is int)

print (my_string.count("A")) #.count es el metodo a usar