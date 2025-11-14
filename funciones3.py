def registro_profesor (nombre, apellido, **materias): #args(*) listas, quargs (**) diccionatios
    """Crea el registro de profesores"""
    print (f"El profesor {nombre}, {apellido}")
    for ciclo, materias in materias.items(): 
        print (f"\t - {ciclo}: \t {materias}")
    
registro_profesor ("Alvin", 
                   "Portillo", 
                   Ciclo1 = ["A", "B"],
                   Ciclo2 = ["B", "C"])