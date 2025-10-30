#Ejercicio 3 
#Escribir un programa que pida al usuario un número entero positivo y muestre por 
#pantalla todos los números impares desde 1 hasta ese número separados por 
#comas
numero_usuario = int (input("DIme un número y te digo todos los impares separados por comas"))
contador = 1
while contador <= numero_usuario:
    print (contador, end=", ")
    contador += 2
   

