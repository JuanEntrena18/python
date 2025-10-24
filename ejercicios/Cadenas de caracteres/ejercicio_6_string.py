#Ejercicio 6 
#Escribir un programa que pida al usuario que introduzca una frase en la consola y 
#una vocal, y después muestre por pantalla la misma frase pero con la vocal 
#introducida en mayúscula.
frase=str(input("Introduce una frase: "))
vocal=str(input("Elige una vocal de la frase: "))
vocal.upper()
frase.replace(vocal,vocal.upper())
print ("La frase con las vocales en mayúsculas es: ", frase.replace(vocal,vocal.upper()))