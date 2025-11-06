#Ejercicio 9 
#Escribir un programa que almacene la cadena de caracteres contraseña en una 
#variable, pregunte al usuario por la contraseña hasta que introduzca la contraseña 
#correcta.
password = input("Introduzca su contraseña, solo letras ")
comprobacion = input("Vamos a comprobar tu contraseña ")
while password != comprobacion:
    input("Te has equivocado de contraseña ")


