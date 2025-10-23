#Ejercicio 11 
#Escribir un programa que pregunte el nombre el un producto, su precio y un número 
#de unidades y muestre por pantalla una cadena con el nombre del producto seguido 
#de su precio unitario con 6 dígitos enteros y 2 decimales, el número de unidades con 
#tres dígitos y el coste total con 8 dígitos enteros y 2 decimales. 
nombre=str(input("¿Cuál es el nombre del producto? "))
precio=float(input("¿Cuál es el precio del producto? " ))
unidades=int(input("Número de unidades "))
total= unidades * precio
print ("Has comprado", unidades, nombre, "a", f"{precio:09.2f}", "con un coste de", f"{total:11.2f}")

#uso de las f-strings: f"{nombre:ancho total, por ejemplo en el ejercicio 09 son 6 izquierda punto 2 derecha}