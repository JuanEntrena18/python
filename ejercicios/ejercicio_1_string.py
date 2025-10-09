#Ejercicio 1
#Escribir un programa que pregunte el nombre del usuario en la consola y un número
#entero e imprima por pantalla en líneas distintas el nombre del usuario tantas veces
#como el número introducido.
nombre=str(input("¿Cuál es tu nombre de usuario "))
multi=int(input("¿Cuántas veces quieres que se repita el nombre? "))
print ((nombre + "\n")* multi)