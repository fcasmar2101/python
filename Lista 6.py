asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]

for asignatura in asignaturas[:]: 
    nota = int(input(f"¿Qué nota has sacado en {asignatura}? "))
    
    if nota >= 5:
        asignaturas.remove(asignatura)

print("Tienes que repetir estas asignaturas:", asignaturas)