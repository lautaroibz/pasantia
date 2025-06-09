
nombres = []
notas = []
buscar = ""
cantidad_aprobados = []
sum = 0
print("Ingrese los datos de 5 alumnos:")
for i in range(2):
    nombre = input(f"Ingrese el nombre del alumno {i+1}: ")
    nota = int(input(f"ingrese la nota del alumno: "))
    nombres.append(nombre)
    notas.append(nota)
    
while buscar!="salir":
    buscar = input(f"Escriba el nombre del alumno a buscar(o 'salir' para terminar): ")
    if buscar == "salir":
            break
    if buscar in nombres:
        indice = nombres.index(buscar)
        print(f"{buscar} tiene una nota de {notas[indice]}")
    else:
        print(f"Alumno no encontrado")

cantidad_aprobados = 0
for nota in notas:
    if nota >= 6:
        cantidad_aprobados+=1
if cantidad_aprobados == 0:
    print("No hay aprobados.")
else:
    porcentaje = (cantidad_aprobados / len(notas)) * 100
    print(f"Porcentaje de aprobados: {porcentaje:.2f}%")