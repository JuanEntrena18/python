#Ejercicio 10 
#Escribir un programa que almacene en una lista los siguientes precios, 50, 75, 46, 
#22, 80, 65, 8, y muestre por pantalla el menor y el mayor de los precios.
precios = [50,75,46,22,80,65,8]
x = 0
mayor = 0
menor = 100000
while x < len(precios):
    if precios[x] > mayor:
        mayor = precios[x]
    elif precios[x] < menor:
        menor = precios[x]
    x = x + 1
    
print ("El numero mayor es ", mayor,"y el número menor es", menor)