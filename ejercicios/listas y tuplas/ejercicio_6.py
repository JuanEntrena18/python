#Ejercicio 6 
#Escribir un programa que almacene las asignaturas de un curso (por ejemplo 
#Matemáticas, Física, Química, Historia y Lengua) en una lista, pregunte al usuario la 
#nota que ha sacado en cada asignatura y elimine de la lista las asignaturas 
#aprobadas. Al final el programa debe mostrar por pantalla las asignaturas que el 
#usuario tiene que repetir.
asignaturas = ["Matemáticas", "Física", "Química", "Historia", "Lengua"]
notas = []
## Al contrario de en el ejercicio 3, hay que usar float para luego hacer el IF
for asignatura in asignaturas:
    nota = float(input("¿Qué nota has sacado en " + asignatura + "? "))
    notas.append(nota)
## Para hacer operaciones con números hay que indicarle float/int a la variable de arriba
asignaturas_repetir = []
for i in range(len(asignaturas)):
    if notas[i] < 5:
        asignaturas_repetir.append(asignaturas[i])

print("Tienes que repetir las siguientes asignaturas: ", *asignaturas_repetir)


