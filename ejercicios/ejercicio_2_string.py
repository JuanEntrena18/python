#Ejercicio 2
#Escribir un programa que pregunte el nombre completo del usuario en la consola y
#después muestre por pantalla el nombre completo del usuario tres veces, una con
#todas las letras minúsculas, otra con todas las letras mayúsculas y otra solo con la
#primera letra del nombre y de los apellidos en mayúscula. El usuario puede
#introducir su nombre combinando mayúsculas y minúsculas como quiera.
nombre=str(input("¿Cuál es tu nombre "))
apellido1=str(input("¿Cuál es tu primer apellido "))
apellido2=str(input("¿Cuál es tu segundo apellido "))
print ("Tu nombre completo es ", nombre.lower() +"", apellido1.lower() +"", apellido2.lower())
print ("Tu nombre completo es ", nombre.upper() +"", apellido1.upper() +"", apellido2.upper())
print ("Tu nombre completo es ", nombre.title() +"", apellido1.title() +"", apellido2.title())