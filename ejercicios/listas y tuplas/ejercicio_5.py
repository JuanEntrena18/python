#Ejercicio 5 
#Escribir un programa que almacene en una lista los números del 1 al 10 y los 
#muestre por pantalla en orden inverso separados por comas.
numeros = [1,2,3,4,5,6,7,8,9,10]
numeros.reverse()
print (numeros)
## print (* variable) elimina las comas
print(*numeros)
## print sep añade deparador entre los objetos del array
print(*numeros, sep =", ")
## usando replace ponemos las comas donde haga falta
print (str(numeros).replace('[','').replace(']',''))

