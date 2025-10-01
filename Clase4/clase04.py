usuario = "alvin"

cantidad_alumnos = 74 #string
media_edad = 18.23187879 #float
monto_hope = 1234.564567890
inversion_evento = -987654.234567898765

print (type(cantidad_alumnos))
print (type(media_edad))

print (type(cantidad_alumnos) is int) #Verdadero
print (type(media_edad) is int) # Falso

print (int(media_edad))

print("el usuario es", usuario, "y tiene", cantidad_alumnos,) #concatenado
print("y la edad promedio es", media_edad)

print(f"El usuario es {usuario}") 


print(f"y en aula con {cantidad_alumnos - 4} pajaritos en su aula")
print(f"con edad promedio de {media_edad:.2f} años") #.2f significa cual es el formato. (un punto co dos decimales fijos)
print (f"colectaros {monto_hope:,.2f} como un donativo")
print(f"y la totalidad de gastos fue de ${abs(inversion_evento):,.2f} dolares")

print (type(usuario) is str) #str = string

esta_lloviendo = False
print (type(monto_hope) is not bool) # is para que diga si es o no