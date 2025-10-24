#Ejercicio 7 
#Escribir un programa que pregunte el correo electrónico del usuario en la consola y 
#muestre por pantalla otro correo electrónico con el mismo nombre (la parte delante 
#de la arroba @) pero con dominio ceu.es
correo=str(input("Introduzca su correo electrónico: "))
eliminar=correo.split("@")[0]
print ("Tu nuevo correo es ",eliminar+"@ceu.es")
