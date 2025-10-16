#Ejercicio 8 
#Escribir un programa que pregunte por consola el precio de un producto en euros 
#con dos decimales y muestre por pantalla el número de euros y el número de 
#céntimos del precio introducido.
pregunta=float(input("¿Cual es el precio del producto? "))
precio_redo=round(pregunta,2)
euros=int(precio_redo)
centimos=precio_redo-euros
print ("Te ha dado ",pregunta, "que son ", euros, "euros con", centimos, "centimos")

