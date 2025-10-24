#Ejercicio 6 
#Los alumnos de un curso se han dividido en dos grupos A y B de acuerdo al sexo y 
#el nombre. El grupo A está formado por las mujeres con un nombre anterior a la M y 
#los hombres con un nombre posterior a la N y el grupo B por el resto. Escribir un 
#programa que pregunte al usuario su nombre y sexo, y muestre por pantalla el grupo 
#que le corresponde.
nombre=str(input("¿Cuál es tu nombre? ")).lower()
sexo=str(input("Introduce tu sexo, Hombre o Mujer:" )).lower()
inicial = nombre [0]
if (inicial < "m" and sexo == "mujer") or ((inicial < "n" and sexo == "hombre")):
    print ("Vas al grupo A")
else:
    print ("Vas al grupo B")