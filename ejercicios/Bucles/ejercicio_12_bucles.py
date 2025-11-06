#Ejercicio 12 
#Escribir un programa en el que se pregunte al usuario por una frase y una letra, y 
#muestre por pantalla el número de veces que aparece la letra en la frase.
frase = input("Introduce una frase y te digo el número de veces que está una letra repetida ")
letra = input("Introduce la letra")
contador = 0
for caracter in frase:
    if caracter == letra:
        contador = contador +1
##La f le dice a python que es un string formateado
print (f"La letra",letra,"aparece",contador,"veces")