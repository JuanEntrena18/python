#Ejercicio 8 
#Escribir un programa que pida al usuario una palabra y muestre por pantalla si es un 
#palíndromo. 
## Método string inverso
palabra = input("Dime una palabra ").lower()
if palabra == palabra[::-1]:
    print("La palabra", palabra, "es palíndromo")
else:
    print("La palabra", palabra, "no es palíndromo") 
## Método array
palabra = input("Dime una palabra ").lower()
x = list(palabra)
y = len(palabra)