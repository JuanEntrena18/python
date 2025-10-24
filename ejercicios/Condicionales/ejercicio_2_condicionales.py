#Ejercicio 2 
#Escribir un programa que almacene la cadena de caracteres contraseña en una 
#variable, pregunte al usuario por la contraseña e imprima por pantalla si la 
#contraseña introducida por el usuario coincide con la guardada en la variable sin 
#tener en cuenta mayúsculas y minúsculas
contrasena = str(input("Introduce tu contraseña de 8 caracteres, solo letras "))
comprobar= input ("Introduce de nuevo tu contraseña ")
if comprobar.lower() == contrasena.lower():
    print ("Tu contraseña es la misma")
else:
    print ("Contraseña incorrecta")
 