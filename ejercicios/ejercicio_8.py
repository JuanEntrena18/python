#Ejercicio 8 
#Escribir un programa que pida al usuario dos números enteros y muestre por 
#pantalla la <n> entre <m> da un cociente <c> y un resto <r> donde 
#<n> y <m> son los números introducidos por el usuario, y <c> y <r> son el cociente 
#y el resto de la división entera respectivamente.
numero_1=int(input("Introduce el primer número "))
numero_2=int(input("Introduce el segundo número "))
cociente=numero_1 / numero_2
resto=numero_1 % numero_2
print (numero_1,"entre",numero_2,"da un cociente de",cociente,"y un resto de",resto)