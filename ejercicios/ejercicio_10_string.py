#Ejercicio 10 
#Escribir un programa que pregunte por consola por los productos de una cesta de la 
#compra, separados por comas, y muestre por pantalla cada uno de los productos en 
#una línea distinta
lista_compra=input("Introduce los productos de la compra que quieres comprar separados por comas ")
print ("\n".join(lista_compra.split(",")))
