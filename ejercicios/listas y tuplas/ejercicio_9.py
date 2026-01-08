#Ejercicio 9 
#Escribir un programa que pida al usuario una palabra y muestre por pantalla el 
#número de veces que contiene cada vocal.
palabra = input("Dime una palabra y te digo las vocales que tine: ")
vocales = ["a","e","i","o","u","A","E","I","O","U"]
contador = 0
x = 0
while x < len(palabra):
    if palabra[x] in vocales:
        contador = contador + 1
    x = x + 1
print ("Hay", contador, "vocales en la palabra", palabra) 

