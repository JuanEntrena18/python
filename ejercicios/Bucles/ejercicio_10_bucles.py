#Ejercicio 10 
#Escribir un programa que pida al usuario un número entero y muestre por pantalla si 
#es un número primo o no.
n = int(input("Introduce un número entero y te digo si es primo o no "))
contador = 0
for i in range (1,n + 1):
    if (n % i == 0):
        contador = contador +1
if contador <= 2:
        print ("El número es primo")
else:
        print ("El número no es primo")